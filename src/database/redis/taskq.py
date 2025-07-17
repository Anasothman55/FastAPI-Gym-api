import asyncio

from rich import print
from .engine import celery_app
from ...config.email.generate import generate_client_register


@celery_app.task()
def send_cre(email: str, username: str, token: str):
  """ Send Client Register Email """
  try:
    print("this are work 73428")
    asyncio.run(generate_client_register(email, username, token))
  except Exception as e:
    print(f"[Celery Task Error] send_cre failed: {e}")

@celery_app.task()
def send_opt():
  print('opt was send')

