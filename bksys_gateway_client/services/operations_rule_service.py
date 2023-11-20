"""OperationsRuleService class."""

import logging
import aiohttp
from fastapi import HTTPException
from starlette import status

from ..settings import app_settings

log = logging.getLogger(__name__)


class OperationsRuleService:
    """OperationsRuleService class."""

    def __init__(self) -> None:
        """Init.

        Args:
            settings (AppSettings): App settings.
        """
        self.host: str = app_settings.OPERAIONS_RULE_MS_HOST

    async def health_check(self) -> bool:
        """Health check.

        Raises:
            HTTPException:
             - HTTP_503_SERVICE_UNAVAILABLE if service is not available

        Returns:
            bool: True if service is available
        """

        log.info(f"Requesting health check from operations rule service. {self.host}/service-status")
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f"{self.host}/service-status") as response:
                    return response.status == 200
            except aiohttp.ClientError:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)


__all__ = ["OperationsRuleService"]
