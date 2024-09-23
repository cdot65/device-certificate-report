"""
main.py: Generate Device Certificate Reports from PAN-OS Devices

This script provides a CLI utility to generate reports of device certificates from Palo Alto Networks devices.
It supports three subcommands:

- `csv`: Load a CSV file named "panorama.csv" to extract firewall information.
- `panorama`: Connect to a Panorama appliance to retrieve a list of connected firewalls.
- `firewall`: Connect directly to a firewall appliance.

Each subcommand collects necessary data and generates a PDF report.

Features
--------

- **CLI Interface**: Provides an easy-to-use command-line interface using Typer.
- **Data Models**: Utilizes Pydantic models for data validation and management.
- **Report Generation**: Generates comprehensive PDF reports of device certificates.
- **Flexible Workflows**: Supports multiple workflows for data collection.

Usage
-----

Run the CLI utility with one of the subcommands:

    device_certificate_report csv
    device_certificate_report panorama --hostname <panorama_ip> --username <user> --password <password>
    device_certificate_report firewall --hostname <firewall_ip> --username <user> --password <password>

Notes
-----

- Ensure network connectivity and valid credentials before running the tool.
- The `panorama.csv` file should be placed in the current working directory when using the `csv` subcommand.
"""

import logging
import sys
from pathlib import Path
from typing import Optional

import typer
from dynaconf import Dynaconf
from panos.firewall import Firewall
from panos.panorama import Panorama

# Import components
from device_certificate_report.components.data_collection import (
    process_csv_file,
    collect_data_from_panorama,
    collect_data_from_firewall,
)
from device_certificate_report.components.report_generation import generate_report
from device_certificate_report.components.utils import clean_csv

# Initialize Typer app
app = typer.Typer(help="Generate Device Certificate Reports from PAN-OS Devices")

# Define the path to the settings file
SETTINGS_FILE_PATH = Path.cwd() / "settings.yaml"

# Initialize Dynaconf settings object conditionally based on the existence of settings.yaml
if SETTINGS_FILE_PATH.exists():
    SETTINGS_FILE = Dynaconf(settings_files=[str(SETTINGS_FILE_PATH)])
else:
    SETTINGS_FILE = Dynaconf()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Subcommand for processing a CSV file
@app.command()
def csv(
    csv_file: Optional[str] = typer.Option(
        None,
        "--csv-file",
        "-f",
        help="Path to the CSV file containing device information",
        prompt="CSV file path",
    ),
    output_file: Optional[str] = typer.Option(
        "device_certificate_report.pdf",
        "--output-file",
        "-o",
        help="Path to the output PDF report",
    ),
):
    """
    Load a CSV file to extract firewall information and generate the device certificate report.

    Parameters
    ----------
    csv_file : str, optional
        The path to the CSV file containing device information.
    output_file : str, optional
        The path to the output PDF report.
    """
    try:
        # Clean the CSV file
        cleaned_csv_file = Path.cwd() / "cleaned.csv"
        clean_csv(csv_file, str(cleaned_csv_file))
        typer.echo(f"Cleaned CSV file saved as: {cleaned_csv_file}")

        # Process the cleaned CSV file
        typer.echo(f"Processing cleaned CSV file: {cleaned_csv_file}")
        devices = process_csv_file(str(cleaned_csv_file))

        import ipdb; ipdb.set_trace()
        # Generate the report
        generate_report(devices, output_file)
        typer.echo(f"Report generated at {output_file}")
    except Exception as e:
        logger.error(f"An error occurred while processing the CSV file: {e}")
        typer.echo(f"An error occurred: {e}", err=True)
        raise typer.Exit(code=1)


# Subcommand for connecting to a Panorama appliance
@app.command()
def panorama(
    hostname: str = typer.Option(
        ...,
        "--hostname",
        "-h",
        help="Hostname or IP address of Panorama appliance",
        prompt="Panorama hostname or IP",
    ),
    username: str = typer.Option(
        ...,
        "--username",
        "-u",
        help="Username for authentication with the Panorama appliance",
        prompt="Panorama username",
    ),
    password: str = typer.Option(
        ...,
        "--password",
        "-p",
        help="Password for authentication with the Panorama appliance",
        prompt="Panorama password",
        hide_input=True,
    ),
    output_file: Optional[str] = typer.Option(
        "device_certificate_report.pdf",
        "--output-file",
        "-o",
        help="Path to the output PDF report",
    ),
):
    """
    Connect to a Panorama appliance to retrieve connected firewalls and generate the device certificate report.

    Parameters
    ----------
    hostname : str
        Hostname or IP address of the Panorama appliance.
    username : str
        Username for authentication with the Panorama appliance.
    password : str
        Password for authentication with the Panorama appliance.
    output_file : str, optional
        The path to the output PDF report.
    """
    typer.echo(f"Connecting to Panorama at {hostname}")
    try:
        panorama = Panorama(hostname, username, password)
        devices = collect_data_from_panorama(panorama)
        generate_report(devices, output_file)
        typer.echo(f"Report generated at {output_file}")
    except Exception as e:
        logger.error(f"Failed to process Panorama: {e}")
        sys.exit(1)


# Subcommand for connecting to a Firewall appliance
@app.command()
def firewall(
    hostname: str = typer.Option(
        ...,
        "--hostname",
        "-h",
        help="Hostname or IP address of the Firewall appliance",
        prompt="Firewall hostname or IP",
    ),
    username: str = typer.Option(
        ...,
        "--username",
        "-u",
        help="Username for authentication with the Firewall appliance",
        prompt="Firewall username",
    ),
    password: str = typer.Option(
        ...,
        "--password",
        "-p",
        help="Password for authentication with the Firewall appliance",
        prompt="Firewall password",
        hide_input=True,
    ),
    output_file: Optional[str] = typer.Option(
        "device_certificate_report.pdf",
        "--output-file",
        "-o",
        help="Path to the output PDF report",
    ),
):
    """
    Connect to a Firewall appliance to retrieve device certificate information and generate the report.

    Parameters
    ----------
    hostname : str
        Hostname or IP address of the Firewall appliance.
    username : str
        Username for authentication with the Firewall appliance.
    password : str
        Password for authentication with the Firewall appliance.
    output_file : str, optional
        The path to the output PDF report.
    """
    typer.echo(f"Connecting to Firewall at {hostname}")
    try:
        firewall = Firewall(hostname, username, password)
        device = collect_data_from_firewall(firewall)
        generate_report([device], output_file)
        typer.echo(f"Report generated at {output_file}")
    except Exception as e:
        logger.error(f"Failed to process Firewall: {e}")
        sys.exit(1)


if __name__ == "__main__":
    app()
