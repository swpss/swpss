import re

from rest_framework import serializers
from machines.models import MachineDetail, Machine

from users.models import Account
from users.serializers import AccountMinSerializer


class MachineDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineDetail
        queryset = MachineDetail.objects.all()


class MachineDetailMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineDetail
        fields = (
                'id',
                'con_model_no',
                'p_make',
        )


class MachineSerializer(serializers.ModelSerializer):
    """
    * farmer_phone_number -> used while registering new machines with farmer's email.
    * machine_model -> used while registering new machines with model's id.
    * read_only fields are used to include the id and other details
      for info, id can then be used to query their details
    """
    farmer_phone_number = serializers.CharField(max_length=10, write_only=True)
    machine_model = serializers.IntegerField(write_only=True)

    bought_by = AccountMinSerializer(read_only=True)
    sold_by = AccountMinSerializer(read_only=True)
    model = MachineDetailMinSerializer(read_only=True)

    def validate(self, data):
        mid_pattern = r'\w+'
        match = re.match(mid_pattern, data['m_id'])

        try:
            data['model'] = MachineDetail.objects.get(id=data['machine_model'])
            data.pop('machine_model')
        except:
            raise serializers.ValidationError(
                    "No model with given id.")

        try:
            data['bought_by'] = Account.objects.get(phone_number=data['farmer_phone_number'])
            data.pop('farmer_phone_number')
        except:
            raise serializers.ValidationError(
                    "No farmer with that email ID.")

        data['sold_by'] = self.context['request'].user

        return data

    class Meta:
        model = Machine