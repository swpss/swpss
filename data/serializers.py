from rest_framework import serializers
from rest_framework_hstore import serializers as h_serializers

from data.models import Dataset


class DatasetSerializer(h_serializers.HStoreSerializer):
    class Meta:
        model = Dataset


class LPDDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    et = serializers.DateTimeField()
    st = serializers.DateTimeField()
    avg_lpm = serializers.FloatField()
    t_duration = serializers.IntegerField()
    lpd = serializers.FloatField()


class MultipleLPDDataSerializer(serializers.Serializer):
    uid = serializers.IntegerField()
    date = serializers.DateField()
    et = serializers.DateTimeField()
    st = serializers.DateTimeField()
    avg_lpm = serializers.FloatField()
    t_duration = serializers.IntegerField()
    lpd = serializers.FloatField()


class PowDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    et = serializers.DateTimeField()
    st = serializers.DateTimeField()
    avg_pow = serializers.FloatField()
    t_duration = serializers.IntegerField()
    pow_h = serializers.FloatField()
