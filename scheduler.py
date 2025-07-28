# This is a basic loop scheduler; in production use Airflow or cron jobs.
import time
import subprocess

while True:
    subprocess.run(['python', 'scripts/fetch_api_data.py'])
    subprocess.run(['python', 'scripts/transform_data.py'])
    print("Cycle completed. Sleeping for 15 minutes...")
    time.sleep(900)  # Sleep for 15 mins
