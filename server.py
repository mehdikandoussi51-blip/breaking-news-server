from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
api_router = APIRouter(prefix="/api")

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

app.add_middleware(
    COR
