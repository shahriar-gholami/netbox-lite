# Generated by Django 4.2.15 on 2024-09-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_remove_devicerole_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicerole',
            name='name',
            field=models.CharField(default='--', max_length=255),
        ),
    ]
