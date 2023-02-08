from pymongo import MongoClient
from utils import error_response, response

client = MongoClient("mongodb+srv://trace:Sb2O2k3w01aL0CGC@cluster1.gorvlno.mongodb.net/?retryWrites=true&w=majority")
db = client['mydb']
teams = db['teams']
flags = db['flags']
challenges = db['challenges']

def teams_helper(team):
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

def challenge_helper(challenge):
    return {
        "id": str(challenge["_id"]),
        "challenge_name": challenge["challenge_name"],
        "description": challenge["description"],
        "score": challenge["score"],
        "file_link": challenge["file_links"],
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

def update_team_score(team_name, score, security_token):
    result = teams.update_one({'team_name': team_name}, {'$set': {'score': score}})

    if result.matched_count == 0:
        return error_response(['failed'], f'Team: {team_name} not found')
    team = teams.find_one({'team_name': team_name})
    return response(teams_helper(team), f'Team {team_name} updated')


def submit_flag(team_name: str, flag: str, security_token: str = 'hash'):
    score = 222

    if flags.find_one({'flag': flag}):
        score += 100
        return update_team_score(team_name, score, security_token)
    return error_response('failed', f'Team {team_name} not found')


def create_flag(challenge_name: str, security_token: str = 'hash'):
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

def create_challenge(challenge_name: str, description: str, score: int, file_links: list[str] = []):
    data = {
        'challenge_name': challenge_name,
        'description': description,
        'score': score,
        'file_links': file_links
    }

    existing_challenge = challenges.find_one({'challenge_name': challenge_name})
    if existing_challenge:
        return error_response('failed', f'Challenge {challenge_name} already exists')

    result = challenges.insert_one(data)
    challenge = challenges.find_one({'_id': result.inserted_id})
    return response(challenge_helper(challenge), f'Challenge {challenge_name} created')

def get_challenges():
    data = []
    for challenge in challenges.find():
        data.append(challenge_helper(challenge))
    return response(data, 'success')