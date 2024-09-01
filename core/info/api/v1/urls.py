from django.urls import path
from .views import (
    SiteCreateView, SiteUpdateView,
    DeviceCreateView, DeviceUpdateView,
    InterfaceTypeCreateView, InterfaceTypeUpdateView,
    InterfaceCreateView, InterfaceUpdateView,
    VlanCreateView, VlanUpdateView,
    IPVersionCreateView, IPVersionUpdateView,
    IPAddressCreateView, IPAddressUpdateView,
)

urlpatterns = [
    path('site/create/', SiteCreateView.as_view(), name='site-create'),
    path('site/update/<int:pk>/', SiteUpdateView.as_view(), name='site-update'),
    path('device/create/', DeviceCreateView.as_view(), name='device-create'),
    path('device/update/<int:pk>/', DeviceUpdateView.as_view(), name='device-update'),
    path('interface-type/create/', InterfaceTypeCreateView.as_view(), name='interface-type-create'),
    path('interface-type/update/<int:pk>/', InterfaceTypeUpdateView.as_view(), name='interface-type-update'),
    path('interface/create/', InterfaceCreateView.as_view(), name='interface-create'),
    path('interface/update/<int:pk>/', InterfaceUpdateView.as_view(), name='interface-update'),
    path('vlan/create/', VlanCreateView.as_view(), name='vlan-create'),
    path('vlan/update/<int:pk>/', VlanUpdateView.as_view(), name='vlan-update'),
    path('ip-version/create/', IPVersionCreateView.as_view(), name='ip-version-create'),
    path('ip-version/update/<int:pk>/', IPVersionUpdateView.as_view(), name='ip-version-update'),
    path('ip-address/create/', IPAddressCreateView.as_view(), name='ip-address-create'),
    path('ip-address/update/<int:pk>/', IPAddressUpdateView.as_view(), name='ip-address-update'),
]
