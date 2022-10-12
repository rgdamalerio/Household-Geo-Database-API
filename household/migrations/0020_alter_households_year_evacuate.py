# Generated by Django 4.1 on 2022-10-11 08:12

import django.core.validators
from django.db import migrations, models
import household.models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0019_alter_households_year_construct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='households',
            name='year_evacuate',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1940), household.models.max_value_current_year]),
        ),
    ]