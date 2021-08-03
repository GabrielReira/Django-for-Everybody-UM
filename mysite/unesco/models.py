from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    justification = models.TextField(null=True)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)

    # Foreign Keys
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE, null=True)
