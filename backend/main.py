from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

import redis.asyncio as aioredis
from redis.asyncio.connection import ConnectionPool
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from backend.utils import fixed_api_key_builder
from routers import auth, notes

app = FastAPI(root_path="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(notes.router)


@app.get("/")
async def index():
    return {"message": "Test API"}


@app.on_event("startup")
async def startup():
    pool = ConnectionPool.from_url(url="redis://redis")
    r = aioredis.Redis(connection_pool=pool)
    FastAPICache.init(
        RedisBackend(r), prefix="se-cache", key_builder=fixed_api_key_builder
    )
