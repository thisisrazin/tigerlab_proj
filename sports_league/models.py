from django.db import models
from .storage import OverwriteStorage

class MatchResult_File(models.Model):
    resultID=models.CharField(
        max_length=200, 
        primary_key=True, 
        unique=True, 
        blank=True
    )
    documentCSV=models.FileField(
        storage=OverwriteStorage(),
        upload_to='sports_league/documentCSV/'
    )
    uploaded_at=models.DateTimeField(auto_now_add=True)

class Match(models.Model):
    resultFile=models.ForeignKey(MatchResult_File, on_delete=models.CASCADE)
    teamOne=models.CharField(max_length=200)
    teamTwo=models.CharField(max_length=200)
    teamOneScore=models.IntegerField()
    teamTwoScore=models.IntegerField()

class Rank(models.Model):
    resultFile=models.ForeignKey(MatchResult_File, on_delete=models.CASCADE)
    team=models.CharField(max_length=200)
    points=models.IntegerField()