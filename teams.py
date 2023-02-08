from fastapi import APIRouter
from database import create_team, get_teams, update_team_score, delete_team, submit_flag, create_flag

router = APIRouter(
    prefix="/api",
)


@router.get('/teams')
async def teams_get():
    return get_teams()


@router.post('/teams')
async def team_create(team_name: str, score: int = 0, security_token: str = 'hash'):
    return create_team(team_name, score, security_token)


@router.put('/teams')
async def team_score_update(team_name: str, score: int, security_token: str = 'hash'):
    return update_team_score(team_name, score, security_token)


@router.delete('/teams')
async def team_delete(team_name: str, security_token: str = 'hash'):
    return delete_team(team_name, security_token)


@router.post('/create_flag')
async def flag_create(challenge_name: str, security_token: str = 'hash'):
    return create_flag(challenge_name, security_token)


@router.post('/submit_flag')
async def submit(team_name: str, flag: str, security_token: str = 'hash'):
    return submit_flag(team_name, flag, security_token)