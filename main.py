import os
import sys
from datetime import datetime

from users import login
from filesystem import FileSystem
from processes import ProcessManager
from memory import MemoryManager

OS_NAME = "Shared Brain Cell"
VERSION = "1.0"

COMMANDS = [
    "help", "clear", "date", "time", "whoami", "systeminfo", "exit",
    "dir", "mkdir", "create", "write", "read", "delete", "cd",
    "process", "run", "kill",
    "memory", "allocate", "free",
]


def banner():
    print("=" * 40)
    print(f"          {OS_NAME.upper()} v{VERSION}")
    print("=" * 40)
    print("\nWelcome to MiniOS!\n")


def need_arg(args, usage):
    if not args:
        print(f"Error: Missing argument. Usage: {usage}")
        return False
    return True


def to_int(text):
    try:
        return int(text)
    except ValueError:
        print("Error: Please enter a whole number.")
        return None


def main():
    user = login()
    if user is None:
        return
    fs, procs, mem = FileSystem(), ProcessManager(), MemoryManager()
    banner()

    while True:
        try:
            line = input(f"MiniOS{fs.location() if fs.path else ''}> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            line = "exit"
        if not line:
            continue
        parts = line.split()
        cmd, args = parts[0].lower(), parts[1:]

        if cmd == "help":
            print("\nAvailable Commands:\n")
            for c in COMMANDS:
                print(" ", c)
            print()
        elif cmd == "clear":
            os.system("cls" if os.name == "nt" else "clear")
        elif cmd == "date":
            print(datetime.now().strftime("%Y-%m-%d"))
        elif cmd == "time":
            print(datetime.now().strftime("%H:%M:%S"))
        elif cmd == "whoami":
            print(f"Current User: {user}")
        elif cmd == "systeminfo":
            print("=" * 40)
            print("          SYSTEM INFORMATION")
            print("=" * 40)
            print(f"\nOS Name: {OS_NAME}")
            print(f"Version: {VERSION}")
            print("Architecture: 64-bit")
            print("CPU: Virtual CPU")
            print(f"Memory: {mem.total} MB")
            print(f"User: {user}\n")
            print("=" * 40)
        elif cmd == "exit":
            print("Shutting down MiniOS...\n")
            print("Goodbye!")
            break
        elif cmd == "dir":
            print("\n".join(fs.dir()))
        elif cmd == "mkdir":
            if need_arg(args, "mkdir <folder>"):
                print(fs.mkdir(args[0]))
        elif cmd == "create":
            if need_arg(args, "create <file>"):
                print(fs.create(args[0]))
        elif cmd == "write":
            if need_arg(args, "write <file> <text>"):
                print(fs.write(args[0], " ".join(args[1:])))
        elif cmd == "read":
            if need_arg(args, "read <file>"):
                print(fs.read(args[0]))
        elif cmd == "delete":
            if need_arg(args, "delete <name>"):
                print(fs.delete(args[0]))
        elif cmd == "cd":
            if need_arg(args, "cd <folder> or cd .."):
                msg = fs.cd(args[0])
                if msg:
                    print(msg)
        elif cmd == "process":
            print("\n".join(procs.listing()))
        elif cmd == "run":
            if need_arg(args, "run <name>"):
                pid = procs.run(args[0])
                print("Process started.\n")
                print(f"PID: {pid}")
                print(f"Name: {args[0]}")
                print("Status: RUNNING")
        elif cmd == "kill":
            if need_arg(args, "kill <pid>"):
                pid = to_int(args[0])
                if pid is not None:
                    if procs.kill(pid):
                        print(f"Process {pid} terminated.")
                    else:
                        print("Error: Process does not exist.")
        elif cmd == "memory":
            print("\n".join(mem.status()))
        elif cmd == "allocate":
            if need_arg(args, "allocate <MB>"):
                n = to_int(args[0])
                if n is not None:
                    print(mem.allocate(n))
        elif cmd == "free":
            if need_arg(args, "free <MB>"):
                n = to_int(args[0])
                if n is not None:
                    print(mem.release(n))
        else:
            print("Unknown command.\n")
            print("Type 'help' to see the available commands.")


if __name__ == "__main__":
    main()
