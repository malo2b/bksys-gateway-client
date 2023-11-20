"""Transactions routes."""

import logging
from fastapi import APIRouter

log = logging.getLogger(__name__)


router = APIRouter(prefix="/transactions")


@router.post("/{rib}", tags=["Transactions"])
async def get_account():
    raise NotImplementedError
