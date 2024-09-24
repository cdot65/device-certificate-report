# device_certificate_report/components/pdf_generation.py

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
import importlib.resources as pkg_resources


def generate_report(
    unaffected_devices: List[DeviceInfo],
    no_upgrade_required: List[DeviceInfo],
    upgrade_required: List[DeviceInfo],
    devices_with_globalprotect: List[DeviceInfo],
    devices_with_certificates: List[DeviceInfo],
    output_file: str,
):
    """
    Generate a PDF report based on the collected device information.
    """
    pdf = SimpleDocTemplate(output_file, pagesize=letter)
    content = []
    styles = getSampleStyleSheet()

    # Optional: Include a logo if available
    try:
        logo_path = pkg_resources.files("device_certificate_report.assets").joinpath(
            "logo.png"
        )
        img = Image(str(logo_path), width=71, height=51)
        img.hAlign = "LEFT"
        content.append(img)
        content.append(Spacer(1, 12))
    except (FileNotFoundError, ModuleNotFoundError):
        # If the logo is not found, continue without it
        pass

    # Title and styling
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

    # Function to create a table for a list of devices
    def create_device_table(
        devices: List[DeviceInfo], headers: List[str], fields: List[str]
    ) -> Table:
        table_data = [headers]
        for device in devices:
            row = [getattr(device, field) or "" for field in fields]
            table_data.append(row)
        col_count = len(headers)
        # Set column widths to evenly divide the page width
        page_width = letter[0] - pdf.leftMargin - pdf.rightMargin
        col_width = page_width / col_count
        col_widths = [col_width] * col_count

        table = Table(table_data, colWidths=col_widths, repeatRows=1)
        # Apply styling
        table_style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F04E23")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ]
        )
        # Alternate row colors
        for i in range(1, len(table_data)):
            bg_color = colors.whitesmoke if i % 2 == 0 else colors.white
            table_style.add("BACKGROUND", (0, i), (-1, i), bg_color)
        table.setStyle(table_style)
        return table

    # Unaffected Devices
    content.append(
        Paragraph(
            "Unaffected Models (already supports Device Certificates)",
            styles["Heading2"],
        )
    )
    content.append(Spacer(1, 12))
    if unaffected_devices:
        headers = ["Device Name", "Model", "Software Version"]
        fields = ["device_name", "model", "software_version"]
        table = create_device_table(unaffected_devices, headers, fields)
        content.append(table)
        content.append(Spacer(1, 20))
    else:
        content.append(Paragraph("No unaffected devices.", styles["BodyText"]))
        content.append(Spacer(1, 20))

    # Affected Devices - No Software Upgrade Required
    content.append(
        Paragraph("Affected Models (No Software Upgrade Required)", styles["Heading2"])
    )
    content.append(Spacer(1, 12))
    if no_upgrade_required:
        headers = ["Device Name", "Model", "Software Version"]
        fields = ["device_name", "model", "software_version"]
        table = create_device_table(no_upgrade_required, headers, fields)
        content.append(table)
        content.append(Spacer(1, 20))
    else:
        content.append(
            Paragraph("No affected devices that are up-to-date.", styles["BodyText"])
        )
        content.append(Spacer(1, 20))

    # Affected Devices - Software Upgrade Required
    content.append(
        Paragraph("Affected Models (Software Upgrade Required)", styles["Heading2"])
    )
    content.append(Spacer(1, 12))
    if upgrade_required:
        headers = [
            "Device Name",
            "Model",
            "Software Version",
            "Minimum Version",
        ]
        fields = [
            "device_name",
            "model",
            "software_version",
            "min_required_version",
        ]
        table = create_device_table(upgrade_required, headers, fields)
        content.append(table)
        content.append(Spacer(1, 20))
    else:
        content.append(
            Paragraph(
                "No affected devices that require software upgrade.", styles["BodyText"]
            )
        )
        content.append(Spacer(1, 20))

    # Devices with GlobalProtect Clients
    content.append(Paragraph("Devices with GlobalProtect Clients", styles["Heading2"]))
    content.append(Spacer(1, 12))
    if devices_with_globalprotect:
        headers = ["Device Name", "Model", "Software Version", "GlobalProtect Client"]
        fields = ["device_name", "model", "software_version", "globalprotect_client"]
        table = create_device_table(devices_with_globalprotect, headers, fields)
        content.append(table)
        content.append(Spacer(1, 20))
    else:
        content.append(
            Paragraph("No devices with GlobalProtect clients.", styles["BodyText"])
        )
        content.append(Spacer(1, 20))

    # Device Certificate Status and Expiry
    content.append(
        Paragraph("Device Certificate Status and Expiry", styles["Heading2"])
    )
    content.append(Spacer(1, 12))
    if devices_with_certificates:
        headers = [
            "Device Name",
            "Model",
            "Device Certificate Status",
            "Certificate Expiry Date",
        ]
        fields = [
            "device_name",
            "model",
            "device_certificate",
            "device_certificate_expiry_date",
        ]
        table = create_device_table(devices_with_certificates, headers, fields)
        content.append(table)
        content.append(Spacer(1, 20))
    else:
        content.append(
            Paragraph(
                "No device certificate information available.", styles["BodyText"]
            )
        )
        content.append(Spacer(1, 20))

    # Build the PDF
    pdf.build(content)
