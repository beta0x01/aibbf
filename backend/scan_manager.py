import os
import uuid
import json
import threading

class ScanManager:
    def __init__(self):
        self.scans = {}
        self.results_dir = "../results"

    def create_scan(self, target, modules):
        scan_id = str(uuid.uuid4())
        scan_path = os.path.join(self.results_dir, f"{target}-{scan_id}")
        os.makedirs(scan_path, exist_ok=True)
        
        self.scans[scan_id] = {
            "target": target,
            "modules": modules,
            "status": "running",
            "path": scan_path
        }

        # Start scanning in a separate thread
        thread = threading.Thread(target=self.run_scan, args=(scan_id,))
        thread.start()
        return scan_id

    def run_scan(self, scan_id):
        scan_data = self.scans.get(scan_id)
        if not scan_data:
            return
        
        # Fake scanning process (replace with real modules)
        import time
        for i in range(5):
            time.sleep(2)
            scan_data["status"] = f"Running... {i * 20}%"
        
        scan_data["status"] = "Completed"
        
        # Save results (this is just a placeholder)
        with open(os.path.join(scan_data["path"], "results.json"), "w") as f:
            json.dump({"target": scan_data["target"], "status": "Completed"}, f)

    def get_status(self, scan_id):
        return self.scans.get(scan_id, {"status": "not found"})

    def cancel_scan(self, scan_id):
        if scan_id in self.scans:
            self.scans[scan_id]["status"] = "Cancelled"

    def save_scan(self, scan_id):
        # In real implementation, move results to permanent storage
        pass

    def discard_scan(self, scan_id):
        if scan_id in self.scans:
            scan_path = self.scans[scan_id]["path"]
            if os.path.exists(scan_path):
                os.rmdir(scan_path)
            del self.scans[scan_id]
