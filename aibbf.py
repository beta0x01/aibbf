import os
import argparse
import logging
import subprocess
import requests
import json
import threading
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup

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
    selected_modules = data.get("modules", [])
    domain = data.get("domain", "")
    api_keys = data.get("api_keys", {})
    return jsonify({"status": f"Scanning {domain} with {selected_modules}", "api_keys": api_keys})

# Run CLI Command
def run_command(command):
    """Executes a shell command and returns output."""
    try:
        return subprocess.getoutput(command).split("\n")
    except Exception as e:
        logging.error(f"Error executing command {command}: {e}")
        return []

# Main Function
def main():
    parser = argparse.ArgumentParser(description="Ultimate Bug Bounty Framework")
    parser.add_argument("-ui", action="store_true", help="Start the Web UI")
    parser.add_argument("-port", type=int, default=8088, help="Port for the Web UI (default: 8088)")
    parser.add_argument("-all", action="store_true", help="Run all modules")
    parser.add_argument("-m", "--modules", nargs="+", choices=MODULES.keys(), help="Select specific modules")
    
    # API Keys (Passed via CLI or Web UI)
    parser.add_argument("-shodan", help="Shodan API Key")
    parser.add_argument("-openai", help="OpenAI API Key")
    parser.add_argument("-qwen", help="Qwen API Key")
    parser.add_argument("-telegram", help="Telegram Bot Token")
    
    args = parser.parse_args()
    
    # Use provided API keys or fallback to environment variables
    shodan_api_key = args.shodan or os.getenv("SHODAN_API_KEY", "")
    openai_api_key = args.openai or os.getenv("OPENAI_API_KEY", "")
    qwen_api_key = args.qwen or os.getenv("QWEN_API_KEY", "")
    telegram_bot_token = args.telegram or os.getenv("TELEGRAM_BOT_TOKEN", "")
    
    if args.ui:
        print(f"🌐 Starting Web UI on http://localhost:{args.port}")
        threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": args.port, "debug": False}).start()
    else:
        print("\n🔥 Welcome to the Ultimate Bug Bounty Framework 🔥\n")
        print("📌 Select modules or run all with `-all`")
        print("🔹 Available Modules:")
        for key, value in MODULES.items():
            print(f"   ✅ {key}: {value}")

# Entry Point
if __name__ == "__main__":
    main()
