# Docker Execution for device-certificate-report

Run `device-certificate-report` in Docker for a consistent setup across systems. This guide details the steps for Docker configuration and execution, including options for generating reports from Panorama or CSV files.

## Pulling the Docker Image

Pull the `device-certificate-report` image from GitHub Packages:

<!-- termynal -->
```bash
docker pull ghcr.io/cdot65/device-certificate-report:latest
```

## Running the Container

### Basic Execution

To run the container with interactive prompts:

<!-- termynal -->
```bash
docker run -it --rm ghcr.io/cdot65/device-certificate-report:latest
```

### Executing with Command-Line Arguments

For Panorama-based report generation:

<!-- termynal -->
```bash
docker run -it --rm \
  -v "$(pwd)/output:/app/output" \
  ghcr.io/cdot65/device-certificate-report:latest \
  panorama --hostname <panorama_ip> --username <username> --password <password>
```

For CSV-based report generation:

<!-- termynal -->
```bash
docker run -it --rm \
  -v "$(pwd)/input:/app/input" \
  -v "$(pwd)/output:/app/output" \
  ghcr.io/cdot65/device-certificate-report:latest \
  csv --file /app/input/devices.csv
```

## Command-Line Arguments

The `device-certificate-report` Docker container supports various arguments to customize its execution:

### Global Options

- `--help`: Show the help message and exit.
- `--version`: Show the version and exit.

### Panorama Report Command

<!-- termynal -->
```bash
docker run ... panorama [OPTIONS]
```

Options:
- `--hostname TEXT`: Panorama IP address or hostname [required]
- `--username TEXT`: Username for Panorama authentication [required]
- `--password TEXT`: Password for Panorama authentication [required]
- `--port INTEGER`: Port number for Panorama connection [default: 443]

### CSV Report Command

<!-- termynal -->
```bash
docker run ... csv [OPTIONS]
```

Options:
- `--file PATH`: Path to the input CSV file within the container [required]

## Volume Mounts

- Mount an output directory to save generated reports:
  `-v "$(pwd)/output:/app/output"`

- For CSV input, mount an input directory:
  `-v "$(pwd)/input:/app/input"`

## Examples

### Generating a Report from Panorama

<!-- termynal -->
```bash
docker run -it --rm \
  -v "$(pwd)/output:/app/output" \
  ghcr.io/cdot65/device-certificate-report:latest \
  panorama --hostname 192.168.1.1 --username admin --password admin123
```

### Generating a Report from CSV

<!-- termynal -->
```bash
docker run -it --rm \
  -v "$(pwd)/input:/app/input" \
  -v "$(pwd)/output:/app/output" \
  ghcr.io/cdot65/device-certificate-report:latest \
  csv --file /app/input/devices.csv
```

## Output

The generated reports (PDF and CSV) will be available in the mounted output directory on your host system.

## Troubleshooting

If you encounter issues:

1. Ensure Docker is properly installed and running on your system.
2. Verify that you have the latest version of the `device-certificate-report` image.
3. Check network connectivity if connecting to Panorama.
4. Review the console output for any error messages.

For persistent issues, please open an issue on our GitHub repository with a detailed description of the problem and any relevant error messages.