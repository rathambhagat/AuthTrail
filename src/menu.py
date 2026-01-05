import os
import sys
import time

# ANSI styling (simple + safe)
RESET = "\033[0m"
INVERT = "\033[7m"
DIM = "\033[2m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_key():
    """Cross-platform single key input"""
    if os.name == "nt":
        import msvcrt
        return msvcrt.getch().decode("utf-8", errors="ignore")
    else:
        import termios, tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


MENU_ITEMS = [
    "Start Command Session",
    "View Previous Logs",
    "Exit"
]


def draw_menu(selected):
    clear_screen()
    print(CYAN + " AUTHTRAIL MANAGEMENT CONSOLE ".center(50, "#") + RESET)
    print(DIM + " Use ↑ ↓ or W S • Enter to select • Esc to quit\n" + RESET)

    for index, item in enumerate(MENU_ITEMS):
        if index == selected:
            print(INVERT + f" ▶ {item}".ljust(40) + RESET)
        else:
            print(f"   {item}")

    print(DIM + "\nStatus: READY" + RESET)


def run_menu(start_session_fn, view_history_fn):
    """
    Receives existing functions from authtrail.py
    """
    selected = 0

    while True:
        draw_menu(selected)
        key = get_key()

        # W / S navigation
        if key.lower() == "w":
            selected = (selected - 1) % len(MENU_ITEMS)
        elif key.lower() == "s":
            selected = (selected + 1) % len(MENU_ITEMS)

        # Arrow keys (Windows)
        elif key == "\xe0":
            arrow = get_key()
            if arrow == "H":  # Up
                selected = (selected - 1) % len(MENU_ITEMS)
            elif arrow == "P":  # Down
                selected = (selected + 1) % len(MENU_ITEMS)

        # Enter
        elif key == "\r":
            clear_screen()

            if selected == 0:
                start_session_fn()
            elif selected == 1:
                view_history_fn()
            elif selected == 2:
                print(RED + "Exiting AuthTrail..." + RESET)
                time.sleep(0.8)
                sys.exit(0)

        # ESC
        elif key == "\x1b":
            clear_screen()
            print(RED + "AuthTrail terminated by user." + RESET)
            time.sleep(0.8)
            sys.exit(0)
