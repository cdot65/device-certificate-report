# Python Setup and Execution Guide for device-certificate-report

This guide provides comprehensive steps for configuring and executing the `device-certificate-report` package within a Python environment. It details command-line execution methods, including options for generating reports from Panorama or CSV files.

## Configuring and Executing `device-certificate-report`

### Executing Without Command-Line Arguments

You can start the script interactively by simply issuing `device-certificate-report` from your current working directory. The interactive shell will prompt you to input the required arguments, including whether to generate a report from Panorama or a CSV file.

```bash
$ device-certificate-report
```

### Executing With Command-Line Arguments

For a more streamlined approach, you can provide all necessary arguments directly via the command line:

```bash
$ device-certificate-report panorama --hostname <panorama_ip> --username <username> --password <password>
```

Or for CSV input:

```bash
$ device-certificate-report csv --file <path_to_csv_file>
```

## Command-Line Arguments

The `device-certificate-report` CLI supports various arguments to customize its execution. Here's an overview of the available options:

### Global Options

- `--help`: Show the help message and exit.
- `--version`: Show the version and exit.

### Panorama Report Command

```bash
$ device-certificate-report panorama [OPTIONS]
```

Options:
- `--hostname TEXT`: Panorama IP address or hostname [required]
- `--username TEXT`: Username for Panorama authentication [required]
- `--password TEXT`: Password for Panorama authentication [required]
- `--port INTEGER`: Port number for Panorama connection [default: 443]
- `--output-dir PATH`: Directory to save the generated reports [default: ./output]

### CSV Report Command

```bash
$ device-certificate-report csv [OPTIONS]
```

Options:
- `--file PATH`: Path to the input CSV file [required]
- `--output-dir PATH`: Directory to save the generated reports [default: ./output]

## Examples

### Generating a Report from Panorama

```bash
$ device-certificate-report panorama --hostname 192.168.1.1 --username admin --password admin123 --output-dir ./my_reports
```

### Generating a Report from CSV

```bash
$ device-certificate-report csv --file ./device_list.csv --output-dir ./my_reports
```

## Output

The `device-certificate-report` tool generates two types of reports:

1. A PDF report containing detailed information about device certificates, upgrade requirements, and recommendations.
2. A CSV file summarizing the key findings and actions required for each device.

Both reports will be saved in the specified output directory (or the default ./output directory if not specified).

## Troubleshooting

If you encounter any issues while running `device-certificate-report`, please check the following:

1. Ensure you have the latest version of the tool installed.
2. Verify that you have the necessary permissions to access Panorama or the input CSV file.
3. Check your network connection if connecting to Panorama.
4. Review the error messages for any specific issues.

If problems persist, please open an issue on our GitHub repository with a detailed description of the problem and any relevant error messages.