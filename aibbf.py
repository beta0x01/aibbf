import os
import argparse
import logging
import subprocess
import requests
import json
import threading
from flask import Flask, render_template, request, jsonify

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Flask App for Web UI
app = Flask(__name__)

# Available Modules
MODULES = {
    "recon": "Subdomain Enumeration, WHOIS, DNS, ASN Lookup",
    "web": "API Security, WAF Detection, WebSockets, GraphQL, XSS, SQLi",
    "cloud": "AWS/GCP/Azure Misconfiguration Testing",
    "network": "Firewall Detection, SSRF Mapping, Port Scanning",
    "exploitation": "AI-Powered Exploitation & Payload Crafting",
}

# Flask Routes
@app.route("/")
def home():
    return render_template("index.html", modules=MODULES)

@app.route("/start_scan", methods=["POST"])
def start_scan():
    data = request.json
    selected_modules = data.get("modules", list(MODULES.keys()))  # Default: Run ALL modules
    domain = data.get("domain", "")
    return jsonify({"status": f"Scanning {domain} with {selected_modules}"})

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    domains = file.read().decode("utf-8").splitlines()
    return jsonify({"domains": domains})

# Main Function
def main():
    parser = argparse.ArgumentParser(description="Ultimate Bug Bounty Framework")
    parser.add_argument("-ui", action="store_true", help="Start the Web UI")
    parser.add_argument("-port", type=int, default=8088, help="Port for the Web UI (default: 8088)")
    parser.add_argument("-all", action="store_true", help="Run all modules by default")
    args = parser.parse_args()
    
    if args.ui:
        print(f"🌐 Starting Web UI on http://localhost:{args.port}")
        threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": args.port, "debug": False}).start()
    else:
        print("\n🔥 Welcome to the Ultimate Bug Bounty Framework 🔥\n")
        print("📌 Default mode: Running ALL modules (Use `-ui` for Web UI)")
        print("🔹 Available Modules:")
        for key, value in MODULES.items():
            print(f"   ✅ {key}: {value}")

# Entry Point
if __name__ == "__main__":
    main()
