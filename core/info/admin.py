from django.contrib import admin
from .models import DeviceSeries, Device, InterfaceType, Interface, Vlan, IPVersion, IPAddress
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
    list_display = ('name', 'ip_address', 'series','get_interface_count')
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
    list_editable = ('status',)

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


admin.site.site_header = "NetBox"
admin.site.site_title = "NetBox"
admin.site.index_title = "NetBox"

