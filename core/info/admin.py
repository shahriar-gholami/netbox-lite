from django.contrib import admin
from .models import IoS, DeviceSeries, DeviceRole, Site, Device, InterfaceType, Interface, Vlan, IPVersion, IPAddress

@admin.register(IoS)
class IoSAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(DeviceSeries)
class DeviceSeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'ios')
    list_filter = ('company', 'ios')
    search_fields = ('name', 'company')
    ordering = ('name',)

@admin.register(DeviceRole)
class DeviceRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city')
    ordering = ('name',)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'role', 'site', 'ios', 'series', 'status')
    list_filter = ('role', 'site', 'ios', 'series', 'status')
    search_fields = ('name', 'ip_address')
    ordering = ('name',)
    list_editable = ('status',)

@admin.register(InterfaceType)
class InterfaceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Interface)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device', 'status', 'type', 'ip_address')
    list_filter = ('device', 'status', 'type')
    search_fields = ('name', 'device__name')
    ordering = ('name',)
    list_editable = ('status',)

@admin.register(Vlan)
class VlanAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'name', 'device', 'ip_address')
    list_filter = ('device',)
    search_fields = ('name', 'id_number', 'device__name')
    ordering = ('id_number',)

@admin.register(IPVersion)
class IPVersionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'version', 'status', 'device')
    list_filter = ('version', 'status', 'device')
    search_fields = ('ip_address', 'device__name')
    ordering = ('ip_address',)
    list_editable = ('status',)

from django.contrib import admin

admin.site.site_header = "NetBox"
admin.site.site_title = "NetBox"
admin.site.index_title = "NetBox"

