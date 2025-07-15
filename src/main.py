from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from src.config.setting import settings
from src.database.sql.engine import life_span
from src.module.client.root import clientRoot
from src.module.shared.middleware import TimerMiddleware



app = FastAPI (
  title= "FastAPI Template",
  summary= "This are fastapi package to start project",
  version= '0.1.0',
  contact= {
    'name': "Anas Othman",
    'email': "anasothman581@gmail.com"
  },
  lifespan= life_span
)

app.add_middleware(
  CORSMiddleware, # type: ignore
  allow_origins=settings.BACKEND_CORS_ORIGINS.split(','),
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.add_middleware(TimerMiddleware) # type: ignore


app.include_router(clientRoot)





