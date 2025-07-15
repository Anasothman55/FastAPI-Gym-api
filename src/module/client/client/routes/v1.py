from fastapi import APIRouter

clientRouter = APIRouter(
  tags=['Client']
)



@clientRouter.get('/')
async def get_current_client(): return 'client'

@clientRouter.patch('/')
async def update_current_client(): return 'update'