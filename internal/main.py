from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from adapter.inject.injector import Injector
from adapter.logger.slog import configure_logging
from adapter.routers import recommender


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initiate injector
    configure_logging()
    Injector()

    yield
    # Clean up the instances


app = FastAPI(lifespan=lifespan)
app.include_router(recommender.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
