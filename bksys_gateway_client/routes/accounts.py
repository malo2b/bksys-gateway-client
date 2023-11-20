"""Accounts routes."""

import logging
from fastapi import APIRouter, Depends, HTTPException, status

# from ..author import authorize
from ..schemas.accounts import Account, AccountResponse
from ..services.account_service import AccountService
from ..helpers.response import HTTPResponse

log = logging.getLogger(__name__)


router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.get("/")
async def get_accounts(
    service: AccountService = Depends(),
    # author=Depends(authorize("get-account"))
) -> list[Account]:
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{id}")
async def get_account(
    id: str,
    service: AccountService = Depends(),
    # author=Depends(authorize("get-account")),
) -> Account:
    result: AccountResponse = await service.get_account(id)
    return HTTPResponse(status.HTTP_200_OK, result)
