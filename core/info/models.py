from django.db import models

class IoS(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DeviceSeries(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    ios = models.ForeignKey(IoS, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DeviceRole(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, default='-')

    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.city}'

class Device(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey(DeviceRole, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    ios = models.ForeignKey(IoS, on_delete=models.CASCADE)
    series = models.ForeignKey(DeviceSeries, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

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
    ip_address = models.ForeignKey('IPAddress', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(InterfaceType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.device.name}'

class Vlan(models.Model):
    id_number = models.IntegerField()
    name = models.CharField(max_length=255)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    ip_address = models.ForeignKey('IPAddress', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.device.name}'

class IPVersion(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class IPAddress(models.Model):
    ip_address = models.CharField(max_length=255)
    version = models.ForeignKey(IPVersion, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip_address




