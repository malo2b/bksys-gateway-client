"""Initialize client gateway."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .routes.monitoring import router as monitoring_router
from .routes.accounts import router as accounts_router
from .routes.loans import router as loans_router
from .routes.transactions import router as transactions_router

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
app.include_router(accounts_router)
app.include_router(loans_router)
app.include_router(transactions_router)

__all__ = ["app", "settings"]
