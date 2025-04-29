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
    
## [ ] FROM {sprint_datetime}
## Task
## Evaluation
## Grade
## State
"""
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(todo_block)
        print(f"Successfully appended new sprint starting at {sprint_datetime} to {file_path}")
    except Exception as e:
        print(f"Error appending to {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python append_todo.py <path_to_md_file>")
    else:
        file_path = sys.argv[1]
        append_todo_block(file_path)
