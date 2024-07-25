from django.db import models
from django.utils import timezone

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    typee = models.CharField(max_length=50, null=False)
    dimension = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=50, null=False)
    species = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(
        Location, related_name="location", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Episode(models.Model):
    name = models.CharField(max_length=100, null=False)
    created = models.DateTimeField()
    Episode = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    character = models.ForeignKey(
        Character, related_name="Character", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
