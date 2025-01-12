# Generated by Django 4.1 on 2023-05-09 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0035_familyrelationship"),
        ("household", "0027_families_familydetails"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="demographies",
            options={"verbose_name_plural": "Individuals"},
        ),
        migrations.AlterModelOptions(
            name="familydetails",
            options={
                "verbose_name": "Family Member",
                "verbose_name_plural": "Demographies",
            },
        ),
        migrations.AlterField(
            model_name="availprograms",
            name="controlnumber",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="household.households",
                verbose_name="Beneficiary",
            ),
        ),
        migrations.AlterField(
            model_name="availprograms",
            name="number_of_beneficiaries",
            field=models.SmallIntegerField(verbose_name="No. of beneficiaries"),
        ),
        migrations.AlterField(
            model_name="families",
            name="family_head",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="household.demographies",
                verbose_name="Head of family",
            ),
        ),
        migrations.AlterField(
            model_name="families",
            name="remarks",
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="families",
            name="status",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="library.familystatus",
                verbose_name="Family status",
            ),
        ),
        migrations.AlterField(
            model_name="familydetails",
            name="fam_fk",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="household.families",
                verbose_name="Family head",
            ),
        ),
        migrations.AlterField(
            model_name="familydetails",
            name="fam_member",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="household.demographies",
                verbose_name="Family member",
            ),
        ),
        migrations.AlterField(
            model_name="familydetails",
            name="relationship",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="library.familyrelationship",
                verbose_name="Relationship",
            ),
        ),
        migrations.AlterField(
            model_name="familydetails",
            name="remarks",
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="familydetails",
            name="status",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="library.familystatus",
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="hhlivelihoods",
            name="controlnumber",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="household.households",
                verbose_name="Livelihood belong",
            ),
        ),
    ]
