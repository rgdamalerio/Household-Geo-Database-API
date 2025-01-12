# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class PointSenior(models.Model):
    household_number = models.TextField(blank=True, null=True)
    munname = models.CharField(max_length=255, blank=True, null=True)
    brgyname = models.CharField(max_length=255, blank=True, null=True)
    purok = models.CharField(max_length=255, blank=True, null=True)
    brgycode = models.CharField(max_length=255, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    lat = models.CharField(max_length=50, blank=True, null=True)
    long = models.CharField(max_length=50, blank=True, null=True)
    person = models.BigIntegerField(blank=True, null=True)
    elderly_male = models.BigIntegerField(blank=True, null=True)
    elderly_female = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'point_senior'
