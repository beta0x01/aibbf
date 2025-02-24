import os
from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO
from gevent import pywsgi
from scan_manager import ScanManager

app = Flask(__name__, static_folder="../frontend", static_url_path="/")
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="gevent")

scan_manager = ScanManager()

# 🔹 Serve Frontend (Fix for "Not Found" Error)
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

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
    server = pywsgi.WSGIServer(("0.0.0.0", 8088), app)
    print("🔥 Server running at http://localhost:8088")
    server.serve_forever()
