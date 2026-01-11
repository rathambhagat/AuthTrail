import os
import sys
import json

# --- HELPER: GET PATH ---
# This ensures the logs are saved in the right place, 
# whether running as a script or an EXE.
def get_log_path():
    if getattr(sys, 'frozen', False):
        # If running as EXE
        application_path = os.path.dirname(sys.executable)
    else:
        # If running as Python script
        application_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    logs_folder = os.path.join(application_path, "logs")
    
    # Create logs folder if it doesn't exist
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)
        
    return os.path.join(logs_folder, "authtrail_sessions.json")

def log_session(session_data):
    """
    Reads existing logs, appends the new session, and saves it back.
    """
    try:
        log_path = get_log_path()
        full_log = []
        
        # Load existing data if file exists
        if os.path.exists(log_path):
            try:
                with open(log_path, "r") as file:
                    full_log = json.load(file)
            except (json.JSONDecodeError, ValueError):
                full_log = []

        # Add new data
        full_log.append(session_data)

        # Write back to file
        with open(log_path, "w") as file:
            json.dump(full_log, file, indent=4)
            
        return True
    except Exception as e:
        print(f"[ERROR] Session Logging failed: {e}")
        return False

def get_all_logs():
    """
    Returns the full list of past sessions.
    """
    try:
        log_path = get_log_path()
        if os.path.exists(log_path):
            with open(log_path, "r") as file:
                return json.load(file)
        return []
    except Exception:
        return []