#!/usr/bin/env python3
import os
import sys
from datetime import datetime, timedelta


def get_sprint_datetime():
    now = datetime.now()
    minutes = now.minute

    if minutes <= 15:
        sprint_minute = 0
    elif minutes <= 45:
        sprint_minute = 30
    else:
        # Move to next hour
        now += timedelta(hours=1)
        sprint_minute = 0

    sprint_time = now.replace(minute=sprint_minute, second=0, microsecond=0)
    # Example: "29 April, 2025 11:30 AM"
    formatted_time = sprint_time.strftime("%d %B, %Y %I:%M %p").lstrip("0")
    return formatted_time


def append_todo_block(file_path):
    sprint_datetime = get_sprint_datetime()
    todo_block = f"""

## [ ] CREATED AT {sprint_datetime}
## Task
## Evaluation
### Pros
### Cons
## Grade
## State
"""
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(todo_block)
        print(
            f"Successfully appended new sprint starting at {sprint_datetime} to {file_path}")
    except Exception as e:
        print(f"Error appending to {file_path}: {e}")


if __name__ == "__main__":
    # Get current year and month
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%B").lower()

    # Define the base directory
    base_dir = os.path.expanduser("~/Documents/30-min-lapse")

    # Create the base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Create directory for the year if it doesn't exist
    year_dir = os.path.join(base_dir, year)
    if not os.path.exists(year_dir):
        os.makedirs(year_dir)

    # Create file for the month if it doesn't exist
    file_path = os.path.join(year_dir, f"{month}.md")
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {month.capitalize()} {year}\n")

    # Append the todo block
    append_todo_block(file_path)
