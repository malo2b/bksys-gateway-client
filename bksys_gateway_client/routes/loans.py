"""Loans routes."""

import logging
from fastapi import APIRouter, HTTPException

log = logging.getLogger(__name__)


router = APIRouter(prefix="/loans", tags=["Loans"])


@router.get("/")
async def get_account():
    raise HTTPException(status_code=501, detail="Not implemented")
