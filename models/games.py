
"""Game model module"""
from django.db import models


class Games(models.Model):
    """Game database model"""
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    designer = models.CharField(max_length=75)
    yearReleased = models.IntegerField()
    numOfPlayers = models.IntegerField()
    estimatedTimeOfPlay = models.IntegerField()
    ageRecommendation = models.IntegerField()