# Generated by Django 4.1 on 2022-08-11 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("library", "0032_alter_buildingstatus_options_and_more"),
        ("household", "0010_availprograms"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hhlivelihoods",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("market_value", models.IntegerField()),
                ("products", models.CharField(max_length=255)),
                ("with_insurance", models.BooleanField()),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "controlnumber",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="household.households",
                        verbose_name="Housedhold belong",
                    ),
                ),
                (
                    "livelihood",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.livelihoods",
                    ),
                ),
                (
                    "livelihood_tenural_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.livelihoodtenuralstatus",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        default=1,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Livelihoods",
            },
        ),
    ]