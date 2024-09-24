# device_certificate_report/components/data_collection.py

import csv
import logging

from typing import List

from panos.panorama import Panorama
from panos.firewall import Firewall

logger = logging.getLogger(__name__)

from device_certificate_report.models.device import DeviceInfo


def process_csv_file(csv_file: str) -> List[DeviceInfo]:
    """
    Process the cleaned CSV file to extract device information.

    Parameters
    ----------
    csv_file : str
        Path to the cleaned CSV file.

    Returns
    -------
    List[DeviceInfo]
        A list of device information extracted from the CSV.
    """
    devices = []

    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Fields that might have multiple entries
            device_names = [
                name.strip() for name in row.get("Device Name", "").split(";")
            ]
            serial_numbers = [
                sn.strip() for sn in row.get("IP Address Serial Number", "").split(";")
            ]
            ipv4_addresses = [
                ip.strip() for ip in row.get("IP Address IPv4", "").split(";")
            ]
            device_states = [
                state.strip() for state in row.get("Status Device State", "").split(";")
            ]
            device_certificates = [
                cert.strip()
                for cert in row.get("Status Device Certificate", "").split(";")
            ]
            device_certificate_expiry_dates = [
                date.strip()
                for date in row.get("Status Device Certificate Expiry Date", "").split(
                    ";"
                )
            ]
            globalprotect_clients = [
                gp.strip() for gp in row.get("GlobalProtect Client", "").split(";")
            ]

            # Determine the number of devices in this row
            num_devices = len(device_names)

            # Fields that may have single value
            model = row.get("Model", "").strip()
            software_version = row.get("Software Version", "").strip()

            for i in range(num_devices):
                device = DeviceInfo(
                    device_name=device_names[i] if i < len(device_names) else None,
                    model=model or None,
                    serial_number=(
                        serial_numbers[i] if i < len(serial_numbers) else None
                    ),
                    ipv4_address=ipv4_addresses[i] if i < len(ipv4_addresses) else None,
                    device_state=device_states[i] if i < len(device_states) else None,
                    device_certificate=(
                        device_certificates[i] if i < len(device_certificates) else None
                    ),
                    device_certificate_expiry_date=(
                        device_certificate_expiry_dates[i]
                        if i < len(device_certificate_expiry_dates)
                        else None
                    ),
                    software_version=software_version or None,
                    globalprotect_client=(
                        globalprotect_clients[i]
                        if i < len(globalprotect_clients)
                        and globalprotect_clients[i] != "0.0.0"
                        else None
                    ),
                )
                devices.append(device)

    return devices


def collect_data_from_panorama(panorama: Panorama) -> List[DeviceInfo]:
    """
    Collect data from Panorama and its connected devices.

    Parameters
    ----------
    panorama : Panorama
        An authenticated Panorama instance.

    Returns
    -------
    List[DeviceInfo]
        A list of device information collected from connected firewalls.
    """
    devices = []

    try:
        logger.info("Sending operational command to Panorama to retrieve all devices.")
        response = panorama.op(
            "<show><devices><all/></devices></show>",
            cmd_xml=False,
        )
    except Exception as e:
        logger.error(f"Failed to retrieve devices from Panorama: {e}")
        return devices

    # Parse the XML response
    try:
        logger.info("Parsing XML response from Panorama.")
        devices_entries = response.findall(".//devices/entry")
        logger.info(f"Found {len(devices_entries)} devices connected to Panorama.")

        for entry in devices_entries:
            # Extract required fields
            device_name = entry.findtext("hostname")
            model = entry.findtext("model")
            serial_number = entry.findtext("serial")
            ipv4_address = entry.findtext("ip-address")
            device_state = entry.findtext("connected")
            device_certificate = entry.findtext("device-cert-present")
            device_certificate_expiry_date = entry.findtext("device-cert-expiry-date")
            software_version = entry.findtext("sw-version")
            globalprotect_client = entry.findtext(
                "global-protect-client-package-version"
            )

            device = DeviceInfo(
                device_name=device_name or "",
                model=model or "",
                serial_number=serial_number or "",
                ipv4_address=ipv4_address or "",
                device_state="Connected" if device_state == "yes" else "Disconnected",
                device_certificate=device_certificate or "",
                device_certificate_expiry_date=device_certificate_expiry_date or "",
                software_version=software_version or "",
                globalprotect_client=(
                    globalprotect_client if globalprotect_client != "0.0.0" else ""
                ),
            )
            devices.append(device)
    except Exception as e:
        logger.error(f"Error parsing devices from Panorama response: {e}")

    return devices


def collect_data_from_firewall(firewall: Firewall) -> DeviceInfo:
    """
    Collect data from a single firewall device.

    Parameters
    ----------
    firewall : Firewall
        An authenticated Firewall instance.

    Returns
    -------
    DeviceInfo
        Device information collected from the firewall.
    """
    try:
        logger.info("Sending operational command to Firewall to retrieve system info.")
        system_info_response = firewall.op(
            cmd="<show><system><info/></system></show>",
            cmd_xml=False,
        )
    except Exception as e:
        logger.error(f"Failed to retrieve system info from Firewall: {e}")
        raise e

    try:
        logger.info(
            "Sending operational command to Firewall to retrieve device certificate status."
        )
        device_cert_response = firewall.op(
            cmd="<show><device-certificate><status/></device-certificate></show>",
            cmd_xml=False,
        )
    except Exception as e:
        logger.error(f"Failed to retrieve device certificate status from Firewall: {e}")
        device_cert_response = None  # Proceed without certificate info

    # Parse the system info response
    try:
        logger.info("Parsing XML response from Firewall system info.")
        system_info = system_info_response.find(".//system")

        if system_info is None:
            logger.error("No system info found in the Firewall response.")
            raise ValueError("No system info found in the Firewall response.")

        # Extract required fields from system info
        device_name = system_info.findtext("hostname")
        model = system_info.findtext("model")
        serial_number = system_info.findtext("serial")
        ipv4_address = system_info.findtext("ip-address")
        device_state = "Connected"  # Since we are connected to the firewall
        software_version = system_info.findtext("sw-version")
        globalprotect_client = system_info.findtext(
            "global-protect-client-package-version"
        )
        device_certificate_status = system_info.findtext("device-certificate-status")

    except Exception as e:
        logger.error(f"Error parsing system info from Firewall response: {e}")
        raise e

    # Initialize certificate expiry date
    device_certificate_expiry_date = ""

    # Parse the device certificate status response
    try:
        if device_cert_response is not None:
            logger.info("Parsing XML response from Firewall device certificate status.")
            cert_info = device_cert_response.find(".//device-certificate")

            if cert_info is not None:
                device_certificate_status = (
                    cert_info.findtext("validity") or device_certificate_status
                )
                device_certificate_expiry_date = (
                    cert_info.findtext("not_valid_after") or ""
                )
            else:
                logger.warning(
                    "No device certificate info found in the Firewall response."
                )

    except Exception as e:
        logger.error(
            f"Error parsing device certificate status from Firewall response: {e}"
        )
        # Proceed with whatever data we have

    # Create DeviceInfo instance
    device = DeviceInfo(
        device_name=device_name or "",
        model=model or "",
        serial_number=serial_number or "",
        ipv4_address=ipv4_address or "",
        device_state=device_state,
        device_certificate=device_certificate_status or "",
        device_certificate_expiry_date=device_certificate_expiry_date or "",
        software_version=software_version or "",
        globalprotect_client=(
            globalprotect_client if globalprotect_client != "0.0.0" else ""
        ),
    )
    return device
