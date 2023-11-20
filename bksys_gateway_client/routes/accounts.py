"""Accounts routes."""

import logging
from fastapi import APIRouter, Depends

# from ..author import authorize
from ..schemas.accounts import Account
from ..services.account_service import AccountService

log = logging.getLogger(__name__)


router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.get("/")
async def get_accounts(
    service: AccountService = Depends(),
    # author=Depends(authorize("get-account"))
) -> list[Account]:
    raise NotImplementedError


@router.get("/{id}")
async def get_account(
    id: str,
    service: AccountService = Depends(),
    # author=Depends(authorize("get-account")),
) -> Account:
    raise NotImplementedError
