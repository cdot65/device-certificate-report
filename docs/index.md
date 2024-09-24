<style>
.md-content .md-typeset h1 { display: none; }
</style>

<p align="center">
    <a href="https://paloaltonetworks.com"><img src="https://github.com/cdot65/device-certificate-report/blob/main/docs/images/logo.svg?raw=true" alt="PaloAltoNetworks"></a>
</p>
<p align="center">
    <em><code>device-certificate-report</code>, Reporting on PAN-OS Device Certificate Status</em>
</p>
<p align="center">
<a href="https://github.com/cdot65/device-certificate-report/graphs/contributors" target="_blank">
    <img src="https://img.shields.io/github/contributors/cdot65/device-certificate-report.svg?style=for-the-badge" alt="Contributors">
</a>
<a href="https://github.com/cdot65/device-certificate-report/network/members" target="_blank">
    <img src="https://img.shields.io/github/forks/cdot65/device-certificate-report.svg?style=for-the-badge" alt="Forks">
</a>
<a href="https://github.com/cdot65/device-certificate-report/stargazers" target="_blank">
    <img src="https://img.shields.io/github/stars/cdot65/device-certificate-report.svg?style=for-the-badge" alt="Stars">
</a>
<a href="https://github.com/cdot65/device-certificate-report/issues" target="_blank">
    <img src="https://img.shields.io/github/issues/cdot65/device-certificate-report.svg?style=for-the-badge" alt="Issues">
</a>
<a href="https://github.com/cdot65/device-certificate-report/blob/main/LICENSE" target="_blank">
    <img src="https://img.shields.io/github/license/cdot65/device-certificate-report.svg?style=for-the-badge" alt="License">
</a>
</p>

---

**Documentation**: <a href="https://cdot65.github.io/device-certificate-report/" target="_blank">https://cdot65.github.io/device-certificate-report/</a>

**Source Code**: <a href="https://github.com/cdot65/device-certificate-report" target="_blank">https://github.com/cdot65/device-certificate-report</a>

---

`device-certificate-report` is designed to help customers navigate the complex landscape of PAN-OS device certificates. This tool retrieves a list of firewall devices connected to Panorama, connects directly to a firewall, or ingests a CSV file downloaded from Panorama's Device Summary page. The result is a comprehensive PDF report highlighting devices that are unaffected due to platform model, devices that require an upgrade (and which version to upgrade to), and device certificate status information.

## Key Features

- **Multiple Data Sources**: Collect device information from Panorama appliances, individual firewalls, or CSV files.
- **Comprehensive Device Analysis**: Analyzes firewall devices to determine upgrade requirements and certificate status.
- **Detailed Reporting**: Generates detailed PDF reports with critical device information.
- **Upgrade Recommendations**: Identifies devices requiring upgrades and specifies the appropriate versions.
- **Certificate Status Tracking**: Provides detailed information on device certificate statuses and expiry dates.
- **User-Friendly CLI**: Utilizes Typer to create an intuitive command-line interface for easy interaction.

## Important Dates

- **November 18, 2024**: Deadline for User-ID and Terminal Server (TS) agent remediation.
- **November 11, 2025**: New enforcement date for Device Certificate for Cloud-Delivered Security Services (CDSS).

## Affected Products and Services

- Next-Generation Firewalls (NGFW)
- Panorama for NGFW management
- Cloud Delivered Security Services (CDSS), including WildFire/Advanced WildFire, DNS Security, and URL/Advanced URL Filtering
- User-ID using User-ID agents or Terminal Server agents
- WF-500 and WF-500-B appliances

## Workflow

1. **Data Collection**: Retrieve device information from Panorama, individual firewalls, or input CSV file.
2. **Analysis**: Process the data to identify device statuses, required upgrades, and certificate information.
3. **Report Generation**: Create detailed PDF reports with actionable insights.

---

## Execution

`device-certificate-report` can be executed using Python in a virtual environment:

<!-- termynal -->
```console
$ pip install device-certificate-report
$ device-certificate-report --help
Usage: device-certificate-report [OPTIONS] COMMAND [ARGS]...

  Generate Device Certificate Reports from PAN-OS Devices

Options:
  --help  Show this message and exit.

Commands:
  csv       Load a CSV file to extract firewall information and generate...
  firewall  Connect to a Firewall appliance to retrieve device...
  panorama  Connect to a Panorama appliance to retrieve connected...
```

For more detailed usage instructions and examples, refer to the [User Guide](user-guide/introduction.md).

---

## Contributing

Contributions are welcome and greatly appreciated. Visit the [Contributing](about/contributing.md) page for guidelines on how to contribute.

## License

This project is licensed under the Apache 2.0 License - see the [License](about/license.md) page for details.