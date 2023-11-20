"""Schemas helper module for the bksys_gateway_client package."""

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelCasedBaseModel(BaseModel):
    """CamelCasedBaseModel class for camelizing the model keys."""

    model_config = ConfigDict(alias_generator=to_camel)

    def to_json(self):
        """Convert the model to JSON with CamelCase."""
        return self.model_dump_json(by_alias=True)


__all__ = ["CamelCasedBaseModel"]
