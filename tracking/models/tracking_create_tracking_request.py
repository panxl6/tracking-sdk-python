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
from tracking.models.next_couriers_tracking_create_tracking_request import (
    NextCouriersTrackingCreateTrackingRequest,
)


class TrackingCreateTrackingRequest(BaseModel):
    """
    TrackingCreateTrackingRequest
    """  # noqa: E501

    tracking_number: Optional[str] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    order_id: Optional[str] = None
    order_id_path: Optional[str] = None
    custom_fields: Optional[Any] = None
    language: Optional[str] = None
    order_promised_delivery_date: Optional[str] = None
    delivery_type: Optional[str] = None
    pickup_location: Optional[str] = None
    pickup_note: Optional[str] = None
    tracking_account_number: Optional[str] = None
    tracking_key: Optional[str] = None
    tracking_ship_date: Optional[str] = None
    emails: Optional[List[str]] = None
    smses: Optional[List[str]] = None
    customer_name: Optional[str] = None
    origin_country_iso3: Optional[str] = None
    origin_state: Optional[str] = None
    origin_city: Optional[str] = None
    origin_postal_code: Optional[str] = None
    origin_raw_location: Optional[str] = None
    destination_country_iso3: Optional[str] = None
    destination_state: Optional[str] = None
    destination_city: Optional[str] = None
    destination_postal_code: Optional[str] = None
    destination_raw_location: Optional[str] = None
    note: Optional[str] = None
    slug_group: Optional[SlugGroupV1] = None
    order_date: Optional[str] = None
    order_number: Optional[str] = None
    shipment_type: Optional[str] = None
    shipment_tags: Optional[List[str]] = None
    courier_connection_id: Optional[str] = None
    next_couriers: Optional[List[NextCouriersTrackingCreateTrackingRequest]] = None
    tracking_origin_country: Optional[str] = None
    tracking_destination_country: Optional[str] = None
    tracking_postal_code: Optional[str] = None
    tracking_state: Optional[str] = None
    location_id: Optional[str] = None
    shipping_method: Optional[str] = None

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
