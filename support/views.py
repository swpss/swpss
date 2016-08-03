import json

from rest_framework.response import Response
from rest_framework import views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from support import serializers
from support.models import Issue, Reason, Solution, Complaint
from support.permissions import ComplaintPerms, DefaultPerms
from machines.models import Machine
from data.models import Dataset
from data.schema import fault_codes
from users.models import Account

class IssueList(views.APIView):
    """
    List all issues.
    """
    permission_classes = (DefaultPerms, )

    def get(self, request, format=None):
        issues = Issue.objects.all()
        serializer = serializers.IssueSerializer(issues, many=True)

        return Response(serializer.data)


class ReasonList(views.APIView):
    """
    List all reasons, for a particular issue.
    """
    permission_classes = (DefaultPerms, )

    def get(self, request, issue_id, format=None):
        issue = Issue.objects.get(id=issue_id)
        reasons = Reason.objects.filter(issue=issue)

        serializer = serializers.ReasonSerializer(reasons, many=True)

        return Response(serializer.data)


class SolutionList(views.APIView):
    """
    List all solutions for a particular issue and reason.
    Issue and Reason are taken from query params
    i -> issue.id
    r -> reason.id
    """
    permission_classes = (DefaultPerms, )

    def get(self, request, format=None):
        issue_id = request.query_params.get('i', None)
        reason_id = request.query_params.get('r', None)

        try:
            issue = Issue.objects.get(id=issue_id)
        except:
            return Response(data='Issue not found',
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            reason = Reason.objects.get(id=reason_id)
        except:
            return Response(data='Reason not found.',
                            status=status.HTTP_400_BAD_REQUEST)

        solutions = Solution.objects.filter(issue=issue).filter(reason=reason)

        serializer = serializers.SolutionSerializer(solutions, many=True)

        return Response(serializer.data)


class ComplaintList(views.APIView):
    """
    List all the complaints (newest to oldest), and create new one.
    TODO: return complaints based on the logged in user
    """
    permission_classes = (ComplaintPerms,IsAuthenticated, )
 

    def get(self, request, format=None):
        if request.user.account_type ==7:
            machines = Machine.objects.filter(location = request.user.location)
            complaints = []
            for machine in machines:
                complaints_ = Complaint.objects.filter(machine = machine)
                for complaint in complaints_:
                    complaints.append(complaint)
        elif request.user.account_type ==6:
            c = Account.objects.get(id=request.user.client)
            complaints = Complaint.objects.filter(machine=Machine.objects.get(sold_by=c))
        else:
            complaints = Complaint.objects.all() 
        serializer = serializers.ComplaintSerializer(complaints, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.ComplaintSerializer(
                            data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ComplaintDetail(views.APIView):
    """
    View a single complaint or update it.
    """
    permission_classes = (ComplaintPerms, )

    def get(self, request, pk, format=None):
        complaint = Complaint.objects.get(id=pk)

        serializer = serializers.ComplaintSerializer(complaint)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        complaint = Complaint.objects.get(id=pk)
        print complaint
        serializer = serializers.ComplaintSerializer(
                complaint, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print serializer.data
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ServicePage(views.APIView):
    """
    Get all the data needed for the service page
    TODO: Django ORM query to return fault and its frequency
    """

    permission_classes = (IsAuthenticated, )

    def get(self, request, m_id, format=None):
        machine = Machine.objects.get(m_id=m_id)
        datasets = Dataset.objects.filter(machine=machine)
        issues = Complaint.objects.filter(
                machine=machine).filter(isResolved=True)

        service_data = {
            'total_running_days': 0,
            'faults': {fault_codes[x]: 0 for x in xrange(len(fault_codes))},
            'issues': []
        }

        service_data['total_running_days'] = len(set(
            [x.timestamp.date() for x in datasets]
        ))

        service_data['issues'] = list([
            {
                'service_date': x.serviceDate.isoformat(),
                'issue': x.issue.description,
                'solution': x.solution
            } for x in issues
        ])

        for x in datasets:
            service_data['faults'][fault_codes[int(x.data['due_to'])]] += 1

        return Response(data=service_data)
