from django.db import models
from django_hstore import hstore

from machines.models import Machine

class Dataset(models.Model):
    machine = models.ForeignKey(Machine)

    serial_no = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = hstore.SerializedDictionaryField()

    objects = hstore.HStoreManager()

    def __unicode__(self):
        return self.serial_no
