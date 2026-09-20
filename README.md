# Deadline Manager

A simple Python CLI project designed to help students manage assignments, track deadlines, and organize tasks based on priority.

## Features

- Add new assignments
- View pending assignments
- View completed assignments
- Mark assignments as done
- Update days remaining and priority
- Delete assignments
- Set priority as HIGH, MED, or LOW
- Automatically highlight urgent assignments
- Save assignments locally for future use

## Technologies Used

- Python
- Functions
- Lists and Dictionaries
- Loops
- Conditional statements
- File handling
- User input
- Python modules
- Classes and objects

## Requirements

Python 3.x

No external libraries are required.

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:

```bash
python main.py
```

4. Select an option from the menu and follow the instructions.

## Project Files

- `main.py` - Main program and menu
- `tracker.py` - Handles assignment operations
- `storage.py` - Saves and loads assignment data
- `assignments.txt` - Stores assignment information
- `README.md` - Project documentation

## Data Storage

Assignment data is stored locally in `assignments.txt`, including the course, title, days remaining, priority, and completion status.

Assignments with **2 or fewer days remaining** are marked as `[URGENT!]`.

## Future Improvements

- Add assignment IDs
- Add due dates
- Add search and sorting
- Use JSON or a database for storage
- Add a graphical interface

## Author

Devank Mutreja
