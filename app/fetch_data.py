# fetch_data.py
import requests
import json
from app.models import Team, Match, Betting

def fetch_teams_data():
    
    response = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.groups.json')
    data = response.json()['groups']
    # print(data)


# Parsing teams
    for team_data in data:
        grp_name = team_data['name']
        teams = team_data['teams']


        for country in teams:
            code = country['code']
            country_name = country['name']
            # Saving data to the database
            Team.objects.get_or_create(country=country_name,name=grp_name,code=code)
    # print(grp_name, code,country_name) 

    # # Parsing matches
def fetch_match_data():
    response = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.json')
    data = response.json()['rounds']
    
    for round_ in data:
        round = round_['name']
        matches = round_['matches']
        for match in matches:
           
            team1_name = match['team1']['name']
            team1_code = match['team1']['code']
            
            team2_name = match['team2']['name']
            team2_code = match['team2']['code']
            if 'p' not in match['score']:
                score1 = match['score']['ft'][0]
                score2 = match['score']['ft'][1]
            else:
                score1 = match['score']['p'][0]
                score2 = match['score']['p'][1]
            print(f"{round}, {id} {team1_name}, {team1_code} - {team2_name}, {team2_code} = {score1} / {score2}")

            Match.objects.get_or_create(  team1=team1_name , team2=team2_name, score1=score1, score2=score2 )