from django.db import models

# Create your models here.
class ESG(models.Model):
    name = models.CharField(max_length=4096, unique=True)
    ticker = models.CharField(max_length=4096, )
    activity = models.CharField(max_length=4096, )
    comparison = models.CharField(max_length=4096, )
    industry = models.CharField(max_length=4096, )
    country = models.CharField(max_length=4096, )
    rating = models.CharField(max_length=4096, )


class Sustainable(models.Model):
    name = models.CharField(max_length=4096, unique=True)
    ticker = models.CharField(max_length=4096, )
    esg_rating = models.FloatField()
    risk = models.CharField(max_length=4096, )


class SPGlobal(models.Model):
    name = models.CharField(max_length=4096, unique=True)
    ticker = models.CharField(max_length=4096, )
    industry = models.CharField(max_length=4096)
    country = models.CharField(max_length=4096, )
    esg_score = models.FloatField()
    environmental_score = models.CharField(max_length=4096)
    social_score = models.CharField(max_length=4096)
    governance_score = models.CharField(max_length=4096)
