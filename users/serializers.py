import re

from rest_framework import serializers
from users.models import Account


class AccountSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=False)
    last_name = serializers.CharField(
            required=False,
            max_length=40,
            allow_blank=True
    )

    def validate(self, data):
        phone_number_pattern = r'\d{10}'
        match = re.match(phone_number_pattern, data['phone_number'])

        if match is None or match.group() != data['phone_number']:
            raise serializers.ValidationError("Invalid phone number.")
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError("Passwords don't match.")

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        if validated_data['account_type'] == 6:
            client = validated_data.pop('client')
        else:
            client = 0
        account = self.Meta.model(**validated_data)
        account.set_password(password)
        account.client = client
        account.save()

        return account

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name',
                instance.first_name)
        instance.last_name = validated_data.get('last_name',
                instance.last_name)
        instance.address = validated_data.get('address',
                instance.address)
        instance.phone_number = validated_data.get('phone_number',
                instance.phone_number)
        instance.has_smart_phone = validated_data.get('has_smart_phone',
                instance.has_smart_phone)
        instance.account_type = validated_data.get('account_type',
                instance.account_type)
        instance.set_password(
                validated_data.get('password', instance.password)
            )
        instance.save()

        return instance

    class Meta:
        model = Account
        fields = (
                'id',
                'email',
                'first_name',
                'last_name',
                'phone_number',
                'address',
                'location',
                'account_type',
                'has_smart_phone',
                'password',
                'confirm_password',
                'created_at',
                'modified_at',
                'client'
        )
        read_only_fields = (
                'created_at',
                'modified_at'
        )
        write_only_fields = (
                'password',
        )


class AccountMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
                'id',
                'first_name',
                'phone_number'
        )
