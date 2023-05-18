# DTL Data Team Mini-project

This is a Python script designed to download specific files from the SGX website (https://www.sgx.com/research-education/derivatives). The script is intented to download daily derivative data files and provide options to include historical files or only download the latest file. The downloaded files are saved to the specified destination folder, and logging is implemented to track the download progress and debug any issues.

This is a part of an internship screening process, and the code and its documentation are intended solely for evaluation purposes.

## Requirements
The project uses Python 3.11.3.

To install the required dependencies for this project, you can use the provided `requirements.txt` file. Make sure you have Python and pip installed on your system, and then follow these steps:

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv myenv
   ```

2. Activate the virtual environment:
   - For Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

3. Install the dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

This will install all the required packages and their specific versions as listed in the `requirements.txt` file.

Please note that the versions specified in the `requirements.txt` file are frozen at the time of project submission. It is recommended to verify and update the dependencies as necessary to ensure compatibility with your specific Python environment.

## Usage

The script can be run using command line options or by providing a config file.

### Command Line Options

Use the following command line options to configure the file download:

- `--include-latest`: Include the latest file in the download (yesterday's date).
- `--date [DATE]`: Download files for the specified date(s) in the format YYYY-MM-DD. Multiple dates can be provided.
- `--start-date [START_DATE] --end-date [END_DATE]`: Download files for a range of dates, inclusive. The dates should be specified in the format YYYY-MM-DD.

Example usages:

- Download only the latest file:
  ```
  python main.py --include-latest
  ```

- Download files for a specific date:
  ```
  python main.py --date 2023-05-17
  ```

- Download files for a multiple specific date:
  ```
  python main.py --date 2022-01-17 2023-03-27
  ```

- Download files for a range of dates:
  ```
  python main.py --start-date 2023-05-15 --end-date 2023-05-17
  ```

## Project Structure

The project structure is organized as follows:

```
- main.py
- utils/
    - __init__.py
    - logging_utils.py
    - file_utils.py
- downloads/
    - __init__.py
```

- `main.py` contains the main execution logic of the script and handles command line arguments.
- `utils/logging_utils.py` provides a function to set up logging configurations for the script.
- `utils/file_utils.py` contains utility functions for downloading files, checking folders, and calculating date indices.
- `downloads/` is the default destination folder where the downloaded files will be saved.

## Logging

The script uses the built-in logging module provided by Python for flexible logging configurations. It logs messages with timestamps and levels to aid in debugging and issue resolution. The logs are saved to both the console (stdout) and a log file (`download.log`) in the current working directory.


# To do

[] Include explanation about dates that are already downloaded
[] files that are checked and are missing, download whole set of files for that date again 
[] for downloading ranges, checks if the date is a weekend or not. but take note that only until 2021 is correct for index computation.
[] Download log is implemented but the same shows up in terminal
[] downloading process involved looking at the direct link for download to access historical files.
[] the redownloading process is automatic 
