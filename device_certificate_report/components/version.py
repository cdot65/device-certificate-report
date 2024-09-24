# device_certificate_report/components/version.py

import re


class Version:
    def __init__(self, major: int, feature: int, maintenance: int, hotfix: int = 0):
        self.major = major
        self.feature = feature
        self.maintenance = maintenance
        self.hotfix = hotfix

    def __lt__(self, other):
        if self.major != other.major:
            return self.major < other.major
        if self.feature != other.feature:
            return self.feature < other.feature
        if self.maintenance != other.maintenance:
            return self.maintenance < other.maintenance
        return self.hotfix < other.hotfix

    def __repr__(self):
        if self.hotfix:
            return f"{self.major}.{self.feature}.{self.maintenance}-h{self.hotfix}"
        else:
            return f"{self.major}.{self.feature}.{self.maintenance}"


def parse_version(version_str: str) -> Version:
    """
    Parse a version string into a Version object.
    """
    # Example version strings: '10.2.10-h4', '9.1.13-h5', '11.1.0'
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)(?:-h(\d+))?$", version_str)
    if not match:
        raise ValueError(f"Invalid version format: {version_str}")
    major = int(match.group(1))
    feature = int(match.group(2))
    maintenance = int(match.group(3))
    hotfix = int(match.group(4)) if match.group(4) else 0
    return Version(major, feature, maintenance, hotfix)
