# models/certificate.py

from pydantic import BaseModel
from typing import Optional


class CertificateInfo(BaseModel):
    """
    Model representing a device certificate.
    """

    certificate_name: str
    common_name: Optional[str]
    expiration_date: Optional[str]
    issuer: Optional[str]
    valid_from: Optional[str]
    valid_to: Optional[str]
    status: Optional[str]
    algorithm: Optional[str]
    serial_number: Optional[str]
