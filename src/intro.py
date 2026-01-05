import os
import sys
import time
import shutil

# ANSI colors (safe for Windows EXE)
RESET = "\033[0m"
DIM = "\033[2m"
CYAN = "\033[96m"
GREEN = "\033[92m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def center(text):
    width = shutil.get_terminal_size((80, 20)).columns
    return text.center(width)


def type_line(text, delay=0.015):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def boot_sequence():
    lines = [
        "Initializing secure environment",
        "Loading discipline scenarios",
        "Verifying audit integrity",
        "Mounting session logger",
        "AuthTrail system ready"
    ]

    for line in lines:
        type_line(center(DIM + "[ OK ] " + line + RESET))
        time.sleep(0.2)


def show_logo():
    logo = [
        " █████╗ ██╗   ██╗████████╗██╗  ██╗████████╗██████╗  █████╗ ██╗██╗     ",
        "██╔══██╗██║   ██║╚══██╔══╝██║  ██║╚══██╔══╝██╔══██╗██╔══██╗██║██║     ",
        "███████║██║   ██║   ██║   ███████║   ██║   ██████╔╝███████║██║██║     ",
        "██╔══██║██║   ██║   ██║   ██╔══██║   ██║   ██╔══██╗██╔══██║██║██║     ",
        "██║  ██║╚██████╔╝   ██║   ██║  ██║   ██║   ██║  ██║██║  ██║██║███████╗",
        "╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝",
    ]

    print()
    for line in logo:
        print(center(CYAN + line + RESET))
        time.sleep(0.04)

    print()
    print(center(GREEN + "Secure Authentication Trail System" + RESET))
    print(center(DIM + "Press Enter to continue..." + RESET))


def run_intro():
    clear_screen()
    boot_sequence()
    time.sleep(0.4)
    clear_screen()
    show_logo()
    input()
    clear_screen()


# Standalone test
if __name__ == "__main__":
    run_intro()
