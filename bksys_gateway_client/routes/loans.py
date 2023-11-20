"""Loans routes."""

import logging
from fastapi import APIRouter

log = logging.getLogger(__name__)


router = APIRouter(prefix="/loans", tags=["Loans"])


@router.get("/")
async def get_account():
    raise NotImplementedError
