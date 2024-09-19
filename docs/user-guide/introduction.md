# Introduction

## Purpose of the Project

The `device-certificate-report` CLI tool is designed to simplify the process of managing and reporting on device certificates for Palo Alto Networks firewalls. This tool offers a streamlined workflow to help administrators navigate the complex landscape of PAN-OS device certificates, especially in light of recent changes to certificate management processes.

## Problem Statement

Managing device certificates across a large network of firewalls can be complex and time-consuming. The `device-certificate-report` tool addresses these challenges by:

- Retrieving and analyzing device information from Panorama or a CSV file.
- Identifying devices that require upgrades or certificate renewals.
- Generating comprehensive reports on device certificate statuses.

## Workflow

The `device-certificate-report` tool follows a straightforward workflow:

1. **Data Collection**: Retrieve device information either from Panorama or from a provided CSV file.
2. **Analysis**: Process the collected data to identify device statuses, required upgrades, and certificate information.
3. **Report Generation**: Create detailed PDF and CSV reports with actionable insights.

## Key Features

`device-certificate-report` is equipped with several features for efficient certificate management and reporting:

- **Comprehensive Device Analysis**: Analyzes firewall devices connected to Panorama or from a provided CSV file.
- **Detailed Reporting**: Generates both PDF and CSV reports with critical device information.
- **Upgrade Recommendations**: Identifies devices requiring upgrades and specifies the appropriate version.
- **Certificate Status Tracking**: Provides detailed information on device certificate statuses.
- **User-Friendly CLI**: Utilizes Typer to create an intuitive command-line interface for easy interaction.

## Important Dates

The tool helps administrators prepare for crucial deadlines related to PAN-OS device certificates:

- **November 18, 2024**: Deadline for User-ID and Terminal Server (TS) agent remediation.
- **November 11, 2025**: New enforcement date for Device Certificate for Cloud-Delivered Security Services (CDSS).

## Affected Products and Services

The `device-certificate-report` tool is relevant for the following Palo Alto Networks products and services:

- Next-Generation Firewalls (NGFW)
- Panorama for NGFW management
- Cloud Delivered Security Services (CDSS), including WildFire/Advanced WildFire, DNS Security, and URL/Advanced URL Filtering
- User-ID using User-ID agents or Terminal Server agents
- WF-500 and WF-500-B appliances

## Next Steps

With an understanding of `device-certificate-report` and its workflow, you can proceed to set up and start using the tool for managing device certificates across your Palo Alto Networks firewall infrastructure. Follow the installation guide to get started, and refer to the usage documentation for detailed instructions on how to generate and interpret the reports.
