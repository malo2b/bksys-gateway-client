"""Account schemas."""""

from ..helpers.schemas import CamelCasedBaseModel


class Account(CamelCasedBaseModel):
    """Account model."""
    id: str
    balance: float


class AccountResponse(CamelCasedBaseModel):
    """Account response."""
    data: Account
