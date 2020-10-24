# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Democharacters(models.Model):
    ide = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    house = models.TextField(blank=True, null=True)
    wand = models.TextField(blank=True, null=True)
    patronus = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    blood_status = models.TextField(blank=True, null=True)
    hair_colour = models.TextField(blank=True, null=True)
    eye_colour = models.TextField(blank=True, null=True)
    loyalty = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    birth = models.TextField(blank=True, null=True)
    death = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'models_democharacters'


class Demopotions(models.Model):
    name = models.TextField(blank=True, null=True)
    known_ingredients = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    characteristics = models.TextField(blank=True, null=True)
    difficulty_level = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'models_demopotions'


class Demospells(models.Model):
    name = models.TextField(blank=True, null=True)
    incantation = models.TextField(blank=True, null=True)
    spell_type = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    light = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'models_demospells'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class ModelsCharacters(models.Model):
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50)
    job = models.CharField(max_length=200, blank=True, null=True)
    house = models.CharField(max_length=200, blank=True, null=True)
    wand = models.CharField(max_length=200, blank=True, null=True)
    patronus = models.CharField(max_length=200, blank=True, null=True)
    species = models.CharField(max_length=200, blank=True, null=True)
    blood_status = models.CharField(max_length=200, blank=True, null=True)
    hair_color = models.CharField(max_length=200, blank=True, null=True)
    eye_color = models.CharField(max_length=200, blank=True, null=True)
    loyalty = models.CharField(max_length=200, blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'models_characters'


class ModelsPotions(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    ingredients = models.TextField()  # This field type is a guess.
    effect = models.CharField(max_length=200, blank=True, null=True)
    characteristics = models.CharField(max_length=200, blank=True, null=True)
    level = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'models_potions'


class ModelsSpell(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    incantation = models.CharField(max_length=200, blank=True, null=True)
    spell_type = models.CharField(max_length=200, blank=True, null=True)
    effect = models.CharField(max_length=200, blank=True, null=True)
    light = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'models_spell'


