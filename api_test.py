import requests
import json


# response = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.groups.json')
# data = response.json()['groups']
# # print(data)
# for team in data:
#     team_name = team['name']
#     teams = team['teams']
#     for country in teams:
#         code = country['code']
#         country_name = country['name']
#         print(f" {country_name}  ({code})")




def fetch_match_data():
    response = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.json')
    data = response.json()['rounds']
    
    for round_ in data:
        round = round_['name']
        matches = round_['matches']
        for match in matches:
            id = match['num']
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
            print(f"{round}, {id}, {team1_name}, {team1_code} - {team2_name}, {team2_code} = {score1} / {score2}")

            # print(round, match)



fetch_match_data()