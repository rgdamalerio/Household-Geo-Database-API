# Generated by Django 4.1 on 2023-04-03 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("household", "0031_alter_households_location"),
    ]

    operations = [
        migrations.DeleteModel(
            name="MajorRivers",
        ),
    ]