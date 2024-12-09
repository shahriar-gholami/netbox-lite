from django.urls import path
from .views import *

urlpatterns = [
    path('device-series/create/', DeviceSeriesCreateView.as_view(), name='device_series_create'),
    path('device/create/', DeviceCreateView.as_view(), name='device_create'),
    path('device/update/<int:pk>/', DeviceUpdateView.as_view(), name='device_update'),
    path('interface-type/create/', InterfaceTypeCreateView.as_view(), name='interface_type_create'),
    path('interface-type/update/<int:pk>/', InterfaceTypeUpdateView.as_view(), name='interface_type_update'),
    path('interface/create/', InterfaceCreateView.as_view(), name='interface_create'),
    path('interface/update/<int:pk>/', InterfaceUpdateView.as_view(), name='interface_update'),
    path('vlan/create/', VlanCreateView.as_view(), name='vlan_create'),
    path('vlan/update/<int:pk>/', VlanUpdateView.as_view(), name='vlan_update'),
    path('ip-version/create/', IPVersionCreateView.as_view(), name='ip_version_create'),
    path('ip-version/update/<int:pk>/', IPVersionUpdateView.as_view(), name='ip_version_update'),
    path('ip-address/create/', IPAddressCreateView.as_view(), name='ip_address_create'),
    path('route/create/', RouteCreateView.as_view(), name='route_create'),
    path('vrf-route/create/', VrfRouteCreateView.as_view(), name='vrf_route_create'),
    path('ip-address/update/<int:pk>/', IPAddressUpdateView.as_view(), name='ip_address_update'),
    path('mikrotik-interface/create/', MikrotikInterfaceCreateView.as_view(), name='mikrotik_intrface_create'),
    path('mikrotik-ip/create/', MikrotikIPAddressCreateView.as_view(), name='mikrotik_ip_create'),
    path('mikrotik-ip-route/create/', MikrotikIPRouteCreateView.as_view(), name='mikrotik_ip_route_create'),
    path('reset-device/', ResetDeviceView.as_view(), name='reset_device'),
    path('reset-mikrotik-device/', ResetMikrotikDeviceView.as_view(), name='reset_mikrotik_device'),
]
