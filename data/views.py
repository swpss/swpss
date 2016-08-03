import json

from datetime import datetime, timedelta

from rest_framework import views
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from data.models import Dataset
from data.serializers import DatasetSerializer, LPDDataSerializer, MultipleLPDDataSerializer
from data.serializers import PowDataSerializer
from data.pagination import DatasetPagination
from data.lpm import lpm_calculator
from machines.models import Machine, MachineDetail
from users.models import Account
from users.helper import AccountTypes
from django.http import HttpResponse
import data.gfmnn as g



class DatasetView(ListAPIView):
    pagination_class = DatasetPagination
    serializer_class = DatasetSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'm_id'

    def get_queryset(self):
        m_id = self.kwargs.get(self.lookup_field)

        if m_id is not None:
            machine = Machine.objects.get(m_id=m_id)
            return Dataset.objects.filter(
                    machine=machine).order_by('-timestamp')
        return None


class DataWithRange(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = DatasetSerializer
    lookup_field = 'm_id'

    def get_queryset(self):
        m_id = self.kwargs.get(self.lookup_field)
        begin_date = self.request.query_params.get('s', None)
        end_date = self.request.query_params.get('e', None)

        begin_date, end_date = map(
                lambda x: datetime.strptime(x, '%Y-%m-%d'),
                [begin_date, end_date])
        end_date += timedelta(days=1)

        if m_id is not None:
            machine = Machine.objects.get(m_id=m_id)

            if begin_date is not None and end_date is not None:
                return Dataset.objects.filter(
                        machine=machine).filter(
                            timestamp__gt=begin_date).filter(
                                timestamp__lt=end_date)

        return None


class GetRecentData(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, m_id, format=None):
        data = Dataset.objects.filter(
                serial_no=m_id
                ).filter(timestamp__gt=request.query_params['t'])
        serialized = DatasetSerializer(data, many=True)
        return Response(data=serialized.data)

class GetLPDData(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, m_id, format=None):
        machine = Machine.objects.get(m_id=m_id)
        period = request.query_params.get('period', None)

        if period is None or period == 'day':
            data_arr = Dataset.objects.filter(machine=machine).filter(
                                timestamp__gte=datetime.now() -
                                timedelta(days=1)).order_by('timestamp')
        elif period == 'week':
            data_arr = Dataset.objects.filter(machine=machine).filter(
                                timestamp__gte=datetime.now() -
                                timedelta(days=7)).order_by('timestamp')
        else:
            data_arr = Dataset.objects.filter(machine=machine).filter(
                                timestamp__gte=datetime.now() -
                                timedelta(days=30)).order_by('timestamp')

        summary_data = {}
        summary_arr = []
        pump_on = False
        start_time = None
        end_time = None
        total_duration = 0

        if len(data_arr) == 0:
            return Response([])

        for dataset in data_arr:
            date = dataset.timestamp.date()
            data = dataset.data

            if date in summary_data.keys():
                if data['due_to'] == 0:
                    if pump_on:
                        summary_data[date]['et'] = dataset.timestamp
                    else:
                        pump_on = True
                        start_time = dataset.timestamp
                        if summary_data[date]['st'] is None:
                            summary_data[date]['st'] = start_time
                else:
                    if pump_on:
                        pump_on = False
                        end_time = summary_data[date]['et']
                        total_duration += (end_time - start_time).seconds 
            else:
                summary_data[date] = {
                    'st': None, 'et': None, 'lpm_arr': [],
                    'avg_lpm': None, 't_duration': None, 'lpd': None
                }
                pump_on = False

                if data['due_to'] == 0:
                    summary_data[date]['st'] = dataset.timestamp
                    pump_on = True
                    start_time = summary_data[date]['st']
                else:
                    pass

            if data['due_to'] == 0:
                summary_data[date]['lpm_arr'].append(dataset.data['lpm'])


            if summary_data[date]['et'] == end_time:
                summary_data[date]['t_duration'] = total_duration 
            else:
                summary_data[date]['t_duration'] = \
                total_duration +(summary_data[date]['et']- start_time).seconds

        for key,value in summary_data.items():
            if len(summary_data[key]['lpm_arr']) == 0:
                summary_data[key]['avg_lpm'] = 0
            else:
                summary_data[key]['avg_lpm'] = sum(summary_data[key]['lpm_arr'])/len(summary_data[key]['lpm_arr'])
                summary_data[key].pop('lpm_arr')

            summary_data[key]['lpd'] = summary_data[key]['avg_lpm'] * (summary_data[key]['t_duration'] / float(60))

        
        for (key, value) in summary_data.iteritems():
            value['date'] = key
            summary_arr.append(value)

        summary_arr = sorted(summary_arr, key=lambda k: k['date'])

        serialized = LPDDataSerializer(summary_arr, many=True)
        return Response(serialized.data)



class GetLPDDataAnalysis(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, format=None):
        ACCOUNT_TYPES = AccountTypes.to_dict()

        if self.request.user.account_type == ACCOUNT_TYPES['SUPPLIER']:
            queryset = Machine.objects.filter(sold_by=self.request.user)
        elif self.request.user.account_type == ACCOUNT_TYPES['ELECTRICITY_OFFICER'] \
                or self.request.user.account_type == ACCOUNT_TYPES['NODAL_OFFICER']:
                    queryset = Machine.objects.filter(
                            location=self.request.user.location
                        )
        elif self.request.user.account_type == ACCOUNT_TYPES['FARMER']:
            queryset = Machine.objects.filter(bought_by=self.request.user)
        else:
            queryset = Machine.objects.all()
        summary_arr=[]
        for i in queryset:
            uid = i.m_id
            machine = Machine.objects.get(m_id=uid)
            period = 30 
            data_arr = Dataset.objects.filter(machine=machine).filter(timestamp__gte=datetime.now() - timedelta(days=30)).order_by('timestamp') 
            summary_data = {} 
            summary_arr1 = [] 
            pump_on = False 
            start_time = None 
            end_time = None 
            total_duration = 0 
            for dataset in data_arr: 
                date = dataset.timestamp.date() 
                data = dataset.data 
                if date in summary_data.keys(): 
                    if data['due_to'] == 0: 
                        if pump_on: 
                            summary_data[date]['et'] = dataset.timestamp 
                        else: 
                            pump_on = True 
                            start_time = dataset.timestamp 
                            if summary_data[date]['st'] is None: 
                                summary_data[date]['st'] = start_time 
                    else: 
                        if pump_on: 
                            pump_on = False 
                            end_time = summary_data[date]['et'] 
                            total_duration += (end_time - start_time).seconds 
                else: 
                    summary_data[date] = {'st': None, 'et': None, 'lpm_arr': [], 'avg_lpm': None, 't_duration': None, 'lpd': None } 
                    pump_on = False 
                    if data['due_to'] == 0: 
                        summary_data[date]['st'] = dataset.timestamp 
                        pump_on = True 
                        start_time = summary_data[date]['st'] 
                    else: 
                        pass 
                if data['due_to'] == 0: 
                    summary_data[date]['lpm_arr'].append(dataset.data['lpm']) 
                if summary_data[date]['et'] == end_time: 
                    summary_data[date]['t_duration'] = total_duration 
                else: 
                    summary_data[date]['t_duration'] = total_duration +(summary_data[date]['et']- start_time).seconds 
            for key,value in summary_data.items(): 
                if len(summary_data[key]['lpm_arr']) == 0: 
                    summary_data[key]['avg_lpm'] = 0 
                else:
                    summary_data[key]['avg_lpm'] = sum(summary_data[key]['lpm_arr'])/len(summary_data[key]['lpm_arr']) 
                    summary_data[key].pop('lpm_arr') 
                summary_data[key]['lpd'] = summary_data[key]['avg_lpm'] * (summary_data[key]['t_duration'] / float(60)) 
                summary_data[key]['uid'] = uid
            for (key, value) in summary_data.iteritems(): 
                value['date'] = key 
                summary_arr1.append(value) 
        
            summary_arr1 = sorted(summary_arr1, key=lambda k: k['date'])

        
            summary_arr = summary_arr+summary_arr1
        #convert summary arr to Data table used for charts

        #actual json format example for two machines lpd will be {date: date  1: lpd of one 2: lpd of two}
        idSet = []
        dateSet = []
        summary = []
        arr = {}

        for i in range(0,len(summary_arr)):
            idSet.append('id'+summary_arr[i]['uid'])
            dateSet.append(summary_arr[i]['date'])

        idSet = list(set(idSet))
        dateSet = list(set(dateSet))
        for i in range(0,len(dateSet)):
            arr[i]={'date': None , 'avg' : None}
            arr[i]['date']=dateSet[i]
            count = 0
            var1 = 0
            for k in range(0,len(summary_arr)):
                if(dateSet[i]==summary_arr[k]['date']):
                    var1 = var1+summary_arr[k]['lpd']
                    count=count+1
                    
            arr[i]['avg']=var1/count

        for i in range(0,len(arr)):
            summary.append(arr[i])
        #serialized = MultipleLPDDataSerializer(summary_arr, many=True)
        return Response(summary)


class GetLPDDataAnalysis1(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, format=None):
        ACCOUNT_TYPES = AccountTypes.to_dict()

        if self.request.user.account_type == ACCOUNT_TYPES['SUPPLIER']:
            queryset = Machine.objects.filter(sold_by=self.request.user)
        elif self.request.user.account_type == ACCOUNT_TYPES['ELECTRICITY_OFFICER'] \
                or self.request.user.account_type == ACCOUNT_TYPES['NODAL_OFFICER']:
                    queryset = Machine.objects.filter(
                            location=self.request.user.location
                        )
        elif self.request.user.account_type == ACCOUNT_TYPES['FARMER']:
            queryset = Machine.objects.filter(bought_by=self.request.user)
        else:
            queryset = Machine.objects.all()
        summary_arr=[]
        for i in queryset:
            uid = i.m_id
            machine = Machine.objects.get(m_id=uid)
            period = 30 
            data_arr = Dataset.objects.filter(machine=machine).filter(timestamp__gte=datetime.now() - timedelta(days=30)).order_by('timestamp') 
            summary_data = {} 
            summary_arr1 = [] 
            pump_on = False 
            start_time = None 
            end_time = None 
            total_duration = 0 
            for dataset in data_arr: 
                date = dataset.timestamp.date() 
                data = dataset.data 
                if date in summary_data.keys(): 
                    if data['due_to'] == 0: 
                        if pump_on: 
                            summary_data[date]['et'] = dataset.timestamp 
                        else: 
                            pump_on = True 
                            start_time = dataset.timestamp 
                            if summary_data[date]['st'] is None: 
                                summary_data[date]['st'] = start_time 
                    else: 
                        if pump_on: 
                            pump_on = False 
                            end_time = summary_data[date]['et'] 
                            total_duration += (end_time - start_time).seconds 
                else: 
                    summary_data[date] = {'st': None, 'et': None, 'lpm_arr': [], 'avg_lpm': None, 't_duration': None, 'lpd': None } 
                    pump_on = False 
                    if data['due_to'] == 0: 
                        summary_data[date]['st'] = dataset.timestamp 
                        pump_on = True 
                        start_time = summary_data[date]['st'] 
                    else: 
                        pass 
                if data['due_to'] == 0: 
                    summary_data[date]['lpm_arr'].append(dataset.data['lpm']) 
                if summary_data[date]['et'] == end_time: 
                    summary_data[date]['t_duration'] = total_duration 
                else: 
                    summary_data[date]['t_duration'] = total_duration +(summary_data[date]['et']- start_time).seconds 
            for key,value in summary_data.items(): 
                if len(summary_data[key]['lpm_arr']) == 0: 
                    summary_data[key]['avg_lpm'] = 0 
                else:
                    summary_data[key]['avg_lpm'] = sum(summary_data[key]['lpm_arr'])/len(summary_data[key]['lpm_arr']) 
                    summary_data[key].pop('lpm_arr') 
                summary_data[key]['lpd'] = summary_data[key]['avg_lpm'] * (summary_data[key]['t_duration'] / float(60)) 
                summary_data[key]['uid'] = uid
            for (key, value) in summary_data.iteritems(): 
                value['date'] = key 
                summary_arr1.append(value) 
        
            summary_arr1 = sorted(summary_arr1, key=lambda k: k['date'])

        
            summary_arr = summary_arr+summary_arr1

        #convert summary arr to Data table used for charts

        #actual json format example for two machines lpd will be {date: date  1: lpd of one 2: lpd of two}
            idSet = []
            dateSet = []
            summary = []
            arr = {}

            for i in range(0,len(summary_arr)):
                idSet.append(summary_arr[i]['uid'])
                dateSet.append(summary_arr[i]['date'])

            idSet = list(set(idSet))
            dateSet = list(set(dateSet))

            for i in range(0,len(dateSet)):
                arr[i] = {'date' : None}
                arr[i]['date'] = dateSet[i]
                count=0
                for j in range(0,len(idSet)):
                    arr[i].update({'id'+idSet[j]:None})
                    for k in range(0,len(summary_arr)):
                        if(idSet[j]==summary_arr[k]['uid'] and dateSet[i]==summary_arr[k]['date']):
                            arr[i]['id'+idSet[j]] = summary_arr[k]['lpd']
                            count=count + 1
                if(count<1):
                    arr[i]['id'+idSet[i]] = 0


        for i in range(0,len(arr)):
            summary.append(arr[i])
        a = []
        print summary
        for j in summary:
            a.append({"date":j["date"], "avg":""})
            del(j["date"])
            lp_value_list = [x for x in j.values() if x is not None]
            print lp_value_list
            if len(lp_value_list)==0:
                avg = lp_value_list[0]
                summary[summary.index(j)]["avg"] = avg
                summary[summary.index(j)]["date"] = a[summary.index(j)]["date"]
            elif len(lp_value_list)==1:
                avg = lp_value_list[0]
                summary[summary.index(j)]["avg"] = avg
                summary[summary.index(j)]["date"] = a[summary.index(j)]["date"]
            elif len(lp_value_list) == 2:
                avg = (lp_value_list[0] + lp_value_list[1])/2
                summary[summary.index(j)]["avg"] = avg
                summary[summary.index(j)]["date"] = a[summary.index(j)]["date"]
            elif (len(lp_value_list)%2 == 0) and len(lp_value_list) > 2:
                avg = (lp_value_list[len(lp_value_list)/2] + lp_value_list[(len(lp_value_list)/2)+1])/2
                summary[summary.index(j)]["avg"] = avg
                summary[summary.index(j)]["date"] = a[summary.index(j)]["date"]
            else:
                avg = (lp_value_list[len(lp_value_list)/2] + lp_value_list[(len(lp_value_list)/2)+1])/2
                summary[summary.index(j)]["avg"] = avg
                summary[summary.index(j)]["date"] = a[summary.index(j)]["date"]
        return Response(summary)



class GetPowData(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, m_id, format=None):
        machine = Machine.objects.get(m_id=m_id)

        period = request.query_params.get('period', None)

        if period is None or period == 'day':
            data_arr = Dataset.objects.filter(machine=machine).filter(
                                timestamp__gte=datetime.now() -
                                timedelta(days=1)).order_by('timestamp')
        elif period == 'week':
            data_arr = Dataset.objects.filter(machine=machine).filter(
                                timestamp__gte=datetime.now() -
                                timedelta(days=7)).order_by('timestamp')
        else:
            data_arr = Dataset.objects.filter(machine=machine).filter(
                                timestamp__gte=datetime.now() -
                                timedelta(days=30)).order_by('timestamp')

        summary_data = {}
        summary_arr = []
        pump_on = False
        start_time = None
        end_time = None
        total_duration = 0

        if len(data_arr) == 0:
            return Response([])

        for dataset in data_arr:
            date = dataset.timestamp.date()
            data = dataset.data

            if date in summary_data.keys():
                if data['due_to'] == 0:
                    if pump_on:
                        summary_data[date]['et'] = dataset.timestamp
                    else:
                        pump_on = True
                        start_time = dataset.timestamp
                        if summary_data[date]['st'] is None:
                            summary_data[date]['st'] = start_time
                else:
                    if pump_on:
                        pump_on = False
                        end_time = summary_data[date]['et']
                        total_duration += (end_time - start_time).seconds 
            else:
                summary_data[date] = {
                    'st': None, 'et': None, 'pow_arr': [],
                    'avg_pow': None, 't_duration': None, 'pow_h': float
                }
                pump_on = False

                if data['due_to'] == 0:
                    summary_data[date]['st'] = dataset.timestamp
                    pump_on = True
                    start_time = summary_data[date]['st']
                else:
                    pass

            if data['due_to'] == 0:
                summary_data[date]['pow_arr'].append(dataset.data['power'])

            if summary_data[date]['et'] == end_time:
                summary_data[date]['t_duration'] = total_duration 
            else:
                summary_data[date]['t_duration'] = \
                    total_duration +(summary_data[date]['et']- start_time).seconds

        for key,value in summary_data.items():
            if len(summary_data[key]['pow_arr']) == 0:
                summary_data[key]['avg_pow'] = 0
            else:
                summary_data[key]['avg_pow'] = sum(summary_data[key]['pow_arr'])/len(summary_data[key]['pow_arr'])
                summary_data[key].pop('pow_arr')


            summary_data[key]['pow_h'] = summary_data[key]['avg_pow'] * (summary_data[key]['t_duration'] / float(3600))


        for (key, value) in summary_data.iteritems():
            value['date'] = key
            summary_arr.append(value)

        summary_arr = sorted(summary_arr, key=lambda k: k['date'])

        serialized = PowDataSerializer(summary_arr, many=True)
        return Response(serialized.data)


class DataInsert(views.APIView):
    """
    TODO: GET request to add data

    QUERY PARAMS:
    mid -> mid number of the machine's ID

    Model:
    s -> status (1 or 0)
    d -> due_to (enum: 0-5)
    v -> voltage
    i -> current
    f -> frequency
    t -> timestamp
    p -> power
    c -> output current
    r -> output voltage
    lpm -> Litres per minute

    TODO: Determine formulae for power, avg_p, lpm
    TODO: If saved properly return 1 as response or else 0
    TODO: Auth mechanism for machines.
    """
    def get(self, request, format=None):
        PUMPING_FACTOR = 305.0

        m_id = int(request.query_params.get('mid', None))
        machine = Machine.objects.get(m_id=m_id)
        model = machine.model

        # TODO: Convert all query params to float and then to string
        status = str(float(request.query_params.get('s', 0)))
        due_to = str(float(request.query_params.get('d', 0)))
        voltage = str(float(request.query_params.get('v', 0)))
        current = str(float(request.query_params.get('i', 0)))
        frequency = str(float(request.query_params.get('f', 0)))
        output_current = str(float(request.query_params.get('c', 0)))
        output_voltage = str(float(request.query_params.get('r', 0)))

        if voltage == 0 and current == 0 and frequency == 0 \
                and due_to == 0 and status == 0:
                    return Response(data='0')

        if None not in [voltage, current, frequency]:
            power = str((float(current) * float(voltage)) / 1000)
            lpm = str(lpm_calculator(
                    machine.depth_during_installation,
                    model.ref_head,
                    model.ref_head_lpm,
                    model.pump_type,
                    model.horse_power,
                    float(power),
                    float(frequency)
                ))
        else:
            return Response(data='0')

        data = dict(
            machine=machine.id,
            serial_no=m_id,
            data=dict(
                status=status,
                due_to=due_to,
                voltage=voltage,
                current=current,
                frequency=frequency,
                power=power,
                lpm=lpm,
                output_current=output_current,
                output_voltage=output_voltage
            )
        )

        serialized_data = DatasetSerializer(data=data)

        if serialized_data.is_valid():
            serialized_data.save()
        else:
            return Response(data='0')

        return Response(data='1')



class faultAnalysis(views.APIView):
    permission_classes = (IsAuthenticated, )
    def get(self,format=None):
        ACCOUNT_TYPES = AccountTypes.to_dict()

        if self.request.user.account_type == ACCOUNT_TYPES['SUPPLIER']:
            queryset = Machine.objects.filter(sold_by=self.request.user)
        elif self.request.user.account_type == ACCOUNT_TYPES['ELECTRICITY_OFFICER'] or self.request.user.account_type == ACCOUNT_TYPES['NODAL_OFFICER']:
            queryset = Machine.objects.filter(location=self.request.user.location)
        elif self.request.user.account_type == ACCOUNT_TYPES['FARMER']:
            queryset = Machine.objects.filter(bought_by=self.request.user)
        else:
            queryset = Machine.objects.all()
        arr1 = []
        data_res = []
        arr = []
        states = [1.0, 2.0, 3.0, 4.0, 6.0]
        machine = Machine.objects.get(m_id=self.request.GET["mid"])
        date_set = Dataset.objects.filter(machine = machine).filter(timestamp__gte=datetime.now()-timedelta(days=1)).order_by('timestamp')
        hour_set = Dataset.objects.filter(machine = machine).filter(timestamp__gte=datetime.now()-timedelta(hours=1)).order_by('timestamp')
        data_day = []
        data_hour = []
        for dat in date_set:
            data_day.append(dat.data["due_to"])
        for dat in hour_set:
            data_hour.append(dat.data["due_to"])     
        for state in states:
            state_data = {"id":machine.m_id}
            state_data["state"] = state
            state_data["day"] = data_day.count(state)
            state_data["hour"] = data_hour.count(state)
            data_res.append(state_data)
        print data_res    
        for i in range(0,len(data_res)):
            if data_res[i]["day"]>=5:
                if (data_res[i]["state"]==1.0 or data_res[i]["state"]==6.0):
                    g.inputs=[data_res[i]["state"],2,data_res[i]["day"]]
                else:
                    g.inputs=[data_res[i]["state"],1,data_res[i]["hour"]]
                g.initialize()
                hyp = g.initclass()
                arr.append(g.inputs)
                arr.append(hyp)
        arr1.append(arr)    
        print arr1                
        return Response(arr1)   


class MachineStatus(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,format=None):
        machine =  Machine.objects.get(m_id=self.request.GET["mid"])
        data_set = Dataset.objects.filter(machine = machine, timestamp__gte=datetime.now()-timedelta(hours=datetime.now().hour, minutes = datetime.now().minute, seconds = datetime.now().second))
        status_machine = data_set.last() 
        return Response(status_machine.data)       
