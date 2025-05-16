import logging

from rest_framework import serializers
from .models import Customer
from .tasks import send_registration_email


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    def create(self, validated_data):
        customer = Customer.objects.create(**validated_data)
        try:
            send_registration_email.delay(customer.email)
        except Exception as e:
            logging.error(e)

        return customer