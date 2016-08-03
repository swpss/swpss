from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from machines.models import MachineDetail, Machine
from machines.serializers import MachineSerializer, MachineDetailSerializer
from machines.permissions import IsAllowedToAlter, IsAllowedToSell
from machines.pagination import MachinePagination
from users.models import Account
from users.helper import AccountTypes
from data.models import Dataset


class DefaultsMixin(object):
    authentication_classes = (TokenAuthentication, )


class SellMachinesMixin(DefaultsMixin):
    permission_classes = (IsAuthenticated, IsAllowedToSell, )


class AddMachineDetailMixin(DefaultsMixin):
    permission_classes = (IsAuthenticated, IsAllowedToAlter, )


class MachineDetailsViewSet(AddMachineDetailMixin, viewsets.ModelViewSet):
    queryset = MachineDetail.objects.all()
    serializer_class = MachineDetailSerializer


class MachineViewSet(SellMachinesMixin, viewsets.ModelViewSet):
    serializer_class = MachineSerializer
    pagination_class = MachinePagination

    def get_queryset(self):
        """
        Returns a list of machines based on the user type.
        Account types can be found in users/helper.py
        """
        ACCOUNT_TYPES = AccountTypes.to_dict()

        if self.request.user.account_type == ACCOUNT_TYPES['SUPPLIER']:
            queryset = Machine.objects.filter(sold_by=self.request.user)
        elif self.request.user.account_type == ACCOUNT_TYPES['ELECTRICITY_OFFICER'] \
                or self.request.user.account_type == ACCOUNT_TYPES['NODAL_OFFICER']:
                    queryset = Machine.objects.filter(
                            location=self.request.user.location
                        )
        elif self.request.user.account_type == 6:
            client = Account.objects.get(id=self.request.user.client)
            queryset = Machine.objects.filter(sold_by=client)   
        elif self.request.user.account_type == 7:
            queryset = Machine.objects.filter(location=self.request.user.location)   
        elif self.request.user.account_type == ACCOUNT_TYPES['FARMER']:
            queryset = Machine.objects.filter(bought_by=self.request.user)
        else:
            queryset = Machine.objects.all()

        return queryset


class MachineStatus(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,format=None):
        machine =  Machine.objects.get(m_id=self.request.GET["mid"])
        data_set = Dataset.objects.filter(machine = machine)
        status_machine = data_set.last() 
        return Response(status_machine.data)       


# class GetMachineDetails(DefaultsMixin, APIView):
#     # url-format: /machine-detail?model_id=<model_id>
#
#     def get(self, request, format=None):
#         machine_detail = MachineDetail.objects.filter(
#                 id=request.query_params.get('email', None)
#         )
#
#         return Response(machine_detail.values())
