# Generated by Django 2.2.10 on 2020-12-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0086_annual_loads_to_float'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadprofileboilerfuelmodel',
            name='annual_mmbtu',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loadprofilechillerthermalmodel',
            name='annual_tonhour',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loadprofilemodel',
            name='annual_kwh',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
