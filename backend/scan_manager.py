import threading
import time

class ScanManager:
    def __init__(self):
        self.scans = {}

    def start_scan(self, target, modules):
        session_id = str(int(time.time()))
        self.scans[session_id] = {"target": target, "modules": modules, "status": "Running"}
        
        thread = threading.Thread(target=self.run_scan, args=(session_id,))
        thread.start()
        
        return session_id

    def run_scan(self, session_id):
        time.sleep(5)  # Simulate scanning time
        self.scans[session_id]["status"] = "Completed"

    def get_status(self, session_id):
        return self.scans.get(session_id, {"error": "Session not found"})
