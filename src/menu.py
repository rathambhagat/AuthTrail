import os
import sys
import time

# --- NEON COLORS ---
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def clear():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    """
    Displays the main options in a stylized box.
    Returns the user's choice ('1', '2', or '3').
    """
    while True:
        clear()
        
        # ASCII Box Design
        print(f"{CYAN}╔══════════════════════════════════════╗{RESET}")
        print(f"{CYAN}║         AUTHTRAIL CONTROL HUB        ║{RESET}")
        print(f"{CYAN}╠══════════════════════════════════════╣{RESET}")
        print(f"{CYAN}║{RESET}                                      {CYAN}║{RESET}")
        print(f"{CYAN}║{RESET}  1. {GREEN}INITIATE SESSION{RESET}               {CYAN}║{RESET}")
        print(f"{CYAN}║{RESET}  2. {YELLOW}ACCESS ARCHIVES (LOGS){RESET}         {CYAN}║{RESET}")
        print(f"{CYAN}║{RESET}  3. {GREEN}SYSTEM SHUTDOWN{RESET}                {CYAN}║{RESET}")
        print(f"{CYAN}║{RESET}                                      {CYAN}║{RESET}")
        print(f"{CYAN}╚══════════════════════════════════════╝{RESET}")
        
        # Input Prompt
        choice = input(f"\n{CYAN}>> AWAITING INPUT:{RESET} ").strip()
        
        if choice in ['1', '2', '3']:
            return choice
        else:
            print(f"{YELLOW}>> ERROR: INVALID COMMAND.{RESET}")
            time.sleep(1)