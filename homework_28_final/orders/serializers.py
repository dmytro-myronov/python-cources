from typing import Any, Dict
from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.

    Validates that either an authenticated customer or a guest email is provided,
    but not both simultaneously.
    """

    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'guest_email',
            'car',
            'start_time',
            'end_time',
            'price',
            'status',
        ]
        read_only_fields = ['customer', 'status']

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate that either a registered customer or guest email is provided,
        but not both.

        Args:
            data (Dict[str, Any]): Incoming data to validate.

        Returns:
            Dict[str, Any]: Validated data.

        Raises:
            serializers.ValidationError: If validation rules are violated.
        """
        user = self.context['request'].user
        guest_email = data.get('guest_email')

        if user.is_authenticated and hasattr(user, 'customer_profile'):
            if guest_email:
                raise serializers.ValidationError(
                    "Only one of 'customer' or 'guest_email' must be provided."
                )
        elif not guest_email:
            raise serializers.ValidationError(
                "Unauthenticated users must provide a guest email."
            )

        return data
