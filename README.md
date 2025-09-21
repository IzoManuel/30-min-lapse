# 30-min-lapse
- A light weight md-based todo "app"?

# Linux: Installation
1. Make the script executable: Run the following command to make the script executable:

```chmod +x /<path-to>/append_todo.py```

2. Add the script to your PATH: You can create a symbolic link to the script in a directory that is already in your PATH, such as bin. Run the following command:

```sudo ln -s "/<path-to>/append_todo.py" /usr/local/bin/append_todo```

3. Run the script from anywhere: Now you can run the script from anywhere using the command:

```append_todo```

- Optionally add a topic when running the command

```append_todo "Finish Adding a Button"```


# Directory path for created MD files
- A directory is created on running the command `~/Documents/30-min-lapse`
- Current year is retrieved and concatenated into the directory `~/Documents/30-min-lapse/2025/`
- Current month is retrieved and created MD file is named after the month `~/Documents/30-min-lapse/2025/may.md`

# Customisations
- Edit the append_todo.py script to modify the template or directory structure