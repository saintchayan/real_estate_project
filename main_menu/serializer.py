from rest_framework import serializers
from .models import RentSale


class RentSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentSale
        fields = "__all__"

    # type = serializers.CharField(default='R')
    # city = serializers.CharField(default='ANTAL')
    # district = serializers.CharField(default='KEPE')
    # address = serializers.CharField()
    # owner = serializers.CharField()
    # phone_number = serializers.IntegerField()
    # price_in_lira = serializers.IntegerField()
    # created_data = serializers.DateField(read_only=True)
    # updated_time = serializers.DateField(read_only=True)
    # description = serializers.CharField()
    #
    # def create(self, validated_data):
    #     return RentSale.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.type = validated_data.get("type", instance.type)
    #     instance.city = validated_data.get("city", instance.city)
    #     instance.district = validated_data.get("district", instance.district)
    #     instance.address = validated_data.get("address", instance.address)
    #     instance.owner = validated_data.get("owner", instance.owner)
    #     instance.phone_number = validated_data.get("phone_number", instance.phone_number)
    #     instance.price_in_lira = validated_data.get("price_in_lira", instance.price_in_lira)
    #     instance.updated_time = validated_data.get("updated_time", instance.updated_time)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.save()
    #     return instance