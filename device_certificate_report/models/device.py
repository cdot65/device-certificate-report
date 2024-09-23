# models/device.py

from pydantic import BaseModel
from typing import Optional


class DeviceInfo(BaseModel):
    """
    Model representing a device with its relevant information.
    """

    device_name: str
    model: str
    serial_number: str
    ipv4_address: str
    device_state: Optional[str]
    device_certificate: Optional[str]
    device_certificate_expiry_date: Optional[str]
    software_version: Optional[str]
    globalprotect_client: Optional[str]
    min_required_version: Optional[str] = None
    notes: Optional[str] = None
