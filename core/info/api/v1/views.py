from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from info.models import *
from .serializers import *
from rest_framework import generics


class DeviceSeriesCreateView(generics.GenericAPIView):
    serializer_class = DeviceSeriesSerializer
    def post(self, request, *args, **kwargs):
        serializer = DeviceSeriesSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            ios = serializer.validated_data.get('ios')
            new_series = DeviceSeries.objects.get_or_create(
                name = name,
                ios = ios
            )            
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

# class SiteCreateView(generics.GenericAPIView):
#     serializer_class = SiteSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = SiteSerializer(data=request.data)
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             city = serializer.validated_data.get('city')
#             new_site = Site.objects.get_or_create(
#                 name = name,
#                 city = city
#             )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SiteUpdateView(generics.GenericAPIView):
#     serializer_class = SiteSerializer
#     def put(self, request, pk, *args, **kwargs):
#         try:
#             site = Site.objects.get(pk=pk)
#         except Site.DoesNotExist:
#             return Response({"error": "Site not found."}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = SiteSerializer(site, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceCreateView(generics.GenericAPIView):
    serializer_class = DeviceSerializer
    def post(self, request, *args, **kwargs):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            ip_address = serializer.validated_data.get('ip_address')
            # site = serializer.validated_data.get('site')
            series = serializer.validated_data.get('series')
            device_model, create = DeviceSeries.objects.get_or_create(
                name = series
            )
            status_field = serializer.validated_data.get('status')
            new_device, create = Device.objects.get_or_create(
                name = name,
                ip_address = ip_address,
                # site = site,
                series = device_model,
                status = status_field,
            )
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
            name = serializer.validated_data.get('name')
            interface = InterfaceType.objects.create(
                name=name,
            )
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
            # Extract validated data for each field
            name = serializer.validated_data.get('name')
            device = serializer.validated_data.get('device')
            interface_device, create = Device.objects.get_or_create(
                name = device
            )
            status_field = serializer.validated_data.get('status', False)
            description = serializer.validated_data.get('description')
            type = serializer.validated_data.get('type')
            interface_type, create = InterfaceType.objects.get_or_create(
                name = type
            )

            interface, create = Interface.objects.get_or_create(
                name=name,
                device=interface_device,
                status=status_field,
                description=description,
                type=interface_type
            )
            
            response_serializer = InterfaceSerializer(interface)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
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
            'id_number', 'name', 'device', 'ip_address'
            id_number = serializer.validated_data.get('id_number')
            name = serializer.validated_data.get('name')
            device = serializer.validated_data.get('device')
            ip_address = serializer.validated_data.get('ip_address')
            description = serializer.validated_data.get('description')
            new_vlan = Vlan.objects.get_or_create(
                id_number = id_number,
                name = name,
                device = device,
                ip_address = ip_address,
                description = description
            )
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
            name = serializer.validated_data.get('name')
            interface, create = IPVersion.objects.get_or_create(
                name=name,
            )
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
            ip_address = serializer.validated_data.get('ip_address')
            if ':' in ip_address:
                version = IPVersion.objects.get(name='ipV6')
            else:
                version = IPVersion.objects.get(name='ipV4')
            description = serializer.validated_data.get('description')
            device = serializer.validated_data.get('device')
            ip_device = Device.objects.get(
                name = device
            )
            interface = serializer.validated_data.get('interface')
            ip_interface = Interface.objects.filter(
                name = interface,
                device = ip_device,
            ).first()
            
            new_ip, create = IPAddress.objects.get_or_create(
                ip_address=ip_address,
                version=version,
                description=description,
                device=ip_device,
                interface = ip_interface
            )
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

class ResetDeviceView(generics.GenericAPIView):

    serializer_class = ResetDeviceSerializer

    def post(self, request):
        serializer = ResetDeviceSerializer(data=request.data)
        if serializer.is_valid():
            device_name = serializer.validated_data.get('device_name')
            device = Device.objects.get(name=device_name)
            interfaces = Interface.objects.filter(device=device)
            interfaces.delete()
            ips = IPAddress.objects.filter(device=device)
            ips.delete()
            vlans = Vlan.objects.filter(device=device)
            vlans.delete()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

























