import os
import sys
import json

# --- HELPER: GET PATH ---
def get_log_path():
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    logs_folder = os.path.join(application_path, "logs")
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)
        
    return os.path.join(logs_folder, "authtrail_sessions.json")

def log_session(session_data):
    """ Writes a new session to the JSON file. """
    try:
        log_path = get_log_path()
        full_log = []
        
        if os.path.exists(log_path):
            try:
                with open(log_path, "r") as file:
                    full_log = json.load(file)
            except (json.JSONDecodeError, ValueError):
                full_log = []

        full_log.append(session_data)

        with open(log_path, "w") as file:
            json.dump(full_log, file, indent=4)
        return True
    except Exception as e:
        print(f"[ERROR] Session Logging failed: {e}")
        return False

def get_all_logs():
    """ Reads all sessions from the JSON file. """
    try:
        log_path = get_log_path()
        if os.path.exists(log_path):
            with open(log_path, "r") as file:
                return json.load(file)
        return []
    except Exception:
        return []