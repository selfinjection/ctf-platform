from pymongo import MongoClient
from utils import response, error_response

client = MongoClient("mongodb+srv://trace:Sb2O2k3w01aL0CGC@cluster1.gorvlno.mongodb.net/?retryWrites=true&w=majority")
db = client['mydb']
teams = db['teams']
flags = db['flags']


def teams_helper(team) -> dict:
    return {
        "id": str(team["_id"]),
        "team_name": team["team_name"],
        "score": team["score"],
    }


def flags_helper(flag):
    return {
        "id": str(flag["_id"]),
        "challenge": flag["challenge"],
        "flag": flag["flag"],
    }


def create_team(team_name: str, score: int, security_token):
    data = {
        'team_name': team_name, 
        'score': score
    }
    existing_team = teams.find_one({'team_name': team_name})
    if existing_team:
        error_response('failed', f'Team {team_name} already exists')

    result = teams.insert_one(data)
    team = teams.find_one({'_id': result.inserted_id})
    return response(teams_helper(team), f'Team {team_name} created')


def update_team_score(team_name, score, security_token):
    result = teams.update_one({'team_name': team_name}, {'$set': {'score': score}})

    if result.matched_count == 0:
        return error_response(['failed'], f'Team: {team_name} not found')

    team = teams.find_one({'team_name': team_name})
    return response(teams_helper(team), f'Team {team_name} updated')


def get_teams():
    result = []

    for team in teams.find():
        result.append(teams_helper(team))
    return result


def delete_team(team_name, security_token):
    existing_team = teams.find_one({'team_name': team_name})

    if existing_team:
        teams.delete_one({'team_name': team_name})
        return response(None, f'{team_name} deleted.')

    return error_response('failed', f'{team_name} not exists')


def submit_flag(team_name: str, flag: str, security_token: str = 'hash'):
    score = 222

    if flags.find_one({'flag': flag}):
        score += 100
        return update_team_score(team_name, score, security_token)
    return error_response('failed', f'Team {team_name} not found')


def create_flag(challenge_name: str, security_token):
    flag = '123123'
    data = {
        'challenge': challenge_name, 
        'flag': flag
    }

    existing_challenge = flags.find_one({'challenge': challenge_name})

    if existing_challenge:
        return error_response('failed', f'Challenge {challenge_name} already exists')

    result = flags.insert_one(data)
    flag = flags.find_one({'_id': result.inserted_id})
    return response(flags_helper(flag), f'Challenge {challenge_name} created')