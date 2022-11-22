from rest_framework import serializers
from .models import RentSale


class RentSaleSerializer(serializers.Serializer):
    type = serializers.CharField(default='R')
    city = serializers.CharField(default='ANTAL')
    district = serializers.CharField(default='KEPE')
    address = serializers.CharField()
    owner = serializers.CharField()
    phone_number = serializers.IntegerField()
    price_in_lira = serializers.IntegerField()
    created_data = serializers.DateField(read_only=True)
    updated_time = serializers.DateField(read_only=True)
    description = serializers.CharField()