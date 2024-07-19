
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize





# euro24_groups = requests.get(f'https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.groups.json')
# euro24_rounds = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.json')

# def euro24_groups():

#     res = requests.get(f'https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.groups.json').json()['groups']
#     for grp in res:
#         grp_name= grp['name']
#         print(grp_name)
#         grp_teams= grp['teams']
#         print(grp_teams)    

    
    


def index(request):
        # groups_ = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.groups.json').json()['groups']
        # groups = { 'groups' : groups_}
        rounds_ = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.json').json()['rounds']
        rounds = { 'rounds' : rounds_}
        return render(request, 'index.html',  rounds )

