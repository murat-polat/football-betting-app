
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from .models import Team, Match, Betting




      
    


def index(request):
        # groups_ = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.groups.json').json()['groups']
        # groups = { 'groups' : groups_}
        rounds_ = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.json').json()['rounds']
        rounds = { 'rounds' : rounds_}
        
               
        return render(request, 'app/index.html',  rounds )

