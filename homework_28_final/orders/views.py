from typing import Any
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Orders.

    - Allows creation of orders by authenticated customers or guests (with guest_email).
    - Restricts viewing orders only to the authenticated customer's own orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer: OrderSerializer) -> None:
        """
        Handle order creation.

        Saves order with:
        - customer set if authenticated user with customer_profile.
        - status set to "pending" for all created orders.

        Raises ValidationError if both or neither customer and guest_email are provided.

        Args:
            serializer (OrderSerializer): The serializer instance with validated data.

        Raises:
            ValidationError: If validation on customer/guest_email presence fails.
        """
        user = self.request.user
        data = serializer.validated_data
        guest_email = data.get("guest_email")

        if user.is_authenticated and hasattr(user, "customer_profile"):
            if guest_email:
                raise ValidationError("Only one of 'customer' or 'guest_email' must be provided.")
            serializer.save(customer=user.customer_profile, status="pending")
        elif guest_email:
            serializer.save(status="pending")  # guest order, no customer
        else:
            raise ValidationError("Either authenticated user with profile or guest_email is required.")

    def get_queryset(self) -> Any:
        """
        Retrieve orders for the authenticated customer only.

        Returns empty queryset for unauthenticated or guest users.

        Returns:
            QuerySet[Order]: Orders belonging to the authenticated customer or empty.
        """
        user = self.request.user
        if user.is_authenticated and hasattr(user, 'customer_profile'):
            return Order.objects.filter(customer=user.customer_profile)
        return Order.objects.none()
