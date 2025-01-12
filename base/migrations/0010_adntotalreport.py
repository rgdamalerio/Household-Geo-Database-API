# Generated by Django 4.1 on 2023-11-15 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_brgyinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdnTotalReport',
            fields=[
                ('households', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('families', models.BigIntegerField(blank=True, null=True)),
                ('person', models.BigIntegerField(blank=True, null=True)),
                ('male', models.BigIntegerField(blank=True, null=True)),
                ('female', models.BigIntegerField(blank=True, null=True)),
                ('infant', models.BigIntegerField(blank=True, null=True)),
                ('elderly', models.BigIntegerField(blank=True, null=True)),
                ('illiteracy', models.BigIntegerField(blank=True, null=True)),
                ('ip', models.BigIntegerField(blank=True, null=True)),
                ('pwd', models.BigIntegerField(blank=True, null=True)),
                ('malnurished', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'adn_total_report',
                'managed': False,
            },
        ),
    ]
