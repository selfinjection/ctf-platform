from fastapi import FastAPI
from teams import router
import uvicorn

app = FastAPI()
app.include_router(router)