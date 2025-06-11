from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import sys
print("schedule_runner.py started...")
scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', minutes=1)  # For testing
def auto_update():
    print("Running scheduled task: auto_update_tasks")
    try:
        result = subprocess.run(
            [sys.executable, "manage.py", "auto_update_tasks"],
            capture_output=True,
            text=True,
            check=True
        )
        print("Task Completed:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("error:\n", e.stderr)

scheduler.start()