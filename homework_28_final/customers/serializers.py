import logging
from typing import Any, Dict

from rest_framework import serializers
from .models import Customer
from .tasks import send_registration_email, send_promo_email


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model.
    Handles creation of a customer and triggers asynchronous email tasks:
    - Sends a registration email immediately after creation.
    - Schedules a promotional email to be sent after 10 minutes.
    """

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data: Dict[str, Any]) -> Customer:
        """
        Create a new Customer instance and trigger email-related tasks.

        Args:
            validated_data (dict): Validated data for creating the customer.

        Returns:
            Customer: The newly created Customer instance.
        """
        customer = Customer.objects.create(**validated_data)

        try:
            send_registration_email.delay(customer.email)
        except Exception as e:
            logging.error(f"Error sending registration email: {e}")

        try:
            send_promo_email.apply_async(args=[customer.id], countdown=600)
        except Exception as e:
            logging.error(f"Error scheduling promo email: {e}")

        return customer
