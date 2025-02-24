from flask import Flask, request, jsonify, send_file
from flask_socketio import SocketIO
from scan_manager import ScanManager
from js_analyzer import analyze_target
from auth import auth_blueprint
from database import db
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "super_secret_key"

socketio = SocketIO(app, cors_allowed_origins="*")

# Register Authentication Routes
app.register_blueprint(auth_blueprint, url_prefix="/auth")

# Initialize DB
db.init_app(app)

@app.route("/start_scan", methods=["POST"])
def start_scan():
    data = request.get_json()
    target = data.get("target")
    modules = data.get("modules", ["All"])

    if not target:
        return jsonify({"error": "No target provided"}), 400

    scan_id = ScanManager.start_scan(target, modules)
    return jsonify({"message": "Scan started", "scan_id": scan_id}), 200

@app.route("/get_results/<scan_id>", methods=["GET"])
def get_results(scan_id):
    results = ScanManager.get_results(scan_id)
    return jsonify(results), 200

@app.route("/analyze_js", methods=["POST"])
def analyze_js():
    target = request.form.get("target")
    if not target:
        return jsonify({"error": "No target provided"}), 400

    analysis_result = analyze_target(target)
    return jsonify(analysis_result)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
