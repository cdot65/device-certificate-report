# device_certificate_report/config.py

from typing import Dict, List, Set
from device_certificate_report.version import Version

# Affected device families and models
AffectedFamilies: Dict[str, List[str]] = {
    "200": ["PA-200"],
    "220": ["PA-220", "PA-220-ZTP", "PA-220R", "PA-220R-ZTP"],
    "3000": ["PA-3020", "PA-3050", "PA-3060"],
    "3200": ["PA-3220", "PA-3220-ZTP", "PA-3250", "PA-3250-ZTP", "PA-3260"],
    "500": ["PA-500"],
    "5000": ["PA-5020", "PA-5050", "PA-5060"],
    "5200": ["PA-5220", "PA-5250", "PA-5260", "PA-5280"],
    "7000": ["PA-7050", "PA-7080"],
    "800": ["PA-820", "PA-820-ZTP", "PA-850", "PA-850-ZTP"],
    "vm": ["PA-VM", "PA-VM (lite)"],
    "vmarm": ["PA-VMARM"],
}

# Unaffected device families and models
UnaffectedFamilies: Dict[str, List[str]] = {
    "400": [
        "PA-410",
        "PA-415",
        "PA-415-5G",
        "PA-440",
        "PA-445",
        "PA-450",
        "PA-450R",
        "PA-460",
    ],
    "1400": ["PA-1410", "PA-1420"],
    "3400": ["PA-3410", "PA-3420", "PA-3430", "PA-3440"],
    "5400": ["PA-5450"],
    "5400f": ["PA-5410", "PA-5420", "PA-5430", "PA-5440", "PA-5445"],
    "7500": ["PA-7500"],
}

# Flatten the lists to create sets for quick lookup
AffectedModels: Set[str] = {
    model for models in AffectedFamilies.values() for model in models
}
UnaffectedModels: Set[str] = {
    model for models in UnaffectedFamilies.values() for model in models
}

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
