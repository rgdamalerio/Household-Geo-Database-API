# Generated by Django 4.1 on 2023-11-16 07:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_adntotalreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloodHazardInfo',
            fields=[
                ('municipality_name', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('flood_id', models.CharField(blank=True, max_length=50, null=True)),
                ('barangay_name', models.CharField(blank=True, max_length=255, null=True)),
                ('purok_name', models.CharField(blank=True, max_length=255, null=True)),
                ('household_number', models.TextField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('lat', models.CharField(blank=True, max_length=50, null=True)),
                ('long', models.CharField(blank=True, max_length=50, null=True)),
                ('brgycode', models.CharField(blank=True, max_length=255, null=True)),
                ('families', models.BigIntegerField(blank=True, null=True)),
                ('person', models.BigIntegerField(blank=True, null=True)),
                ('male', models.BigIntegerField(blank=True, null=True)),
                ('female', models.BigIntegerField(blank=True, null=True)),
                ('infant_male', models.BigIntegerField(blank=True, null=True)),
                ('infant_female', models.BigIntegerField(blank=True, null=True)),
                ('elderly_male', models.BigIntegerField(blank=True, null=True)),
                ('elderly_female', models.BigIntegerField(blank=True, null=True)),
                ('drill', models.BigIntegerField(blank=True, null=True)),
                ('philhealth', models.BigIntegerField(blank=True, null=True)),
                ('sss_gsis', models.BigIntegerField(blank=True, null=True)),
                ('illiteracy', models.BigIntegerField(blank=True, null=True)),
                ('ip', models.BigIntegerField(blank=True, null=True)),
                ('pwd', models.BigIntegerField(blank=True, null=True)),
                ('malnurished', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'flood_hazard_info',
                'managed': False,
            },
        ),
    ]