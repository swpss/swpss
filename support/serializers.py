from django.utils import timezone

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from support.models import Issue, Solution, Reason, Complaint
from users.serializers import AccountMinSerializer
from users.models import Account
from machines.serializers import MachineSerializer
from machines.models import Machine


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        queryset = Issue.objects.all()


class ReasonSerializer(ModelSerializer):
    class Meta:
        model = Reason
        queryset = Reason.objects.all()


class SolutionSerializer(ModelSerializer):
    class Meta:
        model = Solution
        queryset = Solution.objects.all()


class ComplaintSerializer(ModelSerializer):
    user = AccountMinSerializer(read_only=True)
    machine = MachineSerializer(read_only=True)
    issue = IssueSerializer(read_only=True)

    m_id = serializers.IntegerField(write_only=True)
    issue_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        request = self.context.get('request', None)
        
        user = request.user
        machine = Machine.objects.get(bought_by=Account.objects.get(phone_number = validated_data['m_id']))
        issue = Issue.objects.get(id=validated_data['issue_id'])

        try:
            description = validated_data['description']
        except KeyError:
            description = None

        complaint = Complaint.objects.create(
                machine=machine,
                issue=issue,
                user=user,
                description=description
        )
        complaint.save()

        return complaint

    def update(self, instance, validated_data):
        instance.isResolved = validated_data['isResolved']
        instance.serviceDate = timezone.now().date()
        instance.solution = validated_data['solution']

        instance.save()

        return instance

    class Meta:
        model = Complaint
        queryset = Complaint.objects.all()
