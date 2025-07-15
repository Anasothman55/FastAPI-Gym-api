from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.sql.engine import async_session_maker

async def get_db() -> AsyncGenerator[AsyncSession, None]:
  async with async_session_maker() as session:
    try:
      yield session
    except  Exception as e:
      await session.rollback()
      print(e.__dict__)
    finally:
      await session.close()