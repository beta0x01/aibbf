import os
import argparse
import threading
from backend.app.py import app
from backend.scan_manager.py import ScanManager

def start_web_ui(port):
    """Starts the Flask Web UI"""
    print(f"🌐 Web UI is running on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)

def start_cli():
    """Starts CLI Mode"""
    print("\n🔥 Welcome to the Ultimate Bug Bounty Framework 🔥")
    print("📌 Type a domain to scan or use `-ui` for Web UI mode.")
    
    scan_manager = ScanManager()
    target = input("\n🎯 Enter target domain: ").strip()
    
    if not target:
        print("❌ No target entered. Exiting...")
        return

    print("\n🔹 Available Modules:")
    print("  1️⃣ Reconnaissance")
    print("  2️⃣ Web Security")
    print("  3️⃣ Cloud Security")
    print("  4️⃣ Network Security")
    print("  5️⃣ Exploitation")
    print("  🟢 (Leave blank to run all modules)")

    modules = input("👉 Select modules (comma-separated, or press ENTER for all): ").strip()
    if modules:
        modules = [m.strip() for m in modules.split(",")]
    else:
        modules = ["recon", "web", "cloud", "network", "exploitation"]

    scan_id = scan_manager.create_scan(target, modules)
    print(f"\n🚀 Scan started! Scan ID: {scan_id}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ultimate Bug Bounty Framework")
    parser.add_argument("-ui", action="store_true", help="Start the Web UI")
    parser.add_argument("-port", type=int, default=8088, help="Port for Web UI (default: 8088)")
    args = parser.parse_args()

    if args.ui:
        threading.Thread(target=start_web_ui, args=(args.port,)).start()
    else:
        start_cli()
