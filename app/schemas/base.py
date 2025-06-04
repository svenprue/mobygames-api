import re
from datetime import datetime
from typing import Optional

from dateutil import parser
from pydantic import BaseModel, ConfigDict, Field, field_validator
from pydantic.alias_generators import to_camel


class AuditMixin(BaseModel):
    updated_at: datetime = Field(default_factory=datetime.now)


class MobyGamesBaseModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    @field_validator("year", "release_year", mode="before", check_fields=False)
    def parse_str_to_int(cls, v) -> Optional[int]:
        if v is None:
            return None
        if not v or not any(char.isdigit() for char in v):
            return None
        try:
            return int(v)
        except ValueError:
            return None

    @field_validator("games_count", mode="before", check_fields=False)
    def parse_games_count(cls, v) -> Optional[int]:
        if v is None:
            return None
        if not v or not any(char.isdigit() for char in v):
            return None
        try:
            return int(v)
        except ValueError:
            return None