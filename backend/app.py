from flask import Flask, request, jsonify, send_from_directory
import os
import threading
from .scan_manager import ScanManager
from flask_socketio import SocketIO
from websocket_logs import stream_logs

socketio = SocketIO(app, cors_allowed_origins="*")


app = Flask(__name__)
scan_manager = ScanManager()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/start_scan", methods=["POST"])
def start_scan():
    target = request.form.get("target")
    modules = request.form.get("modules", "all").split(",")

    if not target:
        return jsonify({"error": "No target provided"}), 400

    scan_id = scan_manager.start_scan(target, modules)
    return jsonify({"message": f"Scan started for {target}", "scan_id": scan_id})

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    scan_id = scan_manager.start_scan(target, modules)
    thread = threading.Thread(target=stream_logs, args=(scan_id,))
    thread.start()
    return jsonify({"message": "File uploaded and scan started", "scan_id": scan_id})

@app.route("/get_history", methods=["GET"])
def get_history():
    return jsonify(scan_manager.get_scan_history())

@app.route("/results/<scan_id>", methods=["GET"])
def get_results(scan_id):
    return send_from_directory("results", f"{scan_id}.json", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=8088)
