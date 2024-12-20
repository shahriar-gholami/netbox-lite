# Generated by Django 4.2.15 on 2024-09-29 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_rename_id_number_vlan_vlan_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('next_hop', models.CharField(max_length=255)),
                ('interface', models.CharField(max_length=255)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.device')),
            ],
        ),
    ]
