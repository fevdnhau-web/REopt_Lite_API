# Generated by Django 2.2.10 on 2020-07-07 02:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0065_auto_20200616_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='electrictariffmodel',
            name='emissions_factor_series_lb_CO2_per_kwh',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='electrictariffmodel',
            name='year_one_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electrictariffmodel',
            name='year_one_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='emissions_factor_lb_CO2_per_gal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='year_one_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generatormodel',
            name='year_one_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_emissions_bau_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_emissions_lb_C02',
            field=models.FloatField(blank=True, null=True),
        ),
    ]