# Generated by Django 4.1 on 2022-08-11 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0032_alter_buildingstatus_options_and_more"),
        ("household", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Demographies",
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
                ("lastname", models.CharField(max_length=50)),
                ("firstname", models.CharField(max_length=50)),
                ("middlename", models.CharField(max_length=50, null=True)),
                ("extension", models.CharField(max_length=15, null=True)),
                ("birthdate", models.DateField()),
                ("ethnicity_by_blood", models.CharField(max_length=150, null=True)),
                ("member_ip", models.BooleanField(verbose_name="Member of IP's")),
                ("informal_settler", models.BooleanField()),
                ("religion", models.CharField(max_length=150)),
                ("person_with_special_needs", models.BooleanField()),
                ("is_ofw", models.BooleanField(verbose_name="Is OFW")),
                ("residence", models.BooleanField()),
                ("nutritional_status_recorded", models.DateField(null=True)),
                (
                    "currently_attending_school",
                    models.BooleanField(verbose_name="Currently attending in school"),
                ),
                (
                    "can_read_and_write",
                    models.BooleanField(
                        verbose_name="Can read and write or atleast high school graduate"
                    ),
                ),
                ("primary_occupation", models.CharField(max_length=255, null=True)),
                ("sss_member", models.BooleanField()),
                ("gsis_member", models.BooleanField()),
                ("philhealth_member", models.BooleanField()),
                ("dependent_of_philhealth_member", models.BooleanField()),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "controlnumber",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="household.households",
                        verbose_name="Control number",
                    ),
                ),
                (
                    "course_compleated_vocational",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="library.trackstrandcourses",
                        verbose_name="Track/Strand/Course completed (for senior High school/Vocational/College)",
                    ),
                ),
                (
                    "current_grade_level_attending",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="current_attending",
                        to="library.gradelevels",
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.genders",
                        verbose_name="Gender",
                    ),
                ),
                (
                    "highest_eductional_attainment",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_highest_attending",
                        to="library.gradelevels",
                    ),
                ),
                (
                    "marital_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.maritalstatus",
                    ),
                ),
                (
                    "monthly_income",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.monthlyincomes",
                    ),
                ),
                (
                    "nuclear_family",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="household.demographies",
                        verbose_name="Nuclear family belongs to",
                    ),
                ),
                (
                    "nutritional_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.nutritionalstatus",
                    ),
                ),
                (
                    "relationshiptohead",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.relationshiptoheads",
                        verbose_name="Relationship to head",
                    ),
                ),
                (
                    "type_of_disability",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.disabilities",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Demographies",
            },
        ),
    ]