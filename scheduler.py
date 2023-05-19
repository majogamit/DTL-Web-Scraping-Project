import schedule
import time
import subprocess
import argparse

def run_process():
    subprocess.run(['python', 'main.py'])

def schedule_job(time_str):
    schedule.every().day.at(time_str).do(run_process)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scheduler Configuration')
    parser.add_argument('--time', type=str, help='Preferred time to run the code in HH:MM format')

    args = parser.parse_args()

    if args.time:
        schedule_job(args.time)
    else:
        print("Please provide a preferred time using the --time argument (HH:MM format)")

    while True:
        schedule.run_pending()
        time.sleep(1)
