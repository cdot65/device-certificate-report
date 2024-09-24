# device_certificate_report/components/hardware_families.py

from typing import Dict, List, Set

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
