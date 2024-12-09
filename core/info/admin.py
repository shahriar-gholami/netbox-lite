from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.urls import reverse



@admin.register(DeviceSeries)
class DeviceSeriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class InterfaceInline(admin.TabularInline):
    model = Interface
    fields = ('name_link', 'status', 'type')
    readonly_fields = ('name_link',)
    can_delete = False  # حذف قابلیت حذف اینترفیس
    extra = 0 

    def name_link(self, obj):
        link = reverse('admin:info_interface_change', args=[obj.pk])
        return format_html('<a href="{}">{}</a>', link, obj.name)
    name_link.short_description = 'Name'

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name','host_name' ,'ip_address', 'series','get_interface_count')
    inlines = [InterfaceInline]
    ordering = ('name',)

    def get_interface_count(self, obj):
        return obj.get_device_interfaces().count()
    
    get_interface_count.short_description = 'Number of Interfaces'

admin.site.register(Device, DeviceAdmin)

@admin.register(InterfaceType)
class InterfaceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Interface)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device', 'status', 'description')
    list_filter = ('device', 'status', 'type')
    search_fields = ('name', 'device__name')
    ordering = ('name',)
    

@admin.register(Vlan)
class VlanAdmin(admin.ModelAdmin):
    list_display = ('vlan_id', 'vlan_name', 'device', )
    list_filter = ('device',)
    search_fields = ('vlan_name', 'vlan_id', 'device__name')
    ordering = ('vlan_id',)

@admin.register(IPVersion)
class IPVersionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'version', 'interface', 'device')
    list_filter = ('version', 'device')
    search_fields = ('ip_address',)
    ordering = ('ip_address',)

class RouteAdmin(admin.ModelAdmin):
    list_display = ('destination', 'type', 'next_hop', 'interface', 'device')
    search_fields = ('destination', 'next_hop', 'interface', 'device__name')  # جستجو در فیلدهای دلخواه
    list_filter = ('type', 'device')  # اضافه کردن فیلتر بر اساس نوع روت و دستگاه

# Register the Route model with custom admin
admin.site.register(Route, RouteAdmin)


class VrfRouteAdmin(admin.ModelAdmin):
    list_display = ('destination', 'type', 'next_hop', 'interface', 'device', 'vrf_name')  # نمایش فیلدها در لیست اصلی
    search_fields = ('destination', 'vrf_name', 'device__name')  # قابلیت جستجو بر اساس مقصد و VRF و نام دستگاه
    list_filter = ('device', 'type', 'vrf_name')  # فیلتر بر اساس نوع و VRF و دستگاه
    ordering = ('vrf_name', 'destination')  # مرتب‌سازی پیش‌فرض
 
admin.site.register(VrfRoute, VrfRouteAdmin)

@admin.register(MikrotikDevice)
class MikrotikDeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name','host_name' ,'ip_address', 'get_interface_count' )
    search_fields = ('ip_address', 'device_name')
    list_filter = ('ip_address', 'device_name')

    def get_interface_count(self, obj):
        return obj.get_device_interfaces().count()
    
    get_interface_count.short_description = 'Number of Interfaces'

# MikrotikInterfaceAdmin برای نمایش اطلاعات اینترفیس‌ها
@admin.register(MikrotikInterface)
class MikrotikInterfaceAdmin(admin.ModelAdmin):
    list_display = ('name','device',  'flag', 'type')
    search_fields = ('device__device_name', 'name', 'flag', 'type')
    list_filter = ('device', 'type')

# MikrotikIPRouteAdmin برای نمایش اطلاعات مسیریابی‌ها
@admin.register(MikrotikIPRoute)
class MikrotikIPRouteAdmin(admin.ModelAdmin):
    list_display = ('destination', 'device' , 'gateway', 'distance', 'flag')
    search_fields = ('device__device_name', 'destination', 'gateway', 'distance', 'flag')
    list_filter = ('device', 'distance')

# MikrotikIPAddressAdmin برای نمایش اطلاعات آدرس‌های IP
@admin.register(MikrotikIPAddress)
class MikrotikIPAddressAdmin(admin.ModelAdmin):
    list_display = ('address','device',  'network', 'interface','flag')
    search_fields = ('device__device_name', 'address', 'network', 'flag')
    list_filter = ('device', 'network',)


admin.site.site_header = "NetBox"
admin.site.site_title = "NetBox"
admin.site.index_title = "NetBox"

