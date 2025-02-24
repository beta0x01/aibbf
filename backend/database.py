import json
import os

DB_FILE = "scan_history.json"

def load_scans():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    return {}

def save_scan(session_id, data):
    scans = load_scans()
    scans[session_id] = data
    with open(DB_FILE, "w") as file:
        json.dump(scans, file, indent=4)
