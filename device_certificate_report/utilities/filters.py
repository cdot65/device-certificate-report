# device_certificate_report/components/filters.py

from typing import List, Tuple
from device_certificate_report.config.hardware_families import (
    AffectedModels,
    UnaffectedModels,
)
from device_certificate_report.config.panos_versions import MinimumPatchedVersions
from device_certificate_report.models.device import DeviceInfo
from device_certificate_report.components.version import parse_version


def is_affected_model(model: str) -> bool:
    return model in AffectedModels


def is_unaffected_model(model: str) -> bool:
    return model in UnaffectedModels


def filter_devices_by_model(
    devices: List[DeviceInfo],
) -> Tuple[List[DeviceInfo], List[DeviceInfo]]:
    affected_devices = []
    unaffected_devices = []
    for device in devices:
        model = device.model
        if is_affected_model(model):
            affected_devices.append(device)
        elif is_unaffected_model(model):
            unaffected_devices.append(device)
        else:
            # Devices not listed are considered unaffected but should be logged
            device.notes = "Model not recognized; considered unaffected."
            unaffected_devices.append(device)
    return affected_devices, unaffected_devices


def is_version_affected(
    device_version: str, is_global_protect: bool = False
) -> Tuple[bool, str]:
    """
    Check if the device's software version is affected.
    Returns a tuple (is_affected: bool, min_required_version: str)
    """
    try:
        current_version = parse_version(device_version)
    except ValueError as e:
        raise ValueError(f"Error parsing version '{device_version}': {e}")

    # Check if the version is 11.2 or later
    if current_version.major > 11 or (
        current_version.major == 11 and current_version.feature >= 2
    ):
        return False, ""  # Versions 11.2 and later are not affected

    # Construct the feature release string
    feature_release = f"{current_version.major}.{current_version.feature}"
    if is_global_protect and feature_release in ["10.2", "11.0", "11.1"]:
        feature_release += "-gp"

    min_versions = MinimumPatchedVersions.get(feature_release)
    if not min_versions:
        # Handle versions earlier than 8.1
        if current_version.major < 8 or (
            current_version.major == 8 and current_version.feature < 1
        ):
            return True, "8.1.0"  # Versions earlier than 8.1 are considered affected
        # Unknown feature release
        return False, ""

    for min_version in min_versions:
        if current_version < min_version:
            min_required_version = repr(min_version)
            return True, min_required_version

    return False, ""


def split_devices_by_version(
    devices: List[DeviceInfo], is_global_protect: bool = False
) -> Tuple[List[DeviceInfo], List[DeviceInfo]]:
    """
    Splits devices into those that require software upgrade and those that do not.
    Returns (no_upgrade_required, upgrade_required)
    """
    no_upgrade_required = []
    upgrade_required = []
    for device in devices:
        device_version = device.software_version
        if not device_version:
            device.notes = (
                "Software version missing; cannot determine if upgrade is required."
            )
            upgrade_required.append(device)
            continue
        try:
            affected, min_required_version = is_version_affected(
                device_version, is_global_protect
            )
        except ValueError as e:
            device.notes = f"Version parsing error: {e}"
            upgrade_required.append(device)
            continue

        if affected:
            device.min_required_version = min_required_version
            upgrade_required.append(device)
        else:
            no_upgrade_required.append(device)

    return no_upgrade_required, upgrade_required
