from django.db.models import fields
from rest_framework import serializers
from .models import owner,renter,flat_details, earning, remain
from barivara_app import models


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = owner
        fields = '__all__'


class RenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = renter
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        renter_id = instance.renter_id
        representation['flat_number'] = flat_details.objects.get(flat_renter_id = renter_id).flat_number
        #print(renter_id)
        return representation

class FlatDetailsSerializer(serializers.ModelSerializer):
    flat_renter_name = serializers.StringRelatedField(many=False)
    class Meta:
        model = flat_details
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(type(instance.flat_renter_id))
        representation['flat_renter_name'] = str(instance.flat_renter_id)
        return representation


class EarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = earning
        fields = '__all__'

class RemainSerializer(serializers.ModelSerializer):
    class Meta:
        model = remain
        fields = '__all__'
