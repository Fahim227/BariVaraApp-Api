from django.db.models import fields
from rest_framework import serializers
from .models import owner,renter,flat_details


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = owner
        fields = '__all__'


class RenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = renter
        fields = '__all__'

class FlatDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = flat_details
        fields = '__all__'