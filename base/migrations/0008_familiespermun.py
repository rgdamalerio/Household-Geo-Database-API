# Generated by Django 4.1 on 2023-11-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_householdpermun'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiespermun',
            fields=[
                ('munname', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
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
                'db_table': 'familiespermun',
                'managed': False,
            },
        ),
    ]