# Generated by Django 2.2.10 on 2020-12-30 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0091_merge_20201228_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='federal_itc_pct',
        ),
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='federal_rebate_us_dollars_per_kw',
        ),
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='state_ibi_max_us_dollars',
        ),
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='state_ibi_pct',
        ),
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='state_rebate_max_us_dollars',
        ),
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='state_rebate_us_dollars_per_kw',
        ),
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='utility_ibi_max_us_dollars',
        ),
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='utility_ibi_pct',
        ),
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='utility_rebate_max_us_dollars',
        ),
        migrations.RemoveField(
            model_name='absorptionchillermodel',
            name='utility_rebate_us_dollars_per_kw',
        ),
    ]
