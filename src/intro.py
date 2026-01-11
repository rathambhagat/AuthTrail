import sys
import time
import os
import random

# --- NEON COLORS (ANSI Codes) ---
CYAN = "\033[96m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"

def clear():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, color=WHITE, speed=0.03):
    """Prints text one character at a time like a hacker terminal."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET + "\n")

def glitch_text(text, duration=1.5):
    """Simulates a decoding/glitch effect."""
    end_time = time.time() + duration
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&*"
    
    while time.time() < end_time:
        scrambled = "".join(random.choice(chars) for _ in range(len(text)))
        sys.stdout.write(f"\r{MAGENTA}{scrambled}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    
    # Final Reveal
    sys.stdout.write(f"\r{CYAN}{text}{RESET}\n")
    sys.stdout.flush()
    time.sleep(0.5)

def play_intro():
    """Runs the full intro sequence."""
    clear()
    time.sleep(0.5)
    
    # 1. Loading Bar
    print(f"{GREEN}[SYSTEM BOOT SEQUENCE_]{RESET}")
    for i in range(25):
        time.sleep(0.03)
        sys.stdout.write(f"{GREEN}█{RESET}")
        sys.stdout.flush()
    print("\n")

    # 2. System Messages
    type_effect(">> INITIALIZING KERNEL...", GREEN, 0.03)
    type_effect(">> LOADING MODULES: LOGIC, DATA, UI...", GREEN, 0.03)
    type_effect(">> BYPASSING SECURITY PROTOCOLS...", MAGENTA, 0.03)
    time.sleep(0.5)
    clear()

    # 3. The ASCII Logo (Using raw string 'r' to prevent errors)
    logo = r"""
       _    _   _ _____ _   _ _____ ____      _    ___ _     
      / \  | | | |_   _| | | |_   _|  _ \    / \  |_ _| |    
     / _ \ | | | | | | | |_| | | | | |_) |  / _ \  | || |    
    / ___ \| |_| | | | |  _  | | | |  _ <  / ___ \ | || |___ 
   /_/   \_\___/  |_| |_| |_| |_| |_| \_\/_/   \_\___|_____|
    """
    
    # Print Logo with a scanning effect
    for line in logo.split("\n"):
        print(f"{CYAN}{line}{RESET}")
        time.sleep(0.1)

    print("\n")
    
    # 4. Final Glitch Welcome
    glitch_text("   SYSTEM READY. WELCOME USER.", duration=1.2)
    time.sleep(1)