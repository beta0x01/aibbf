from flask_socketio import SocketIO
import time

socketio = SocketIO()

def stream_logs(scan_id):
    for i in range(1, 11):
        socketio.emit("scan_update", {"scan_id": scan_id, "message": f"Step {i}/10 completed..."})
        time.sleep(2)
    socketio.emit("scan_complete", {"scan_id": scan_id, "message": "Scan finished!"})
