# Getting Started with device-certificate-report

Welcome to the `device-certificate-report` library! This guide is designed to help you set up the library in your environment, with a special focus on users who may be new to Python, pip, and virtual environments.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.8 or newer.
- Access to a Palo Alto Networks firewall or Panorama appliance.
- An active internet connection for downloading the package from PyPI.

## Installation

`device-certificate-report` is available on PyPI and can be easily installed within a Python virtual environment, which is a self-contained directory containing a Python installation and additional packages.

### Setting Up a Python Virtual Environment

A Python virtual environment is recommended, especially for beginners. It helps isolate the library installation from your system-wide Python setup.

**Create a Virtual Environment:**

Run the following command to create a new virtual environment named `cert_report_env`:

<div class="termy">

<!-- termynal -->
```bash
$ python3 -m venv cert_report_env
```

</div>

This creates a new directory named `cert_report_env` with a copy of the Python interpreter and the standard library.

**Activate the Virtual Environment:**

- On Windows:

<div class="termy">

<!-- termynal -->
```bash
$ cert_report_env\Scripts\activate
```

</div>

- On macOS and Linux:

<div class="termy">

<!-- termynal -->
```bash
$ source cert_report_env/bin/activate
```

</div>

After activation, your command line will indicate that you are now in the virtual environment.

**Install `device-certificate-report`:**

Within the activated environment, install the package using pip:

<div class="termy">

<!-- termynal -->
```bash
$ pip install device-certificate-report
---> 100%
Successfully device-certificate-report
```

</div>

## Next Steps

With `device-certificate-report` successfully installed in your virtual environment, the next step is to configure the library for use with your Panorama appliance, individual firewalls, or CSV file. Visit the [Python Execution Guide](execution.md) to learn how to set up and configure `device-certificate-report` for generating certificate reports.