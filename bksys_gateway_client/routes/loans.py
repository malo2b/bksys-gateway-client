"""Loans routes."""

import logging
from fastapi import APIRouter

log = logging.getLogger(__name__)


router = APIRouter(prefix="/loans")


@router.get("/", tags=["loans"])
async def get_account():
    raise NotImplementedError
