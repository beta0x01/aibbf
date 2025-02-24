import os
import argparse
import logging
import subprocess
import requests
import json
import threading
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup

# AI Imports (Optional)
try:
    import openai
except ImportError:
    openai = None

try:
    import dashscope  # Qwen API
except ImportError:
    dashscope = None

try:
    import telebot  # Telegram API
except ImportError:
    telebot = None

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# API Keys (Optional)
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
QWEN_API_KEY = os.getenv("QWEN_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# Initialize AI and Telegram (if API keys are provided)
if openai and OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

if telebot and TELEGRAM_BOT_TOKEN:
    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Flask App for Web UI
app = Flask(__name__)

# List of modules
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
    selected_modules = request.json.get("modules", [])
    domain = request.json.get("domain", "")
    return jsonify({"status": "Scanning started for " + domain, "modules": selected_modules})

# AI Analysis Function
def analyze_with_ai(prompt, content):
    """Tries OpenAI first, then falls back to Qwen if OpenAI fails."""
    if openai and OPENAI_API_KEY:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": prompt}, {"role": "user", "content": content}],
            )
            return response["choices"][0]["message"]["content"]
        except Exception as openai_error:
            logging.warning(f"OpenAI failed: {openai_error}")

    if dashscope and QWEN_API_KEY:
        try:
            response = dashscope.Generation.call(
                model="qwen-max",
                messages=[{"role": "system", "content": prompt}, {"role": "user", "content": content}],
                api_key=QWEN_API_KEY,
            )
            return response["output"]["text"]
        except Exception as qwen_error:
            logging.error(f"Both OpenAI and Qwen failed: {qwen_error}")

    return "AI analysis failed."

# Main Function
def main():
    parser = argparse.ArgumentParser(description="Ultimate Bug Bounty Framework")
    parser.add_argument("-ui", action="store_true", help="Start the Web UI")
    parser.add_argument("-port", type=int, default=8088, help="Port for the Web UI (default: 8088)")
    parser.add_argument("-all", action="store_true", help="Run all modules")
    parser.add_argument("-m", "--modules", nargs="+", choices=MODULES.keys(), help="Select specific modules")
    args = parser.parse_args()

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
