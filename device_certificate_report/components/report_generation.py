# components/report_generation.py

from typing import List
from device_certificate_report.models.device import DeviceInfo
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Line
from pathlib import Path
import importlib.resources as pkg_resources


def generate_report(devices: List[DeviceInfo], output_file: str):
    """
    Generate a PDF report based on the collected device information.

    Parameters
    ----------
    devices : List[DeviceInfo]
        A list of device information.
    output_file : str
        Path to the output PDF file.
    """
    pdf = SimpleDocTemplate(output_file, pagesize=letter)
    content = []
    styles = getSampleStyleSheet()

    # Optional: Include a logo if available
    # Assuming you have a logo.png in a package called 'assets'
    try:
        logo_path = pkg_resources.files("device_certificate_report.assets").joinpath("logo.png")
        img = Image(str(logo_path), width=71, height=51)
        img.hAlign = "LEFT"
        content.append(img)
        content.append(Spacer(1, 12))
    except FileNotFoundError:
        # If the logo is not found, continue without it
        pass

    # Add a title
    title_style = styles["Title"]
    title_style.fontSize = 24
    title_style.textColor = colors.HexColor("#333333")
    title_style.alignment = 1  # Center alignment
    title = Paragraph("Device Certificate Report", title_style)
    content.append(title)
    content.append(Spacer(1, 20))

    # Line separator
    d = Drawing(500, 1)
    line = Line(0, 0, 500, 0)
    line.strokeColor = colors.HexColor("#F04E23")
    line.strokeWidth = 2
    d.add(line)
    content.append(d)
    content.append(Spacer(1, 20))

    # Prepare table data
    # Define table headers
    table_data = [
        [
            "Device Name",
            "Virtual System",
            "Model",
            "Serial Number",
            "IPv4 Address",
            "Device State",
            "Device Certificate",
            "Certificate Expiry Date",
            "Software Version",
            "GlobalProtect Client",
        ]
    ]

    # Add device data to the table
    for device in devices:
        row = [
            device.device_name or "",
            device.virtual_system or "",
            device.model or "",
            device.serial_number or "",
            device.ipv4_address or "",
            device.device_state or "",
            device.device_certificate or "",
            device.device_certificate_expiry_date or "",
            device.software_version or "",
            device.globalprotect_client or "",
        ]
        table_data.append(row)

    # Create the table
    table = Table(table_data, repeatRows=1)
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F04E23")),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # Grid lines
    ])

    # Alternate row colors
    for i, _ in enumerate(table_data[1:], start=1):
        bg_color = colors.whitesmoke if i % 2 == 0 else colors.white
        table_style.add('BACKGROUND', (0, i), (-1, i), bg_color)

    table.setStyle(table_style)

    content.append(table)
    content.append(Spacer(1, 20))

    # Build the PDF
    pdf.build(content)