from rest_framework import serializers
from info.models import *


class DeviceSeriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

# class SiteSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     city = serializers.CharField(max_length=255)

class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    ip_address = serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)
    # site = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all())
    series = serializers.CharField(max_length=255)
    status = serializers.BooleanField(default=False)

class InterfaceTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

class InterfaceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    device = serializers.CharField(max_length=255)
    status = serializers.BooleanField(default=False)
    description = serializers.CharField(max_length=1000)
    ip_address = serializers.PrimaryKeyRelatedField(queryset=IPAddress.objects.all(), required=False, allow_null=True)
    type = serializers.CharField(max_length=255)

class IPVersionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

class IPAddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ip_address = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000, required=False, allow_null=True, allow_blank=True)
    device = serializers.CharField(max_length=255)
    interface = serializers.CharField(max_length=255)

class VlanSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    id_number = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    device = serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())
    ip_address = serializers.PrimaryKeyRelatedField(queryset=IPAddress.objects.all(), required=False, allow_null=True)
    description = serializers.CharField(max_length=1000, required=False, allow_null=True, allow_blank=True)

class ResetDeviceSerializer(serializers.Serializer):
    device_name = serializers.CharField(max_length=255)




