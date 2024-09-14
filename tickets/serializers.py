from rest_framework import serializers
from .models import TicketType
from .models import Purchase
from events.serializers import EventSerializer
from users.serializers import CustomUserSerializer

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ['event', 'name', 'price', 'available_quantity']


class PurchaseSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    ticket_type = TicketTypeSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = ['user', 'ticket_type', 'quantity', 'purchase_date']
