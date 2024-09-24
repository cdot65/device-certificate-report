# PAN-OS Device Certificate Report

![Banner Image](https://raw.githubusercontent.com/cdot65/device-certificate-report/refs/heads/main/device_certificate_report/assets/logo.svg)

[![Build Status](https://github.com/cdot65/device-certificate-report/actions/workflows/ci.yml/badge.svg)](https://github.com/cdot65/device-certificate-report/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/device-certificate-report.svg)](https://badge.fury.io/py/device-certificate-report)
[![Python versions](https://img.shields.io/pypi/pyversions/device-certificate-report.svg)](https://pypi.org/project/device-certificate-report/)
[![License](https://img.shields.io/github/license/cdot65/device-certificate-report.svg)](https://github.com/cdot65/device-certificate-report/blob/main/LICENSE)

A CLI tool to generate device certificate reports from Palo Alto Networks PAN-OS devices.

This tool assists customers in navigating the information provided within [this Knowledge Base article](https://live.paloaltonetworks.com/t5/customer-advisories/update-to-additional-pan-os-certificate-expirations-and-new/ta-p/572158).

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [CSV Subcommand](#csv-subcommand)
  - [Panorama Subcommand](#panorama-subcommand)
  - [Firewall Subcommand](#firewall-subcommand)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Features

- **Multiple Data Sources**: Collect device information from CSV files, Panorama appliances, or individual firewalls.
- **Comprehensive Reports**: Generates detailed PDF reports including device certificate status, software versions, and upgrade requirements.
- **Easy to Use**: Provides a straightforward command-line interface powered by [Typer](https://typer.tiangolo.com/).
- **Data Validation**: Utilizes [Pydantic](https://pydantic-docs.helpmanual.io/) models for robust data handling.
- **Flexible Workflows**: Supports multiple workflows for different use cases and environments.

## Installation

Requires Python 3.7 or higher.

Install the package using pip:

```bash
$ pip install device-certificate-report
---> 100%
Successfully installed device-certificate-report
```

## Usage

The `device-certificate-report` utility provides three subcommands:

- [`csv`](#csv-subcommand): Generate a report from a CSV file containing device information.
- [`panorama`](#panorama-subcommand): Connect to a Panorama appliance to retrieve connected firewalls and generate a report.
- [`firewall`](#firewall-subcommand): Connect directly to a firewall appliance to generate a report.

### CSV Subcommand

Process a CSV file to generate the report.

```bash
$ device-certificate-report csv --csv-file <path_to_csv_file> --output-file <output_pdf>
```

* `--csv-file` and `--output-file` flags are optional*

**Examples:**

```bash
$ device-certificate-report csv                                                                                                                                                                                        ─╯
CSV file path: panorama.csv
Cleaned CSV file saved as: /Users/cdot/development/cdot65/device_certificate_report/cleaned.csv
Processing cleaned CSV file: /Users/cdot/development/cdot65/device_certificate_report/cleaned.csv
Report generated at device_certificate_report.pdf
```

```bash
$ device-certificate-report csv --csv-file panorama.csv --output-file device_certificate_report.pdf                                                                                                                    ─╯
Cleaned CSV file saved as: /Users/cdot/development/cdot65/device_certificate_report/cleaned.csv
Processing cleaned CSV file: /Users/cdot/development/cdot65/device_certificate_report/cleaned.csv
Report generated at device_certificate_report.pdf
```

### Panorama Subcommand

Connect to a Panorama appliance and generate the report from connected firewalls.

```bash
$ device-certificate-report panorama --hostname <panorama_ip> --username <user> --password <password> --output-file <output_pdf>
```

* `--hostname`, `--username`, `--password`, and `--output-file` flags are optional*


**Examples:**

```bash
$ device-certificate-report panorama                                                                                                                                                                                   ─╯
Panorama hostname or IP: panorama1.example.io
Panorama username: admin
Panorama password: 
Connecting to Panorama at panorama1.example.io
INFO:device_certificate_report.components.data_collection:Sending operational command to Panorama to retrieve all devices.
INFO:device_certificate_report.components.data_collection:Parsing XML response from Panorama.
INFO:device_certificate_report.components.data_collection:Found 14 devices connected to Panorama.
Report generated at device_certificate_report.pdf
```

```bash
$ device-certificate-report panorama --hostname panorama.example.io --username admin --password paloalto123 --output-file panorama_report.pdf                                                                      ─╯
Connecting to Panorama at panorama1.example.io
INFO:device_certificate_report.components.data_collection:Sending operational command to Panorama to retrieve all devices.
INFO:device_certificate_report.components.data_collection:Parsing XML response from Panorama.
INFO:device_certificate_report.components.data_collection:Found 14 devices connected to Panorama.
Report generated at panorama_report.pdf
```

### Firewall Subcommand

Connect to a single Firewall appliance and generate the report.

```bash
$ device-certificate-report firewall --hostname <firewall_ip> --username <user> --password <password> --output-file <output_pdf>
```

**Examples:**

```bash
$ device-certificate-report firewall                                                                                                                                                                                   ─╯
Firewall hostname or IP: austin-fw1.example.io
Firewall username: admin
Firewall password: 
Connecting to Firewall at austin-fw1.example.io
INFO:device_certificate_report.components.data_collection:Sending operational command to Firewall to retrieve system info.
INFO:device_certificate_report.components.data_collection:Sending operational command to Firewall to retrieve device certificate status.
INFO:device_certificate_report.components.data_collection:Parsing XML response from Firewall system info.
INFO:device_certificate_report.components.data_collection:Parsing XML response from Firewall device certificate status.
Report generated at austin-fw1.example.io.pdf
```

```bash
$ device-certificate-report firewall --hostname austin-fw1.example.io --username admin --password paloalto123 --output-file firewall.pdf                                                                            ─╯
Connecting to Firewall at austin-fw1.example.io
INFO:device_certificate_report.components.data_collection:Sending operational command to Firewall to retrieve system info.
INFO:device_certificate_report.components.data_collection:Sending operational command to Firewall to retrieve device certificate status.
INFO:device_certificate_report.components.data_collection:Parsing XML response from Firewall system info.
INFO:device_certificate_report.components.data_collection:Parsing XML response from Firewall device certificate status.
Report generated at firewall.pdf
```

**Note:** If `--output-file` is not specified, the report will be saved with a default name.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure that your code adheres to the existing coding standards and includes appropriate test coverage.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](./LICENSE) file for details.

## Support

For details on the support provided by Palo Alto Networks for this project, please consult the [SUPPORT.md](./SUPPORT.md) file in the repository.

---

*More extensive documentation will be available through our GitHub Pages site.*
