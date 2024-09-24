# Docker Execution for device-certificate-report

Run `device-certificate-report` in Docker for a consistent setup across systems. This guide details the steps for Docker configuration and execution, including options for generating reports from Panorama or CSV files.

## Pulling the Docker Image

Pull the `device-certificate-report` image from GitHub Packages:

<div class="termy">

<!-- termynal -->
```bash
$ docker pull ghcr.io/cdot65/device-certificate-report:latest
```

</div>

Or build your own custom version of the Dockerfile [in this getting started guide](./getting-started.md).

## Running the Container

### Basic Execution

To run the container with interactive prompts:

<div class="termy">

<!-- termynal -->
```bash
$ docker run -it --rm ghcr.io/cdot65/device-certificate-report:latest
```

</div>

### Executing with Command-Line Arguments

For Panorama-based report generation:

<div class="termy">

<!-- termynal -->
```bash
$ docker run -it --rm \
  -v "$(pwd):/app" \
  ghcr.io/cdot65/device-certificate-report:latest \
  panorama --hostname <panorama_ip> --username <username> --password <password>
```

</div>

For CSV-based report generation:

<div class="termy">

<!-- termynal -->
```bash
$ docker run -it --rm \
  -v "$(pwd):/app" \
  ghcr.io/cdot65/device-certificate-report:latest \
  csv --file /app/devices.csv
```

</div>

## Command-Line Arguments

The `device-certificate-report` Docker container supports various arguments to customize its execution:

### Global Options

- `--help`: Show the help message and exit.
- `--version`: Show the version and exit.

### Panorama Report Command

<div class="termy">

<!-- termynal -->
```bash
$ docker run ... panorama [OPTIONS]
```

</div>

Options:
- `--hostname TEXT`: Panorama IP address or hostname [required]
- `--username TEXT`: Username for Panorama authentication [required]
- `--password TEXT`: Password for Panorama authentication [required]
- `--port INTEGER`: Port number for Panorama connection [default: 443]

### CSV Report Command

<div class="termy">

<!-- termynal -->
```bash
$ docker run ... csv [OPTIONS]
```

</div>

Options:
- `--file PATH`: Path to the input CSV file within the container [required]

## Volume Mounts

- Mount your local directory to import local files and export generated reports:
  `-v "$(pwd):/app"`

## Examples

### Generating a Report from Panorama

<div class="termy">

<!-- termynal -->
```bash
$ docker run -it --rm \
  -v "$(pwd):/app" \
  ghcr.io/cdot65/device-certificate-report:latest \
  panorama --hostname 192.168.1.1 --username admin --password admin123
```

</div>

### Generating a Report from CSV

<div class="termy">

<!-- termynal -->
```bash
$ docker run -it --rm \
  -v "$(pwd):/app" \
  ghcr.io/cdot65/device-certificate-report:latest \
  csv --file /app/panorama.csv
```

</div>

## Output

The generated reports (PDF and CSV) will be available in the mounted directory on your host system.

## Troubleshooting

If you encounter issues:

1. Ensure Docker is properly installed and running on your system.
2. Verify that you have the latest version of the `device-certificate-report` image.
3. Check network connectivity if connecting to Panorama.
4. Review the console output for any error messages.

For persistent issues, please open an issue on our GitHub repository with a detailed description of the problem and any relevant error messages.