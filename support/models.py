from django.db import models

from users.models import Account
from machines.models import Machine


class Issue(models.Model):
    description = models.TextField()

    def __unicode__(self):
        return self.description


class Reason(models.Model):
    issue = models.ForeignKey(Issue)
    description = models.TextField()

    def __unicode__(self):
        return self.description


class Solution(models.Model):
    issue = models.ForeignKey(Issue)
    reason = models.ForeignKey(Reason)
    description = models.TextField()

    def __unicode__(self):
        return self.description


class Complaint(models.Model):
    machine = models.ForeignKey(Machine)
    user = models.ForeignKey(Account)
    issue = models.ForeignKey(Issue)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    isResolved = models.BooleanField(default=False)
    serviceDate = models.DateField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.machine.m_id, self.description)



class Fault(models.Model):
    f_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.description

class FaultReason(models.Model):
    fault = models.ForeignKey(Fault)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.description