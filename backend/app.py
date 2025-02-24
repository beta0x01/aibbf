from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO
import os
from scan_manager import ScanManager

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

scan_manager = ScanManager()

@app.route('/start_scan', methods=['POST'])
def start_scan():
    data = request.json
    target = data.get("target")
    modules = data.get("modules", ["All"])
    
    if not target:
        return jsonify({"error": "No target provided"}), 400
    
    session_id = scan_manager.start_scan(target, modules)
    return jsonify({"message": "Scan started", "session_id": session_id})

@app.route('/scan_status/<session_id>')
def scan_status(session_id):
    return jsonify(scan_manager.get_status(session_id))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8088, debug=True)
