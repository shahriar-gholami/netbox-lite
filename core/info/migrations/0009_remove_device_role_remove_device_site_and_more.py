# Generated by Django 4.2.15 on 2024-09-14 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_remove_deviceseries_ios_delete_ios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='role',
        ),
        migrations.RemoveField(
            model_name='device',
            name='site',
        ),
        migrations.DeleteModel(
            name='DeviceRole',
        ),
        migrations.DeleteModel(
            name='Site',
        ),
    ]
