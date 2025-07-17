from typing import List, Any
from fastapi_mail import FastMail, ConnectionConfig, MessageSchema, MessageType
from pydantic import EmailStr
from pathlib import Path
from jinja2 import Template
from dataclasses import dataclass
from src.config.setting import settings
from datetime import datetime, timezone



mail_config = ConnectionConfig(
  MAIL_USERNAME= settings.SMTP_USER,
  MAIL_PASSWORD= settings.SMTP_PASSWORD,
  MAIL_FROM= settings.EMAILS_FROM_EMAIL,
  MAIL_PORT= 587,
  MAIL_SERVER = settings.SMTP_HOST,
  MAIL_FROM_NAME =  settings.EMAILS_NAME,
  MAIL_STARTTLS = True,
  MAIL_SSL_TLS = False,
  USE_CREDENTIALS = True,
  VALIDATE_CERTS = True,
)


mail = FastMail(
  config= mail_config
)



def render_email_template(*, template_name: str, context: dict[str, Any]) -> str:
  template_str = (
      Path(__file__).parent / "build" / "client" / template_name
  ).read_text()

  html_content = Template(template_str).render(context)
  return html_content


def create_message(recipients: List[EmailStr], subject: str, body: str):
  message = MessageSchema(
    subject=subject,
    recipients=recipients,
    body=body,
    subtype= MessageType.html
  )
  return message



#? when user register we send this email to greet them and send url to verify
async def generate_client_register(
    email_to: str | EmailStr, username: str, verify_token:str
) :

  project_name = settings.PROJECT_NAME
  subject = f"{project_name} - New account for user {username}"
  html_content = render_email_template(
    template_name="register.html",
    context={
      "user_name": username,
      "verification_url": f'http://{settings.WIFI_DOMAIN or settings.SERVER_DOMAIN}:{settings.SERVER_PORT}/api/client/v1/auth/email/verify?token={verify_token}',
      "current_year": f'{datetime.now(timezone.utc).year}',
      "expire_hours": f'{settings.EMAIL_EXP_HOUR}'
    },
  )
  message = create_message([email_to], subject ,html_content )

  await mail.send_message(message)
























