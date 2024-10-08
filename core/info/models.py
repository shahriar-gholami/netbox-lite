from django.db import models


class DeviceSeries(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
    # site = models.ForeignKey(Site, on_delete=models.CASCADE)
    series = models.ForeignKey(DeviceSeries, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def get_device_interfaces(self):
        device_interfaces = Interface.objects.filter(
            device = self
        )
        return device_interfaces

    def __str__(self):
        return self.name

class InterfaceType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Interface(models.Model):
    name = models.CharField(max_length=255)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=1000)
    type = models.ForeignKey(InterfaceType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.device.name}'

class Vlan(models.Model):
    vlan_id = models.IntegerField()
    vlan_name = models.CharField(max_length=255)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vlan_name} - {self.device.name}'

class IPVersion(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class IPAddress(models.Model):
    ip_address = models.CharField(max_length=255)
    version = models.ForeignKey(IPVersion, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    interface = models.ForeignKey(Interface, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.ip_address

class Route(models.Model):
    destination = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    next_hop = models.CharField(max_length=255)
    interface = models.CharField(max_length=255)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)





