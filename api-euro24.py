import requests


euro24_groups = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.groups.json')
euro24_rounds = requests.get('https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.json')


# ## Groups and Teams ##
# def Groups( *args,**kwargs):
#     groups= []
#     for group in euro24_groups.json()['groups']:
#         # print(group['name'])
#         grp_name= group['name']
#         groups.append(grp_name)
#         for team in group['teams']:
#             team_name= team['name']
#             groups.append(team_name)
#             # print(team['name'])
#     grp_A = groups[1:5]
#     grp_B = groups[6:10]
#     grp_C = groups[11:15]
#     grp_D = groups[16:20]
#     grp_E = groups[21:24]
#     grp_F = groups[25:29]

#     print({f"Group A: {grp_A}, Group B: {grp_B}, Group C: {grp_C}, Group D: {grp_D}, Group E: {grp_E}, Group F: {grp_F} "})

#     return {f"Group A: {grp_A}, Group B: {grp_B}, Group C: {grp_C}, Group D: {grp_D}, Group E: {grp_E}, Group F: {grp_F} "}
                  

# def Rounds(*args, **kwargs):
#     rounds = []
#     for round in euro24_rounds.json()['rounds']:
#         for matches in round['matches']:
           
#             team1_name = matches['team1']['name']
#             team1_code = matches['team1']['code']
#             team2_name = matches['team2']['name']
#             team2_code = matches['team2']['code']
#             score_ft = matches['score']['ft']
            
#             if 'p' not in matches['score']:
#                 result= matches['score']['ft']
#             else:
#                 result=matches['score']['p']


#             print(f"{team1_name}({team1_code}) - {team2_name}({team2_code}) : {result}  ")
#         # print(matches['score'])





# Rounds()

# Groups()   



## Groups and Teams ##
def Groups( *args,**kwargs):
    groups= []
    for group in euro24_groups.json()['groups']:
        # print(group['name'])
        grp_name= group['name']
        groups.append(grp_name)
        for team in group['teams']:
            team_name= team['name']
            groups.append(team_name)
            # print(team['name'])
            grp_A = groups[1:5]
            grp_B = groups[6:10]
            grp_C = groups[11:15]
            grp_D = groups[16:20]
            grp_E = groups[21:24]
            grp_F = groups[25:29]

            # print({f"Group A: {grp_A}, Group B: {grp_B}, Group C: {grp_C}, Group D: {grp_D}, Group E: {grp_E}, Group F: {grp_F} "})

            groups.append(grp_A)
            groups.append(grp_B)
            groups.append(grp_C)
            groups.append(grp_D)
            groups.append(grp_E)
            groups.append(grp_F)
            
        print(groups)

        return groups
                    

def Rounds(*args, **kwargs):
    rounds = []
           
    for round in euro24_rounds.json()['rounds']:
        for matches in round['matches']:
          
            team1_name = matches['team1']['name']
            team1_code = matches['team1']['code']
            team2_name = matches['team2']['name']
            team2_code = matches['team2']['code']
            score_ft = matches['score']['ft']
                
            if 'p' not in matches['score']:
                result= matches['score']['ft']
            else:
                result=matches['score']['p']
                rounds.append(result)

            rounds.append(team1_name)
            rounds.append(team1_code)
            rounds.append(team2_name)
            rounds.append(team2_code)
                
                        
        # print(f"{team1_name}({team1_code}) - {team2_name}({team2_code}) : {result}  ")
        print(rounds)
        return rounds
        # print(matches['score'])

# Rounds()
Groups()