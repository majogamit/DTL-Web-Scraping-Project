import argparse
from datetime import timedelta, datetime
import os
import logging

from utils.logging_utils import setup_logging
from utils.file_utils import download_file, download_files, date_index, check_folder_complete


def main():
    """
    The main function that handles the command line arguments and initiates the file download.
    """

    # Parsing command line arguments
    try:
        parser = argparse.ArgumentParser(description='File Downloader')
        parser.add_argument('--include-latest', action='store_true',
                            help='Include the latest file in the download (yesterday\'s date)')
        parser.add_argument('--date', nargs='+', required=False, help='Date in the format YYYY-MM-DD')
        parser.add_argument('--start-date', required=False, help='Start date in the format YYYY-MM-DD')
        parser.add_argument('--end-date', required=False, help='End date in the format YYYY-MM-DD')

        args = parser.parse_args()

        # Setting up base URL, download path, and other variables
        base_url = 'https://links.sgx.com/1.0.0/derivatives-historical'
        download_path = 'downloads'
        include_latest = args.include_latest
        date = args.date

        if args.start_date and args.end_date:
            try:
                start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
                end_date = datetime.strptime(args.end_date, '%Y-%m-%d')
                # Generating a list of dates between start date and end date
                dates = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end_date - start_date).days + 1)]
            except (ValueError, TypeError) as e:
                logging.error(f"Invalid start or end date: {e}")
                return
        elif date is None:
            # If date is not provided, use yesterday's date
            dates = [(datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")]
        else:
            dates = date

        for date in dates:
            # Check if the date is a weekday
            if datetime.strptime(date, '%Y-%m-%d').weekday() < 5:
                try:
                    # convert into the index of the date
                    date_indexs = date_index(date)  
                    # download the required files from specified dates
                    download_files(base_url, download_path, date_indexs, date)
                except Exception as e:
                    logging.error(f"Failed to download files for {date}: {e}")
                    continue
            else:
                logging.warning(f"{date} is not a weekday. Skipping file download.")

        if include_latest:
            try:
                # include most recent file
                yesterday_date = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")  
                # convert date of latest to index
                date_index_yesterday = date_index(yesterday_date) 
                # if the indices are not similar, proceed to download the yesterday files
                if date_index_yesterday != date_indexs:  
                    download_files(base_url, download_path, date_index_yesterday, yesterday_date)
            except Exception as e:
                logging.error(f"Failed to download files for {yesterday_date}: {e}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    setup_logging(log_to_stdout=True, log_to_file=True)
    main()
