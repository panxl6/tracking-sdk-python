# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

from __future__ import annotations
import pprint

from pydantic import BaseModel
from typing import Any, Dict, Optional
from typing_extensions import Self

from tracking.models.meta_v1 import MetaV1
from tracking.models.data_tracking_response_get_multiple_v1 import DataTrackingResponseGetMultipleV1


class TrackingResponseGetMultipleV1(BaseModel):
    """
    Tracking response for getting tracking
    """  # noqa: E501

    meta: Optional[MetaV1] = None
    data: Optional[DataTrackingResponseGetMultipleV1] = None

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
