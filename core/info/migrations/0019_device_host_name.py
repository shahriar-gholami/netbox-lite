# Generated by Django 4.2.15 on 2024-11-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0018_mikrotikipaddress_interface'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='host_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]