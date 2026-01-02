import sys
import os
import time
import datetime
import traceback

# --- PATH FIX ---
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(bundle_dir)

# --- IMPORTS ---
try:
    from config import SCENARIOS, VALID_ACTIONS
    from logger import log_session, get_all_logs
except ImportError:
    print("CRITICAL ERROR: Could not import config or logger.")
    input("Press Enter to exit...")
    sys.exit()

# ==========================================
# OPTION 1: START COMMAND SESSION
# ==========================================
def start_session():
    start_time = datetime.datetime.now()
    session_actions = [] 

    print("\n==========================================")
    print("      AUTHTRAIL DISCIPLINE SESSION        ")
    print(f"      Started: {start_time.strftime('%H:%M:%S')}")
    print("==========================================\n")

    try:
        for index, proposal in enumerate(SCENARIOS):
            print(f"--- TASK {index + 1} OF {len(SCENARIOS)} -----------------------")
            print(f"COMMAND:    {proposal['command']}")
            print(f"CONSTRAINT: {proposal['constraint']}")
            print(f"PROOF:      {proposal['proof']}")
            
            while True:
                user_input = input(f"DECISION ({'/'.join(VALID_ACTIONS)}): ").strip().lower()

                if user_input in VALID_ACTIONS:
                    print("Logged.\n")
                    action_entry = {
                        "command": proposal['command'],
                        "decision": user_input.upper(),
                        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    session_actions.append(action_entry)
                    break 
                else:
                    print(f"> Error: Please use {VALID_ACTIONS}\n")

        # Session Finished
        end_time = datetime.datetime.now()
        duration = str(end_time - start_time).split('.')[0]

        print("==========================================")
        print("      SESSION COMPLETE. SAVING...         ")
        print("==========================================")

        full_report = {
            "login_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "logout_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "session_duration": duration,
            "total_tasks_attempted": len(session_actions),
            "activity_log": session_actions
        }
        log_session(full_report)
        print("[SUCCESS] Data saved secureley.")
        input("\nPress Enter to return to menu...")

    except KeyboardInterrupt:
        print("\nSession cancelled.")

# ==========================================
# OPTION 2: VIEW PREVIOUS LOGS
# ==========================================
def view_history():
    logs = get_all_logs()
    
    print("\n==========================================")
    print(f"      PAST SESSION LOGS ({len(logs)} Found)")
    print("==========================================")

    if not logs:
        print("No history found yet. Go do some work!")
    else:
        # Loop through logs in reverse order (newest first)
        for i, session in enumerate(reversed(logs)):
            print(f"\n[SESSION {len(logs)-i}] - Date: {session.get('login_time', 'N/A')}")
            print(f"Duration: {session.get('session_duration', 'N/A')}")
            print("-" * 40)
            
            for action in session.get('activity_log', []):
                # Format:  [APPROVE]  WAKE_UP_EARLY
                print(f"  [{action['decision']}]  {action['command']}")
            print("-" * 40)
    
    input("\nPress Enter to return to menu...")

# ==========================================
# MAIN MENU LOOP
# ==========================================
def main_menu():
    while True:
        # Clear screen command (cls for Windows, clear for others)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n##########################################")
        print("      AUTHTRAIL MANAGEMENT CONSOLE        ")
        print("##########################################")
        print("1. Start Command Session")
        print("2. View Previous Logs")
        print("3. Exit")
        print("------------------------------------------")
        
        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            start_session()
        elif choice == '2':
            view_history()
        elif choice == '3':
            print("Exiting...")
            time.sleep(1)
            sys.exit()
        else:
            print("Invalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()