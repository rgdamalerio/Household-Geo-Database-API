# Generated by Django 4.1 on 2023-03-24 01:15

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("household", "0023_merge_20230324_0907"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="households",
            name="purok_id",
        ),
        migrations.AlterField(
            model_name="households",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(
                geography=True, srid=4326
            ),
        ),
    ]