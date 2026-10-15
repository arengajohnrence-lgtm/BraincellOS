# Shared Brain Cell

Operating Systems Final Project

Shared Brain Cell is a simple command-line operating system simulator written in Python. It runs in Windows Command Prompt (CMD). It does not boot a real system and does not control real hardware. It simulates a shell, a file system, processes, memory, user accounts, and system information.

## Group Members

| Name | Role |
| --- | --- |
| John Rence Arenga | Project Leader |
| Kian Chris Po | CLI Developer |
| Cj Sajonia | File Management Developer |
| Neil Sermeno | Process and Memory Developer |
| Kent Cedric Pacios | User and System Developer, Testing, and Documentation |

Group: Shared Brain Cells

## Member Contributions

John Rence Arenga, Project Leader
- Created the GitHub repository
- Coordinated the group and the deadlines
- Combined the code and checked the final version
- Submitted the project to Canvas

Kian Chris Po, CLI Developer
- Built main.py, the command prompt, and the command loop
- Built the help, clear, date, time, and exit commands

Cj Sajonia, File Management Developer
- Built filesystem.py
- Built the dir, mkdir, create, write, read, delete, and cd commands

Neil Sermeno, Process and Memory Developer
- Built processes.py and memory.py
- Built the run, process, kill, memory, allocate, and free commands

Kent Cedric Pacios, User and System Developer
- Built users.py and the login system
- Built the whoami and systeminfo commands
- Built the error handling
- Tested every command and helped write the documentation

## Project Description

Our program shows how the main parts of an operating system work together. A user logs in, types commands at the Shared Brain Cell prompt, and the system responds. Files, processes, and memory are all simulated inside the program.

## Features

- Command-line interface with its own prompt
- Help command
- Login system with two user accounts
- File management: dir, mkdir, create, write, read, delete, cd
- Process simulation: run, process, kill
- Memory simulation: memory, allocate, free
- System information
- Error handling for unknown commands, missing files, bad process IDs, and bad memory amounts
- Clean exit

## Requirements

- Python 3.x
- Windows CMD
- No outside libraries

## How to Run

1. Clone the repository.
2. Open CMD.
3. Go to the project folder.
4. Run:

```
python main.py
```

If Windows does not know the python command, run:

```
py main.py
```

## Login Accounts

| Username | Password |
| --- | --- |
| admin | admin123 |
| student | student123 |

You get three tries to log in.

## Available Commands

General

- help: shows all commands
- clear: clears the screen
- date: shows today's date
- time: shows the current time
- whoami: shows the logged-in user
- systeminfo: shows simulated system details
- exit: shuts down the system

File Management

- dir: lists files and folders in the current folder
- mkdir <folder>: creates a folder
- create <file>: creates an empty file
- write <file> <text>: saves text in a file
- read <file>: shows the content of a file
- delete <name>: deletes a file or an empty folder
- cd <folder>: opens a folder. Use cd .. to go back

Process Management

- run <name>: starts a simulated process and gives it a PID
- process: lists all running processes
- kill <pid>: ends a process

Memory Management

- memory: shows total, used, and free memory
- allocate <MB>: uses memory
- free <MB>: releases memory

## Example Session

```
MiniOS> mkdir Documents
Directory created.

MiniOS> create notes.txt
File created.

MiniOS> run calculator
Process started.

PID: 1
Name: calculator
Status: RUNNING

MiniOS> allocate 200
200 MB allocated.

MiniOS> hellooo
Unknown command.

Type 'help' to see the available commands.
```

## Project Structure

```
MiniOS/
├── main.py
├── users.py
├── filesystem.py
├── processes.py
├── memory.py
├── README.md
├── requirements.txt
├── docs/
├── screenshots/
└── individual-reports/
```

- main.py runs the command loop and sends each command to the right module
- users.py handles login
- filesystem.py simulates files and folders with nested dictionaries
- processes.py simulates a process table with PIDs
- memory.py tracks total, used, and free memory

## Documentation

- User Manual: docs/User_Manual.pdf
- Technical Documentation: docs/Technical_Documentation.pdf
- Screenshots: screenshots folder
- Individual reports: individual-reports folder
