import uuid
import json
import os
import threading
import time

RESULTS_FOLDER = "results"
os.makedirs(RESULTS_FOLDER, exist_ok=True)

class ScanManager:
    def __init__(self):
        self.scans = {}

    def start_scan(self, target, modules):
        scan_id = str(uuid.uuid4())
        scan_data = {"id": scan_id, "target": target, "modules": modules, "status": "Running", "result": ""}
        self.scans[scan_id] = scan_data

        thread = threading.Thread(target=self.run_scan, args=(scan_id,))
        thread.start()
        return scan_id

    def run_scan(self, scan_id):
        scan = self.scans[scan_id]
        time.sleep(5)  # Simulating scan process

        # Generate results
        result_path = os.path.join(RESULTS_FOLDER, f"{scan_id}.json")
        with open(result_path, "w") as f:
            json.dump({"target": scan["target"], "modules": scan["modules"], "status": "Completed"}, f)

        scan["status"] = "Completed"
        scan["result"] = result_path

    def get_scan_history(self):
        return list(self.scans.values())
