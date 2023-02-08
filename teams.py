from fastapi import APIRouter, Query
from database import database

router = APIRouter(
    prefix="/api",
)

@router.get('/teams')
async def teams_get():
    return database.get_teams()


@router.post('/teams')
async def team_create(team_name: str, score: int = 0, security_token: str = 'hash'):
    return database.create_team(team_name, score, security_token)


@router.put('/teams')
async def team_score_update(team_name: str, score: int, security_token: str = 'hash'):
    return database.update_team_score(team_name, score, security_token)


@router.delete('/teams')
async def team_delete(team_name: str, security_token: str = 'hash'):
    return database.delete_team(team_name, security_token)


@router.post('/create_flag')
async def flag_create(challenge_name: str, security_token: str = 'hash'):
    return database.create_flag(challenge_name, security_token)


@router.post('/submit_flag')
async def submit(team_name: str, flag: str, security_token: str = 'hash'):
    return database.submit_flag(team_name, flag, security_token)


@router.post('/challenges')
async def challenge_create(challenge_name: str, description: str, score: int, file_links: list[str] = Query(default=[])):
    return database.create_challenge(challenge_name, description, score, file_links)

@router.get('/challenge')
async def challenge_get():
    return database.get_challenges()