# Generated by Django 4.2.15 on 2024-09-14 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_remove_interface_ip_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceseries',
            name='company',
        ),
    ]
