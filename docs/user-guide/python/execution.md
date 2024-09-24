# Python Setup and Execution Guide for device-certificate-report

This guide provides comprehensive steps for configuring and executing the `device-certificate-report` package within a Python environment. It details command-line execution methods, including options for generating reports from Panorama, individual firewalls, or CSV files.

## Configuring and Executing `device-certificate-report`

### Executing Without Command-Line Arguments

You can start the script interactively by simply issuing `device-certificate-report` from your current working directory. The interactive shell will prompt you to input the required arguments, including whether to generate a report from Panorama, a firewall, or a CSV file.

<!-- termynal -->
```bash
$ device-certificate-report
```

### Executing With Command-Line Arguments

For a more streamlined approach, you can provide all necessary arguments directly via the command line:

<!-- termynal -->
```bash
$ device-certificate-report panorama --hostname <panorama_ip> --username <username> --password <password>
```

Or for CSV input:

<!-- termynal -->
```bash
$ device-certificate-report csv --csv-file <path_to_csv_file>
```

Or to connect directly to a firewall:

<!-- termynal -->
```bash
$ device-certificate-report firewall --hostname <firewall_ip> --username <username> --password <password>
```

## Command-Line Arguments

The `device-certificate-report` CLI supports various arguments to customize its execution. Here's an overview of the available options:

### Global Options

- `--help`: Show the help message and exit.

### Panorama Report Command

<!-- termynal -->
```bash
$ device-certificate-report panorama [OPTIONS]
```

Options:
- `--hostname TEXT`: Panorama IP address or hostname [optional]
- `--username TEXT`: Username for Panorama authentication [optional]
- `--password TEXT`: Password for Panorama authentication [optional]
- `--output-file TEXT`: Path to the output PDF report [default: device_certificate_report.pdf]

### Firewall Report Command

<!-- termynal -->
```bash
$ device-certificate-report firewall [OPTIONS]
```

Options:
- `--hostname TEXT`: Firewall IP address or hostname [optional]
- `--username TEXT`: Username for Firewall authentication [optional]
- `--password TEXT`: Password for Firewall authentication [optional]
- `--output-file TEXT`: Path to the output PDF report [default: <hostname>.pdf]

### CSV Report Command

<!-- termynal -->
```bash
$ device-certificate-report csv [OPTIONS]
```

Options:
- `--csv-file PATH`: Path to the input CSV file [optional]
- `--output-file TEXT`: Path to the output PDF report [default: device_certificate_report.pdf]

## Examples

### Generating a Report from Panorama

<!-- termynal -->
```bash
$ device-certificate-report panorama --hostname 192.168.1.1 --username admin --password admin123 --output-file panorama_report.pdf
```

### Generating a Report from CSV

<!-- termynal -->
```bash
$ device-certificate-report csv --csv-file ./device_list.csv --output-file csv_report.pdf
```

### Generating a Report from a Firewall

<!-- termynal -->
```bash
$ device-certificate-report firewall --hostname 192.168.1.20 --username admin --password admin123 --output-file firewall_report.pdf
```

## Output

The `device-certificate-report` tool generates a PDF report containing detailed information about device certificates, upgrade requirements, and recommendations. The report will be saved with the specified output file name.

## Troubleshooting

If you encounter any issues while running `device-certificate-report`, please check the following:

1. Ensure you have the latest version of the tool installed.
2. Verify that you have the necessary permissions to access Panorama, the firewall, or the input CSV file.
3. Check your network connection if connecting to Panorama or a firewall.
4. Review the error messages for any specific issues.

If problems persist, please open an issue on our GitHub repository with a detailed description of the problem and any relevant error messages.