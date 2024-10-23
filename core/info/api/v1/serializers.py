from rest_framework import serializers
from info.models import *


class DeviceSeriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

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
    vlan_id = serializers.IntegerField()
    vlan_name = serializers.CharField(max_length=255)
    device_name = serializers.CharField(max_length=255)

class ResetDeviceSerializer(serializers.Serializer):
    device_name = serializers.CharField(max_length=255)

class RouteSerializer(serializers.Serializer):
    destination = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    next_hop = serializers.CharField(max_length=255)
    interface = serializers.CharField(max_length=255)
    device_name = serializers.CharField(max_length=255)

class VrfRouteSerializer(serializers.Serializer):
    destination = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    next_hop = serializers.CharField(max_length=255)
    interface = serializers.CharField(max_length=255)
    device_name = serializers.CharField(max_length=255)
    vrf_name = serializers.CharField(max_length=255)

class MikrotikInterfaceSerializer(serializers.Serializer):
    device_name = serializers.CharField()
    name = serializers.CharField()
    flag = serializers.CharField()
    type = serializers.CharField()

class MikrotikIPRouteSerializer(serializers.Serializer):
    device_name = serializers.CharField()
    destination = serializers.CharField()
    gateway = serializers.CharField()
    distance = serializers.CharField()
    flag = serializers.CharField()

class MikrotikIPAddressSerializer(serializers.Serializer):
    device_name = serializers.CharField()
    address = serializers.CharField()
    network = serializers.CharField()
    flag = serializers.CharField()
    interface = serializers.CharField()









