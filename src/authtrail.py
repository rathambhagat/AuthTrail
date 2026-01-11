import sys
import os
import datetime

# 1. SETUP PATHS (Essential for the EXE to work later)
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(bundle_dir)

# 2. IMPORTS
# We import the other 5 files here.
# If these files don't exist yet, this script will crash (that is normal for now).
import config
import logger
import intro
import menu
import ui

def run_discipline_mode():
    """
    The core logic loop:
    1. Gets tasks from config.
    2. Uses UI to show them.
    3. Saves result to logger.
    """
    start_time = datetime.datetime.now()
    session_actions = []
    
    # Iterate through every task in the config list
    for index, proposal in enumerate(config.SCENARIOS):
        # UI: Show the card
        ui.display_task_card(index, len(config.SCENARIOS), proposal)
        
        # UI: Get valid input
        decision = ui.get_user_decision(config.VALID_ACTIONS)
        
        # Record the action
        action_entry = {
            "command": proposal['command'],
            "decision": decision.upper(),
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        session_actions.append(action_entry)

    # End Session
    end_time = datetime.datetime.now()
    duration = str(end_time - start_time).split('.')[0]
    
    # Prepare Data Packet
    full_report = {
        "login_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "logout_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
        "session_duration": duration,
        "total_tasks_attempted": len(session_actions),
        "activity_log": session_actions
    }
    
    # Save to JSON
    logger.log_session(full_report)
    
    # Show Summary Screen
    ui.show_session_summary(duration, len(session_actions))

def main():
    """
    The Main Program Flow
    """
    # Step 1: Play the Intro Animation
    intro.play_intro()

    # Step 2: Show the Menu Loop
    while True:
        choice = menu.show_main_menu()
        
        if choice == '1':
            run_discipline_mode()
        elif choice == '2':
            # Fetch logs and show them
            logs = logger.get_all_logs()
            ui.show_logs(logs)
        elif choice == '3':
            # Clean Exit
            print("\nShutting down system...")
            sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[SYSTEM FORCE QUIT]")