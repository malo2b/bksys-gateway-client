"""Initialize client gateway."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.monitoring import router as monitoring_router

logging.basicConfig(format='%(levelname)s : %(asctime)s : [%(name)s]: %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)


# Initialize FastAPI app
app = FastAPI()
log.info("Initializing FastAPI app.")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="https?://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routes
app.include_router(monitoring_router)

__all__ = ["app", "settings"]
