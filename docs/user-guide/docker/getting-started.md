# Getting Started with device-certificate-report using Docker

Welcome to the Docker-based workflow of the `device-certificate-report` library! This guide will help you set up and use the `device-certificate-report` tool within a Docker container. This approach is ideal for users who prefer a containerized environment or who are not as familiar with Python environments.

## Prerequisites

Before starting, make sure you have:

- Docker installed on your system. Visit the [Docker installation guide](https://docs.docker.com/get-docker/) for instructions.
- Access to a Palo Alto Networks Panorama appliance or a CSV file with device information.
- An active internet connection for pulling the Docker image.

## Pulling the Docker Image

The `device-certificate-report` Docker image is hosted on GitHub Packages. Pull the image using the following command:

<div class="termy">

<!-- termynal -->
```bash
$ docker pull ghcr.io/cdot65/device-certificate-report:latest
```

</div>

## Building the Docker Image

As an alternative, if you would like to build the container yourself:

1. Clone the repository:

   <div class="termy">
   
   <!-- termynal -->
   ```bash
   $ git clone https://github.com/cdot65/device-certificate-report.git
   $ cd device-certificate-report
   ```
   
   </div>

2. Navigate to the `docker` directory:

   <div class="termy">

   <!-- termynal -->
   ```bash
   $ cd docker
   ```
   
   </div>

3. Build your custom image:

   <div class="termy">

   <!-- termynal -->
   ```bash
   $ docker build -t device-certificate-report:custom .
   ```

   </div>

You can modify the Dockerfile to your liking before building.

## Next Steps

With the Docker container set up and ready, you can begin using the `device-certificate-report` tool to generate certificate reports for your PAN-OS devices. For detailed configuration instructions and usage examples, proceed to the [Docker Execution Guide](execution.md).

This guide will show you how to:

- Run the container to generate reports from Panorama
- Use the container with a CSV input file
- Customize the execution with various command-line options
- Access and interpret the generated reports