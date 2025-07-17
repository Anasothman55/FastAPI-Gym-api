import json

from src.config.setting import settings
import uvicorn
from rich import print


if __name__ == '__main__':
  print(json.dumps({
    'localhost': f"http://{settings.SERVER_DOMAIN}:{settings.SERVER_PORT}",
    'wifi host': f"http://{settings.WIFI_DOMAIN}:{settings.SERVER_PORT}",
    'localhost docs': f"http://{settings.SERVER_DOMAIN}:{settings.SERVER_PORT}/docs#",
    'wifi host docs': f"http://{settings.WIFI_DOMAIN}:{settings.SERVER_PORT}/docs#"
  },indent=2 ))
  uvicorn.run(
    app="src.main:app",
    port=settings.SERVER_PORT,
    host= "0.0.0.0",
    reload=True,
    workers=4             # Enable HTTP/2
  )


"""
alembic
1- alembic init -t async migrations
2- alembic revision --autogenerate -m "4st migrations"
3- alembic upgrade 9252446b8f25    
"""


