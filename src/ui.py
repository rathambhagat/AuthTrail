import os
import shutil

# =========================
# ANSI COLOR DEFINITIONS
# =========================
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
INVERT = "\033[7m"

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"


# =========================
# TERMINAL HELPERS
# =========================
def clear():
    """Clear terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


def term_width(default=80):
    """Get terminal width safely"""
    return shutil.get_terminal_size((default, 20)).columns


def center(text):
    """Center text based on terminal width"""
    return text.center(term_width())


# =========================
# UI COMPONENTS
# =========================
def divider(char="─", color=DIM):
    """Horizontal divider"""
    print(color + char * term_width() + RESET)


def header(title, subtitle=None):
    """
    Draw a cyber-style header
    """
    clear()
    print(CYAN + center(f" {title} ") + RESET)
    divider()

    if subtitle:
        print(DIM + center(subtitle) + RESET)
        print()


def footer(text="READY | AuthTrail CLI"):
    """
    Draw footer status bar
    """
    print()
    divider()
    print(DIM + center(text) + RESET)


def boxed(text_lines, title=None, color=CYAN):
    """
    Draw a boxed panel with optional title
    """
    width = max(len(line) for line in text_lines) + 6
    top = "┌" + "─" * (width - 2) + "┐"
    bottom = "└" + "─" * (width - 2) + "┘"

    print(color + center(top) + RESET)

    if title:
        title_line = f" {title} "
        print(color + center(f"│{title_line.center(width - 2)}│") + RESET)

    for line in text_lines:
        print(color + center(f"│  {line.ljust(width - 6)}  │") + RESET)

    print(color + center(bottom) + RESET)


def menu_option(text, selected=False):
    """
    Render a menu option with highlight
    """
    if selected:
        return INVERT + f" ▶ {text} ".ljust(60) + RESET
    return f"   {text}"


def message(text, level="info"):
    """
    Styled messages
    """
    if level == "info":
        print(CYAN + text + RESET)
    elif level == "success":
        print(GREEN + text + RESET)
    elif level == "warning":
        print(YELLOW + text + RESET)
    elif level == "error":
        print(RED + text + RESET)
    else:
        print(text)


def prompt(text="Press Enter to continue..."):
    """
    Standard pause prompt
    """
    input(DIM + text + RESET)


# =========================
# BRAND ELEMENTS
# =========================
def brand_tagline():
    print(DIM + center("Secure Authentication Trail System") + RESET)


def version_bar(version="v1.0"):
    print(DIM + center(f"AuthTrail {version} | CLI MODE") + RESET)


# =========================
# STANDALONE PREVIEW
# =========================
if __name__ == "__main__":
    header("AUTHTRAIL", "Cyber Audit Interface")
    boxed(
        [
            "View Authentication Logs",
            "Search User Trails",
            "Export Audit Report",
            "Configuration",
            "Exit"
        ],
        title="MAIN MENU"
    )
    footer("READY | Awaiting Input")
