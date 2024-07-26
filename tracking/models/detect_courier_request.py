# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

from __future__ import annotations
import pprint

from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from typing_extensions import Self

from tracking.models.slug_group_v1 import SlugGroupV1


class DetectCourierRequest(BaseModel):
    """
    DetectCourierRequest
    """  # noqa: E501

    tracking_number: Optional[str] = None
    slug: Optional[List[str]] = None
    tracking_postal_code: Optional[str] = None
    tracking_ship_date: Optional[str] = None
    tracking_account_number: Optional[str] = None
    tracking_key: Optional[str] = None
    tracking_origin_country: Optional[str] = None
    tracking_destination_country: Optional[str] = None
    tracking_state: Optional[str] = None
    slug_group: Optional[SlugGroupV1] = None
    origin_country_iso3: Optional[str] = None
    destination_country_iso3: Optional[str] = None

    def to_str(self, **kwargs) -> str:
        return pprint.pformat(self.model_dump(**kwargs))

    def to_json(self, **kwargs) -> str:
        return self.model_dump_json(**kwargs)

    def to_dict(self, **kwargs) -> Dict[str, Any]:
        return self.model_dump(**kwargs)

    @classmethod
    def from_json(cls, json_str: str, **kwargs) -> Optional[Self]:
        return cls.model_validate_json(json_str, **kwargs)

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]], **kwargs) -> Optional[Self]:
        return cls.model_validate(obj, **kwargs) if isinstance(obj, Dict) else None