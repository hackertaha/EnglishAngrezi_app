from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User


class Header(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to='uploads/')
    title = models.CharField(max_length=500, null=True, blank=True)
    # logo_light = models.ImageField(null=True, blank=True, upload_to='uploads/')
    book = models.ImageField(null=True, blank=True, upload_to='uploads/')
    detail=models.CharField(max_length=500, null=True, blank=True)
    description=models.CharField(max_length=500, null=True, blank=True)


    def __str__(self):
        return self.book


class Testimonals(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    details = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    sort_order = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Social_Links(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    social_url = models.URLField(max_length=256, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Arthur_Details(models.Model):
    title=models.CharField(max_length=50, null=True, blank=True)
    detail=models.CharField(max_length=5000, null=True, blank=True)
    image=models.ImageField(null=True, blank=True, upload_to='uploads/')
    sign=models.ImageField(null=True, blank=True, upload_to='uploads/')
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Pricing(models.Model):
    price = models.FloatField()
    detail=models.CharField(max_length=800, blank=True, null=True)
    description=models.CharField(max_length=800, blank=True, null=True)

    def __str__(self):
        return self.description


class Pricing_Plan(models.Model):
    title=models.CharField(max_length=800, blank=True, null=True)
    detail=models.CharField(max_length=800, blank=True, null=True)

    def __str__(self):
        return  self.detail




