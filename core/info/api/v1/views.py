from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from info.models import *
from .serializers import *
from rest_framework import generics


class IoSCreateView(generics.GenericAPIView):
    serializer_class = IoSSerializer
    def post(self, request, *args, **kwargs):
        serializer = IoSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IoSUpdateView(generics.GenericAPIView):
    serializer_class = IoSSerializer
    def put(self, request, pk, *args, **kwargs):
        try:
            ios = IoS.objects.get(pk=pk)
        except IoS.DoesNotExist:
            return Response({"error": "IoS not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = IoSSerializer(ios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceSeriesCreateView(generics.GenericAPIView):
    serializer_class = DeviceSeriesSerializer
    def post(self, request, *args, **kwargs):
        serializer = DeviceSeriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceSeriesUpdateView(generics.GenericAPIView):
    serializer_class = DeviceSeriesSerializer
    def put(self, request, pk, *args, **kwargs):
        try:
            device_series = DeviceSeries.objects.get(pk=pk)
        except DeviceSeries.DoesNotExist:
            return Response({"error": "DeviceSeries not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DeviceSeriesSerializer(device_series, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceRoleCreateView(generics.GenericAPIView):
    serializer_class = DeviceRoleSerializer
    def post(self, request, *args, **kwargs):
        serializer = DeviceRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceRoleUpdateView(generics.GenericAPIView):
    serializer_class = DeviceRoleSerializer
    def put(self, request, pk, *args, **kwargs):
        try:
            device_role = DeviceRole.objects.get(pk=pk)
        except DeviceRole.DoesNotExist:
            return Response({"error": "DeviceRole not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DeviceRoleSerializer(device_role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SiteCreateView(generics.GenericAPIView):
    serializer_class = SiteSerializer
    def post(self, request, *args, **kwargs):
        serializer = SiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SiteUpdateView(generics.GenericAPIView):
    serializer_class = SiteSerializer
    def put(self, request, pk, *args, **kwargs):
        try:
            site = Site.objects.get(pk=pk)
        except Site.DoesNotExist:
            return Response({"error": "Site not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SiteSerializer(site, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceCreateView(generics.GenericAPIView):
    serializer_class = DeviceSerializer
    def post(self, request, *args, **kwargs):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceUpdateView(generics.GenericAPIView):
    serializer_class = DeviceSerializer
    def put(self, request, pk, *args, **kwargs):
        try:
            device = Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            return Response({"error": "Device not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterfaceTypeCreateView(generics.GenericAPIView):
    serializer_class = InterfaceTypeSerializer
    def post(self, request, *args, **kwargs):
        serializer = InterfaceTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterfaceTypeUpdateView(generics.GenericAPIView):
    serializer_class = InterfaceTypeSerializer
    def put(self, request, pk, *args, **kwargs):
        try:
            interface_type = InterfaceType.objects.get(pk=pk)
        except InterfaceType.DoesNotExist:
            return Response({"error": "InterfaceType not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = InterfaceTypeSerializer(interface_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterfaceCreateView(generics.GenericAPIView):
    serializer_class = InterfaceSerializer
    def post(self, request, *args, **kwargs):
        serializer = InterfaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterfaceUpdateView(generics.GenericAPIView):
    serializer_class = InterfaceSerializer
    def put(self, request, pk, *args, **kwargs):
        try:
            interface = Interface.objects.get(pk=pk)
        except Interface.DoesNotExist:
            return Response({"error": "Interface not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = InterfaceSerializer(interface, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VlanCreateView(generics.GenericAPIView):
    serializer_class = VlanSerializer
    def post(self, request, *args, **kwargs):
        serializer = VlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VlanUpdateView(generics.GenericAPIView):
    serializer_class = VlanSerializer
    def put(self, request, pk, *args, **kwargs):
        try:
            vlan = Vlan.objects.get(pk=pk)
        except Vlan.DoesNotExist:
            return Response({"error": "Vlan not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VlanSerializer(vlan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IPVersionCreateView(generics.GenericAPIView):
    serializer_class = IPVersionSerializer
    def post(self, request, *args, **kwargs):
        serializer = IPVersionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IPVersionUpdateView(generics.GenericAPIView):
    serializer_class = IPVersionSerializer
    def put(self, request, pk, *args, **kwargs):
        try:
            ip_version = IPVersion.objects.get(pk=pk)
        except IPVersion.DoesNotExist:
            return Response({"error": "IPVersion not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = IPVersionSerializer(ip_version, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IPAddressCreateView(generics.GenericAPIView):
    serializer_class = IPAddressSerializer
    def post(self, request, *args, **kwargs):
        serializer = IPAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IPAddressUpdateView(generics.GenericAPIView):
    serializer_class = IPAddressSerializer
    def put(self, request, pk, *args, **kwargs):
        try:
            ip_address = IPAddress.objects.get(pk=pk)
        except IPAddress.DoesNotExist:
            return Response({"error": "IPAddress not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = IPAddressSerializer(ip_address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)