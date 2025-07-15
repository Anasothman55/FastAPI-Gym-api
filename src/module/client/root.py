from fastapi import APIRouter, FastAPI

from src.module.client.auth.routes.v1 import clientAuthRouter
from src.module.client.client.routes.v1 import clientRouter

clientRootV1 = APIRouter(
  prefix='/v1'
)


clientRootV1.include_router(clientRouter)
clientRootV1.include_router(clientAuthRouter)

clientRootV2 = APIRouter(
  prefix='/v2'
)


clientRoot = APIRouter()

clientRoot.include_router(clientRootV1, prefix='/api/client')
clientRoot.include_router(clientRootV2, prefix='/api/client')
