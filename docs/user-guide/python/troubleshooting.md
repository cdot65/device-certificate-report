# Troubleshooting Guide for device-certificate-report

Encountering issues while using the `device-certificate-report` tool is not uncommon, especially when dealing with complex network environments and certificate management. This guide provides troubleshooting steps for common problems you might face during the report generation process, including connections through Panorama.

## Common Issues and Solutions

### 1. Connection Issues

**Problem:** The script fails to connect to the Panorama device.

**Solution:** Ensure that the Panorama's hostname/IP and credentials are correct. Verify network connectivity and accessibility. Check firewall rules and ensure the necessary ports are open.

### 2. CSV File Issues

**Problem:** The script fails to process the provided CSV file.

**Solution:** Verify the CSV file format and content. Ensure it follows the expected structure and contains all required fields. Check for any special characters or formatting issues that might cause parsing errors.

### 3. Report Generation Failures

**Problem:** The script stops during the report generation process.

**Solution:** Check the Panorama and network settings. Make sure Panorama is responding correctly. Review the logs in the `logs/` directory for specific error messages.

### 4. Script Hangs

**Problem:** The script hangs or does not progress.

**Solution:** Interrupt the script (Ctrl+C) and check the log files for any clues. Common issues might be network latency or Panorama response delays.

### 5. Incorrect Certificate Information

**Problem:** The generated report contains incorrect or outdated certificate information.

**Solution:** Verify that Panorama has the most up-to-date information from the managed firewalls. Ensure that the firewalls are properly connected and synced with Panorama.

### 6. PDF Generation Issues

**Problem:** The script fails to generate the PDF report.

**Solution:** Check if the required PDF generation libraries are properly installed. Ensure there's enough disk space for report generation. Verify permissions for writing to the output directory.

### 7. Incomplete Device Information

**Problem:** The report is missing information for some devices.

**Solution:** Check the connectivity between Panorama and the managed firewalls. Verify that all devices are properly registered and communicating with Panorama.

### 8. Version Compatibility Issues

**Problem:** The script reports incompatibility with certain PAN-OS versions.

**Solution:** Ensure that the `device-certificate-report` tool is up-to-date and compatible with the PAN-OS versions in your environment. Check the documentation for supported versions.

### 9. Memory Issues

**Problem:** The script runs out of memory when processing a large number of devices.

**Solution:** Consider running the script on a machine with more RAM. If possible, process the devices in smaller batches or optimize the script's memory usage.

### 10. API Rate Limiting

**Problem:** The script encounters API rate limiting errors when querying Panorama.

**Solution:** Implement backoff and retry logic in the script. Consider adding delays between API calls or reducing the concurrency of requests if processing multiple devices simultaneously.

## General Tips

- Always ensure you're using the latest version of the `device-certificate-report` tool.
- Keep Panorama and managed firewalls updated to the latest compatible versions.
- Review the `logs/` directory for detailed logs if any issues arise.
- For large environments, consider running the script in batches to manage resource usage and troubleshoot more effectively.

## Reporting Issues

If you encounter an issue not covered in this guide, please report it on the [issues page](https://github.com/cdot65/device-certificate-report/issues) of our GitHub repository. Provide detailed information including log excerpts, Panorama version, managed firewall models and versions, and any relevant configuration details to help diagnose the problem.