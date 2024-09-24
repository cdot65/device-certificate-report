# device_certificate_report/components/panos_versions.py

from typing import Dict, List
from device_certificate_report.components.version import Version

# Minimum patched versions for each PAN-OS feature release
MinimumPatchedVersions: Dict[str, List[Version]] = {
    "8.1": [
        Version(8, 1, 21, 3),
        Version(8, 1, 25, 3),
        Version(8, 1, 26, 0),
    ],
    "9.0": [
        Version(9, 0, 16, 7),
        Version(9, 0, 17, 5),
    ],
    "9.1": [
        Version(9, 1, 11, 5),
        Version(9, 1, 12, 7),
        Version(9, 1, 13, 5),
        Version(9, 1, 14, 8),
        Version(9, 1, 16, 5),
        Version(9, 1, 17, 0),
    ],
    "10.0": [
        Version(10, 0, 8, 8),
        Version(10, 0, 11, 4),
        Version(10, 0, 12, 5),
    ],
    "10.1": [
        Version(10, 1, 3, 3),
        Version(10, 1, 4, 6),
        Version(10, 1, 5, 4),
        Version(10, 1, 6, 8),
        Version(10, 1, 7, 1),
        Version(10, 1, 8, 7),
        Version(10, 1, 9, 8),
        Version(10, 1, 10, 5),
        Version(10, 1, 11, 5),
        Version(10, 1, 12, 0),
    ],
    "10.2": [
        Version(10, 2, 0, 2),
        Version(10, 2, 1, 1),
        Version(10, 2, 2, 4),
        Version(10, 2, 3, 12),
        Version(10, 2, 4, 10),
        Version(10, 2, 6, 1),
        Version(10, 2, 7, 3),
        Version(10, 2, 8, 0),
    ],
    "10.2-gp": [
        Version(10, 2, 0, 3),
        Version(10, 2, 1, 2),
        Version(10, 2, 2, 5),
        Version(10, 2, 3, 13),
        Version(10, 2, 4, 16),
        Version(10, 2, 5, 6),
        Version(10, 2, 6, 3),
        Version(10, 2, 7, 8),
        Version(10, 2, 8, 3),
        Version(10, 2, 9, 1),
    ],
    "11.0": [
        Version(11, 0, 0, 2),
        Version(11, 0, 1, 3),
        Version(11, 0, 2, 3),
        Version(11, 0, 3, 3),
        Version(11, 0, 4, 0),
    ],
    "11.0-gp": [
        Version(11, 0, 0, 3),
        Version(11, 0, 1, 4),
        Version(11, 0, 2, 4),
        Version(11, 0, 3, 10),
        Version(11, 0, 4, 1),
    ],
    "11.1": [
        Version(11, 1, 0, 2),
        Version(11, 1, 1, 0),
    ],
    "11.1-gp": [
        Version(11, 1, 0, 3),
        Version(11, 1, 1, 1),
        Version(11, 1, 2, 3),
    ],
}
