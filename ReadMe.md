# DTL Data Team Mini-project

This is a Python script designed to download specific files from the SGX website (https://www.sgx.com/research-education/derivatives). The script is intended to download daily derivative data files and provide options to include historical files or only download the latest file. The downloaded files are saved to the specified destination folder, and logging is implemented to track the download progress and debug any issues.

This is a part of an internship screening process, and the code and its documentation are intended solely for evaluation purposes.

## Requirements
This project uses:
- [Python 3.11.3](https://www.python.org/downloads/)
- [pip 22.3.1](https://pip.pypa.io/en/stable/installation/)
- [Requests 2.30.0](https://pypi.org/project/requests/)
- [schedule 1.2.0](https://pypi.org/project/schedule/)

To install the required dependencies for this project, use pip and the provided `requirements.txt` file:
  ```bash
   pip install -r requirements.txt
   ```

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

- Download files for multiple specific dates:
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

## Scheduler

The script uses the 'schedule' library in Python to schedule the execution of the download process at a specific time every day. The scheduling logic is in the file 'scheduler.py' file.  
Here is a sample usage if the  program needs to be executed everyday at a certain time:

1. Run the script using the following command:
   ```
   python scheduler.py --time <HH:MM>
   ```
   Replace `<HH:MM>` with your preferred time in the 24-hour format.
   
   For example, to schedule the job to run at 09:30, use:
   ```
   python scheduler.py --time 09:30
   ```
   
   Note: If you don't provide the `--time` argument, the script will prompt you to enter a preferred time.
2. The script will schedule the job to run at the specified time using the `schedule` library.
3. The script will continuously check for pending jobs and run them accordingly.
4. To stop the script, press `Ctrl + C`.

## Additional

 Features

The project includes the following additional features:

- **Checking for Existing Files**: The script checks if the specified date folder already exists in the destination folder. If it exists, the script further checks if all the files for that date have already been downloaded. If all the files are downloaded, the script skips the download process for that date. However, if any file is missing, the script downloads the entire set of files in that folder again.

- **Weekend Date Handling**: For downloading files within a range of dates, the script checks if each date falls on a weekend or not. Please note that the date index computation is only an approximation from the dates April 2013 until present.

- **Download Log**: The script implements a download log, which is displayed in the terminal. It provides information about the progress of the download, including the files being downloaded.








