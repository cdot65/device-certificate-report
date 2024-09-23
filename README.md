# PAN-OS Device Certificate Report

![Banner Image](device_certificate_report/assets/logo.svg)

[![Build Status](https://github.com/cdot65/device-certificate-report/actions/workflows/ci.yml/badge.svg)](https://github.com/cdot65/device-certificate-report/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/device_certificate_report.svg)](https://badge.fury.io/py/device_certificate_report)
[![Python versions](https://img.shields.io/pypi/pyversions/device_certificate_report.svg)](https://pypi.org/project/device_certificate_report/)
[![License](https://img.shields.io/github/license/cdot65/device-certificate-report.svg)](https://github.com/cdot65/device-certificate-report/blob/main/LICENSE)

A tool to generate device certificate reports from PAN-OS devices.

This tool is meant to help customers navigate the information provided within [this Knowledge Base article](https://live.paloaltonetworks.com/t5/customer-advisories/update-to-additional-pan-os-certificate-expirations-and-new/ta-p/572158)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
pip install device_certificate_report
```

## Usage

The `device_certificate_report` utility provides three subcommands:

### CSV Subcommand

Process a CSV file to generate the report.

```bash
device_certificate_report csv --csv-file panorama.csv --output-file report.pdf
```

### Panorama Subcommand

Connect to a Panorama appliance and generate the report from connected firewalls.

```bash
device_certificate_report panorama --hostname <panorama_ip> --username <user> --password <password> --output-file report.pdf
```

### Firewall Subcommand

Connect to a single Firewall appliance and generate the report.

```bash
device_certificate_report firewall --hostname <firewall_ip> --username <user> --password <password> --output-file report.pdf
```

*Examples will be provided later on.*

## Configuration

Configuration is managed via Dynaconf. You can define your settings in a `settings.yaml` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](./LICENSE) file for details.


## Support

For details on the support provided by Palo Alto Networks for this project, please consult the [SUPPORT.md](./SUPPORT.md) file in the repository.
