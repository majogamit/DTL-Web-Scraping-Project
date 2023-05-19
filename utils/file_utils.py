import os
import requests

from datetime import timedelta, datetime

import logging


def download_file(url, destination, date):
    """
    Downloads a file from the given URL and saves it to the specified destination.

    Args:
        url (str): The URL of the file to download.
        destination (str): The path where the downloaded file will be saved.
        date (str): The date associated with the file being downloaded.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful

        # Create the subfolders if they don't exist
        os.makedirs(os.path.dirname(destination), exist_ok=True)

        with open(destination, 'wb') as file:
            file.write(response.content)
        logging.info(f"{date}: Downloaded file from {url}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download file from {url}: {e}")


def download_files(base_url, download_path, date_index, date):
    """
    Downloads the required files from the website.

    Args:
        base_url (str): The base URL of the files to download.
        download_path (str): The path where the downloaded files will be saved.
        date_index (int): The index associated with the date.
        date (str): The date associated with the files being downloaded.
    """
    download_path = os.path.join(download_path, date)  # Add date as a subfolder

    # Check if the folder already exists and is complete
    if os.path.exists(download_path) and check_folder_complete(download_path, date):
        logging.info(f"{date}: Files are already downloaded.")
        return

    logging.info("Starting file download...")

    # List of files to download
    files_to_download = [
        ("WEBPXTICK_DT.zip", f"WEBPXTICK_DT-{date}.zip"),
        ("TickData_structure.dat", "TickData_structure.dat"),
        ("TC.txt", f"TC_{date}.txt"),
        ("TC_structure.dat", "TC_structure.dat")
    ]

    # Download each file
    for file_url, file_name in files_to_download:
        file_url = f"{base_url}/{date_index}/{file_url}"
        file_path = os.path.join(download_path, file_name)
        try:
            download_file(file_url, file_path, date)
        except Exception as e:
            logging.error(f"Failed to download file: {e}")
            continue
            raise

    logging.info("File download completed.")


def date_index(date):
    """
    Calculates the index associated with the date.

    Args:
        date (str): The date to calculate the index for.

    Returns:
        int: The index associated with the date.
    """
    try:
        start_date = datetime.strptime('2013-04-08', '%Y-%m-%d')
        end_date = datetime.strptime(date, '%Y-%m-%d')
        days_difference = (end_date - start_date).days
        weekdays = sum(1 for i in range(days_difference) if (start_date + timedelta(days=i)).weekday() < 5)
        return weekdays + 2756 + 28
    except (ValueError, TypeError) as e:
        logging.error(f"Failed to calculate date index: {e}")
        raise


def check_folder_complete(folder_path, date):
    """
    Checks if the folder contains all the required files.

    Args:
        folder_path (str): The path of the folder to check.
        date (str): The date associated with the files.

    Returns:
        bool: True if the folder is complete, False otherwise.
    """
    required_files = [
        f"WEBPXTICK_DT-{date}.zip",
        "TickData_structure.dat",
        f"TC_{date}.txt",
        "TC_structure.dat"
    ]

    for file_name in required_files:
        file_path = os.path.join(folder_path, file_name.format(date=date))
        if not os.path.exists(file_path):
            return False

    return True
