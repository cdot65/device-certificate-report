# components/data_collection.py

import csv
from typing import List
from panos.panorama import Panorama
from panos.firewall import Firewall
from panos.errors import PanDeviceError

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
            device_names = [name.strip() for name in row.get("Device Name", "").split(";")]
            serial_numbers = [sn.strip() for sn in row.get("IP Address Serial Number", "").split(";")]
            ipv4_addresses = [ip.strip() for ip in row.get("IP Address IPv4", "").split(";")]
            device_states = [state.strip() for state in row.get("Status Device State", "").split(";")]
            device_certificates = [cert.strip() for cert in row.get("Status Device Certificate", "").split(";")]
            device_certificate_expiry_dates = [date.strip() for date in row.get("Status Device Certificate Expiry Date", "").split(";")]
            globalprotect_clients = [gp.strip() for gp in row.get("GlobalProtect Client", "").split(";")]

            # Determine the number of devices in this row
            num_devices = len(device_names)

            # Fields that may have single value
            virtual_system = row.get("Virtual System", "").strip()
            model = row.get("Model", "").strip()
            software_version = row.get("Software Version", "").strip()

            for i in range(num_devices):
                device = DeviceInfo(
                    device_name=device_names[i] if i < len(device_names) else None,
                    virtual_system=virtual_system or None,
                    model=model or None,
                    serial_number=serial_numbers[i] if i < len(serial_numbers) else None,
                    ipv4_address=ipv4_addresses[i] if i < len(ipv4_addresses) else None,
                    device_state=device_states[i] if i < len(device_states) else None,
                    device_certificate=device_certificates[i] if i < len(device_certificates) else None,
                    device_certificate_expiry_date=device_certificate_expiry_dates[i] if i < len(device_certificate_expiry_dates) else None,
                    software_version=software_version or None,
                    globalprotect_client=globalprotect_clients[i] if i < len(globalprotect_clients) else None,
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
    # TODO: Implement data collection logic from Panorama
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
    # TODO: Implement data collection logic from Firewall
    return DeviceInfo(
        hostname=firewall.hostname,
        ip_address=firewall.hostname,
        serial_number="",
        certificates=[],
    )
