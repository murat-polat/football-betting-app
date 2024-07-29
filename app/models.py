

from django.db import models
import json
from importlib import resources
import requests

# class Rounds(models.Model):
#         rounds_ = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.json').json()['rounds']
#         rounds = { 'rounds' : rounds_}
#         models.JSONField(rounds)


# class UserScore(models.Model):
#     username = models.CharField(max_length=200)
#     team1_score = models.IntegerField(default=0)
#     team2_score = models.IntegerField(default=0)

#     def __str__(self):
#         return self.username, self.team1_score,self.team2_score
    


# models.py


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    country = models.CharField(max_length=255)

    def __repr__(self):
        return self.name, self.code, self.country

class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    team1 = models.CharField(max_length=255)
    team2 = models.CharField(max_length=255)
    score1 = models.IntegerField(null=True, blank=True)
    score2 = models.IntegerField(null=True, blank=True)

    def __repr__(self):
        return self.team1, self.team2, self.score1, self.score2


class Betting(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    user_score1 = models.IntegerField(null=True, blank=True)
    user_score2 = models.IntegerField(null=True, blank=True)

    def __repr__(self):
        return self.user_score1, self.user_score2