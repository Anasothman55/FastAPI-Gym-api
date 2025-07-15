from src.config.setting import settings

if __name__ == '__main__':
  import uvicorn

  uvicorn.run(
    app="src.main:app",
    port=settings.SERVER_PORT,
    host=settings.SERVER_DOMAIN,
    reload=True
  )


"""
alembic
1- alembic init -t async migrations
2- alembic revision --autogenerate -m "1st migrations"
3- alembic upgrade 9252446b8f25    
"""


