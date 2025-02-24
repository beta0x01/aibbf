from flask import Flask, request, jsonify, send_from_directory
import os
import uuid
import json
from scan_manager import ScanManager

app = Flask(__name__)
scan_manager = ScanManager()

@app.route("/")
def home():
    return send_from_directory("../frontend/templates", "index.html")

@app.route("/api/start_scan", methods=["POST"])
def start_scan():
    data = request.json
    target = data.get("target")
    modules = data.get("modules", [])
    scan_id = scan_manager.create_scan(target, modules)
    return jsonify({"status": "started", "scan_id": scan_id})

@app.route("/api/scan_status/<scan_id>")
def scan_status(scan_id):
    status = scan_manager.get_status(scan_id)
    return jsonify(status)

@app.route("/api/cancel_scan/<scan_id>", methods=["POST"])
def cancel_scan(scan_id):
    scan_manager.cancel_scan(scan_id)
    return jsonify({"status": "cancelled"})

@app.route("/api/save_scan/<scan_id>", methods=["POST"])
def save_scan(scan_id):
    scan_manager.save_scan(scan_id)
    return jsonify({"status": "saved"})

@app.route("/api/discard_scan/<scan_id>", methods=["POST"])
def discard_scan(scan_id):
    scan_manager.discard_scan(scan_id)
    return jsonify({"status": "discarded"})

if __name__ == "__main__":
    app.run(debug=True, port=8088)
