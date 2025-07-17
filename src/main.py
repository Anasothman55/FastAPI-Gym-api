from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from src.config.setting import settings
from src.database.sql.engine import life_span
from src.module.client.root import clientRoot
from src.module.shared.middleware import TimerMiddleware
from fastapi.responses import ORJSONResponse
from rich import print

app = FastAPI (
  default_response_class=ORJSONResponse,
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
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)


app.include_router(clientRoot)





