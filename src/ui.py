import os
import time

# --- NEON COLORS ---
HEADER = "\033[95m"   # Magenta
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
WARNING = "\033[93m"  # Yellow
RESET = "\033[0m"

def display_task_card(index, total, proposal):
    """
    Displays a single task in a futuristic card format.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Visual Progress Bar
    progress_filled = "█" * (index + 1)
    progress_empty = "-" * (total - (index + 1))
    
    print(f"{HEADER}┌──────────────────────────────────────────────────┐{RESET}")
    print(f"{HEADER}│  MISSION PROGRESS: [{GREEN}{progress_filled}{progress_empty}{HEADER}] {index+1}/{total}     │{RESET}")
    print(f"{HEADER}└──────────────────────────────────────────────────┘{RESET}")
    print("")
    
    # Task Details
    print(f"{CYAN}:: OBJECTIVE ID :: {RESET} {proposal['command']}")
    print(f"{WARNING}:: CONSTRAINTS  :: {RESET} {proposal['constraint']}")
    print(f"{BLUE}:: VERIFICATION :: {RESET} {proposal['proof']}")
    print(f"\n{HEADER}────────────────────────────────────────────────────{RESET}")

def get_user_decision(valid_actions):
    """
    Loops until the user enters a valid command (approve/reject).
    """
    while True:
        user_input = input(f"{GREEN}>> AUTHORIZE? ({'/'.join(valid_actions)}): {RESET}").strip().lower()
        
        if user_input in valid_actions:
            return user_input
            
        print(f"{WARNING}>> ACCESS DENIED. INVALID INPUT.{RESET}")

def show_session_summary(duration, tasks_count):
    """
    Displays the end-of-session stats.
    """
    print(f"\n{GREEN}>> SESSION COMPLETE.{RESET}")
    print(f"   DURATION:     {duration}")
    print(f"   TASKS LOGGED: {tasks_count}")
    print(f"{CYAN}>> DATA ENCRYPTED AND SAVED TO DRIVE.{RESET}")
    input(f"\n{HEADER}[PRESS ENTER TO RETURN]{RESET}")

def show_logs(logs):
    """
    Formats and prints the JSON history log.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{CYAN}>> ACCESSING ARCHIVES...{RESET}\n")
    
    if not logs:
        print(f"{WARNING}>> NO RECORDS FOUND.{RESET}")
    else:
        # Loop reversed so newest sessions appear first
        for i, session in enumerate(reversed(logs)):
            print(f"{HEADER}╔══ SESSION RECORD {len(logs)-i} ═════════════════════════{RESET}")
            print(f"║ DATE: {session.get('login_time', 'N/A')}")
            print(f"║ DURATION: {session.get('session_duration', 'N/A')}")
            print(f"{HEADER}╟────────────────────────────────────────────────{RESET}")
            
            for action in session.get('activity_log', []):
                # Color code: Green for Approve, Yellow for Reject
                decision_color = GREEN if action['decision'] == 'APPROVE' else WARNING
                print(f"║ [{decision_color}{action['decision']}{RESET}] {action['command']}")
            
            print(f"{HEADER}╚════════════════════════════════════════════════{RESET}\n")
    
    input(f"{HEADER}[PRESS ENTER TO EXIT]{RESET}")