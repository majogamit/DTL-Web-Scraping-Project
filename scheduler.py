import schedule
import time
import subprocess
import argparse

def run_process():
    try:
        subprocess.run(['python', 'main.py'])
    except Exception as e:
        print(f"Error running the process: {e}")

def schedule_job(time_str):
    try:
        schedule.every().day.at(time_str).do(run_process)
    except Exception as e:
        print(f"Error scheduling the job: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scheduler Configuration')
    parser.add_argument('--time', type=str, help='Preferred time to run the code in HH:MM format')

    args = parser.parse_args()

    if args.time:
        schedule_job(args.time)
    else:
        print("Please provide a preferred time using the --time argument (HH:MM format)")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped by user")
    except Exception as e:
        print(f"An error occurred: {e}")
