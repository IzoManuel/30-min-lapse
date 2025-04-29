import sys
from datetime import datetime, timedelta

def get_sprint_time():
    now = datetime.now()
    minutes = now.minute

    if minutes <= 15:
        sprint_minute = 0
    elif minutes <= 45:
        sprint_minute = 30
    else:
        # move to next hour
        now += timedelta(hours=1)
        sprint_minute = 0

    sprint_time = now.replace(minute=sprint_minute, second=0, microsecond=0)
    return sprint_time.strftime("%I:%M %p").lstrip("0")  # Format like "11:00 AM", without leading 0

def append_todo_block(file_path):
    sprint_time = get_sprint_time()
    todo_block = f"""

## [ ] FROM {sprint_time}
## Task
## Evaluation
## Grade
## State
"""
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(todo_block)
        print(f"Successfully appended new sprint starting at {sprint_time} to {file_path}")
    except Exception as e:
        print(f"Error appending to {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python append_todo.py <path_to_md_file>")
    else:
        file_path = sys.argv[1]
        append_todo_block(file_path)
