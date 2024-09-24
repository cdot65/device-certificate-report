# device_certificate_report/components/cleaner.py

import re
import csv


def clean_html_tags(text: str):
    """
    :param text: The input string that may contain HTML tags and extraneous characters.
    :return: A cleaned string with HTML tags removed, extra quotes and semicolons normalized, and leading/trailing whitespace stripped.
    """
    # Remove all HTML tags
    cleaned = re.sub(r"<[^>]+>", "", text)
    # Remove extra quotes and semicolons that might have been introduced
    cleaned = re.sub(r'";+"', ";", cleaned)
    cleaned = re.sub(r'"+', '"', cleaned)
    # Remove any leading/trailing whitespace
    return cleaned.strip()


def clean_csv(
    input_file: str,
    output_file: str,
):
    """
    :param input_file: Path to the input CSV file that needs to be cleaned.
    :param output_file: Path to the output CSV file where the cleaned data will be saved.
    :return: None
    """
    with open(
        input_file,
        "r",
        newline="",
        encoding="utf-8-sig",
    ) as infile, open(
        output_file,
        "w",
        newline="",
        encoding="utf-8",
    ) as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            cleaned_row = [clean_html_tags(cell) for cell in row]
            writer.writerow(cleaned_row)
