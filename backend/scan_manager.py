import time
import json
import os

class ScanManager:
    scans = {}

    @classmethod
    def start_scan(cls, target, modules):
        scan_id = f"{target}-{int(time.time())}"
        cls.scans[scan_id] = {"target": target, "modules": modules, "status": "Running", "results": {}}
        return scan_id

    @classmethod
    def get_results(cls, scan_id):
        return cls.scans.get(scan_id, {"error": "Scan not found"})

    @classmethod
    def update_scan(cls, scan_id, results):
        if scan_id in cls.scans:
            cls.scans[scan_id]["results"] = results
            cls.scans[scan_id]["status"] = "Completed"
