from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.config.setting import settings
from sqlalchemy import  text

class Base(DeclarativeBase):
  pass

engine: AsyncEngine = create_async_engine(
  url=settings.POSTGRESQL_URI,
  echo = False,
  pool_size = 3,
  max_overflow= 20,
  pool_timeout= 30,
  pool_recycle= 3600,
)



async_session_maker: async_sessionmaker[AsyncSession]  = async_sessionmaker(
  bind=engine,
  class_= AsyncSession,
  expire_on_commit=False
)

async def close_db_connection():
  await engine.dispose()

async def init_db():
  async with engine.begin() as conn :
    await conn.run_sync(Base.metadata.create_all)
    print("Database table create successfully")

  async with async_session_maker() as db:
    result = await db.execute(text("SELECT 1"))
    scalar_result = result.scalar_one()
    print(f"Connection test result: {scalar_result}")  # Should print 1



@asynccontextmanager
async def life_span(app: FastAPI):
  try:
    await init_db()
  except Exception as e:
    print(f'Error initializing database: {e}')
    raise
  yield
  try:
    await close_db_connection()
    print("Application shutdown complete")
  except Exception as e:
    print(f"Error closing database connection: {str(e)}")











