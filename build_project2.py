import os
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Lenovo\Desktop\Projects\Realtime-Video-Sensor-Dashboard")
(BASE_DIR / "templates").mkdir(parents=True, exist_ok=True)
(BASE_DIR / "static").mkdir(parents=True, exist_ok=True)

SENSORS_PY = '''"""
Telemetry simulation module modeling realistic hardware environmental and ultrasonic sensors.
"""
import random
import time
try:
    import psutil
except ImportError:
    psutil = None

_temp = 24.5
_humidity = 52.0
_distance = 85.0


def generate_telemetry() -> dict:
    """Generates drifting realistic telemetry readings."""
    global _temp, _humidity, _distance

    # Random walk simulation
    _temp += random.uniform(-0.3, 0.3)
    _temp = max(18.0, min(38.0, _temp))

    _humidity += random.uniform(-0.8, 0.8)
    _humidity = max(35.0, min(80.0, _humidity))

    _distance += random.uniform(-4.0, 4.0)
    _distance = max(15.0, min(250.0, _distance))

    if psutil:
        cpu = psutil.cpu_percent(interval=None)
    else:
        cpu = round(random.uniform(15.0, 65.0), 1)

    return {
        "temperature": round(_temp, 2),
        "humidity": round(_humidity, 1),
        "distance_cm": round(_distance, 1),
        "cpu_load": round(cpu, 1),
        "timestamp": time.strftime("%H:%M:%S")
    }
'''

APP_PY = '''"""
Real-Time Video & Sensor Streaming Dashboard
Flask + OpenCV + Socket.IO server.
"""
import time
import io
from flask import Flask, render_template, Response, jsonify
from flask_socketio import SocketIO
from sensors import generate_telemetry

try:
    import cv2
except ImportError:
    cv2 = None

try:
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np
except ImportError:
    Image = None

app = Flask(__name__)
app.config["SECRET_KEY"] = "abdullah-telecom-telemetry-key"
socketio = SocketIO(app, cors_allowed_origins="*")

camera = None
if cv2 is not None:
    try:
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            camera = None
    except Exception:
        camera = None


def generate_synthetic_frame() -> bytes:
    """Generates a dynamic placeholder video frame when no hardware camera is present."""
    width, height = 640, 480
    if Image is not None:
        img = Image.new("RGB", (width, height), color=(18, 22, 34))
        draw = ImageDraw.Draw(img)

        # Draw grid
        for x in range(0, width, 40):
            draw.line([(x, 0), (x, height)], fill=(30, 40, 60), width=1)
        for y in range(0, height, 40):
            draw.line([(0, y), (width, y)], fill=(30, 40, 60), width=1)

        # Crosshair
        cx, cy = width // 2, height // 2
        draw.line([(cx - 30, cy), (cx + 30, cy)], fill=(0, 212, 255), width=2)
        draw.line([(cx, cy - 30), (cx, cy + 30)], fill=(0, 212, 255), width=2)
        draw.ellipse([(cx - 20, cy - 20), (cx + 20, cy + 20)], outline=(0, 212, 255), width=2)

        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        draw.text((20, 20), "TELEMETRY VIDEO STREAM [EMULATED LIVE]", fill=(0, 255, 170))
        draw.text((20, 45), f"TIMESTAMP: {ts}", fill=(200, 200, 220))
        draw.text((20, 440), "Edge AI Object Tracking: Standby", fill=(255, 180, 0))

        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=80)
        return buffer.getvalue()
    else:
        # Fallback raw JPEG minimal header
        return b""


def get_frame() -> bytes:
    """Acquires frame from hardware camera or synthesizes one."""
    if camera and camera.isOpened():
        success, frame = camera.read()
        if success:
            ret, buffer = cv2.imencode(".jpg", frame)
            if ret:
                return buffer.tobytes()
    return generate_synthetic_frame()


def gen_frames():
    """MJPEG streaming generator."""
    while True:
        frame_bytes = get_frame()
        yield (b"--frame\\r\\n"
               b"Content-Type: image/jpeg\\r\\n\\r\\n" + frame_bytes + b"\\r\\n")
        time.sleep(0.06)  # ~16 FPS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/telemetry")
def telemetry_api():
    return jsonify(generate_telemetry())


def telemetry_broadcaster():
    """Background task pushing live telemetry to connected WebSocket clients."""
    while True:
        data = generate_telemetry()
        socketio.emit("telemetry_update", data)
        socketio.sleep(1.0)


@socketio.on("connect")
def on_connect():
    print("[*] Dashboard client connected.")


if __name__ == "__main__":
    socketio.start_background_task(telemetry_broadcaster)
    print("==================================================================")
    print("  Real-Time Video Sensor Streaming Dashboard")
    print("  Access dashboard in browser at: http://localhost:5000")
    print("==================================================================")
    socketio.run(app, host="0.0.0.0", port=5000, debug=False, allow_unsafe_werkzeug=True)
'''

INDEX_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-Time Video & Sensor Telemetry Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
    <style>
        :root {
            --bg-color: #0d1117;
            --panel-bg: #161b22;
            --border-color: #30363d;
            --accent-cyan: #00d4ff;
            --accent-green: #3fb950;
            --accent-orange: #f0883e;
            --text-primary: #f0f6fc;
            --text-muted: #8b949e;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            padding: 20px;
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 20px;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 20px;
        }
        h1 { font-size: 1.4rem; font-weight: 600; }
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            color: var(--text-muted);
            background: var(--panel-bg);
            padding: 6px 14px;
            border-radius: 20px;
            border: 1px solid var(--border-color);
        }
        .dot {
            width: 10px; height: 10px;
            border-radius: 50%;
            background: var(--accent-green);
            box-shadow: 0 0 8px var(--accent-green);
        }
        .grid-container {
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 20px;
        }
        .card {
            background: var(--panel-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px;
            overflow: hidden;
        }
        .card-title {
            font-size: 0.95rem;
            color: var(--text-muted);
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .video-wrapper {
            position: relative;
            width: 100%;
            aspect-ratio: 4/3;
            background: #000;
            border-radius: 8px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .video-wrapper img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-bottom: 16px;
        }
        .metric-tile {
            background: #0d1117;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 14px;
        }
        .metric-label { font-size: 0.8rem; color: var(--text-muted); }
        .metric-val {
            font-size: 1.8rem;
            font-weight: 700;
            margin-top: 4px;
            color: var(--accent-cyan);
        }
        .metric-unit { font-size: 0.9rem; color: var(--text-muted); font-weight: normal; }
        .chart-box {
            background: #0d1117;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 12px;
            height: 200px;
        }
    </style>
</head>
<body>
    <header>
        <div>
            <h1>Telemetry & Video Streaming Dashboard</h1>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Hardware Telemetry | Low-Latency MJPEG Stream</div>
        </div>
        <div class="status-badge">
            <div class="dot" id="status-dot"></div>
            <span id="status-text">Connected</span>
        </div>
    </header>

    <div class="grid-container">
        <!-- Video Stream Column -->
        <div class="card">
            <div class="card-title">Live Camera Stream</div>
            <div class="video-wrapper">
                <img src="/video_feed" alt="Video Stream" onerror="this.src=\'data:image/svg+xml;utf8,<svg xmlns=\\\'http://www.w3.org/2000/svg\\\' width=\\\'640\\\' height=\\\'480\\\'><rect width=\\\'640\\\' height=\\\'480\\\' fill=\\\'#121622\\\'/><text x=\\\'50%\\\' y=\\\'50%\\\' fill=\\\'#8b949e\\\' dominant-baseline=\\\'middle\\\' text-anchor=\\\'middle\\\'>Hardware Camera Offline</text></svg>\'">
            </div>
        </div>

        <!-- Telemetry & Charts Column -->
        <div class="card">
            <div class="card-title">Sensor Telemetry</div>
            <div class="metrics-grid">
                <div class="metric-tile">
                    <div class="metric-label">Ambient Temperature</div>
                    <div class="metric-val" id="val-temp">-- <span class="metric-unit">°C</span></div>
                </div>
                <div class="metric-tile">
                    <div class="metric-label">Relative Humidity</div>
                    <div class="metric-val" id="val-humidity">-- <span class="metric-unit">%</span></div>
                </div>
                <div class="metric-tile">
                    <div class="metric-label">Ultrasonic Range</div>
                    <div class="metric-val" id="val-distance" style="color: var(--accent-green)">-- <span class="metric-unit">cm</span></div>
                </div>
                <div class="metric-tile">
                    <div class="metric-label">System CPU Load</div>
                    <div class="metric-val" id="val-cpu" style="color: var(--accent-orange)">-- <span class="metric-unit">%</span></div>
                </div>
            </div>

            <div class="card-title" style="margin-top: 8px;">Temperature History (Live 30s Window)</div>
            <div class="chart-box">
                <canvas id="tempChart"></canvas>
            </div>
        </div>
    </div>

    <script>
        const ctx = document.getElementById("tempChart").getContext("2d");
        const maxPoints = 30;
        const tempChart = new Chart(ctx, {
            type: "line",
            data: {
                labels: [],
                datasets: [{
                    label: "Temperature (°C)",
                    data: [],
                    borderColor: "#00d4ff",
                    backgroundColor: "rgba(0, 212, 255, 0.1)",
                    borderWidth: 2,
                    fill: true,
                    tension: 0.3,
                    pointRadius: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { display: false },
                    y: {
                        grid: { color: "#21262d" },
                        ticks: { color: "#8b949e" }
                    }
                },
                plugins: {
                    legend: { display: false }
                }
            }
        });

        const socket = io();
        socket.on("connect", () => {
            document.getElementById("status-dot").style.background = "#3fb950";
            document.getElementById("status-text").innerText = "Stream Active";
        });
        socket.on("disconnect", () => {
            document.getElementById("status-dot").style.background = "#f85149";
            document.getElementById("status-text").innerText = "Disconnected";
        });

        socket.on("telemetry_update", (data) => {
            document.getElementById("val-temp").innerHTML = `${data.temperature.toFixed(1)} <span class="metric-unit">°C</span>`;
            document.getElementById("val-humidity").innerHTML = `${data.humidity.toFixed(0)} <span class="metric-unit">%</span>`;
            document.getElementById("val-distance").innerHTML = `${data.distance_cm.toFixed(1)} <span class="metric-unit">cm</span>`;
            document.getElementById("val-cpu").innerHTML = `${data.cpu_load.toFixed(0)} <span class="metric-unit">%</span>`;

            // Chart update
            tempChart.data.labels.push(data.timestamp);
            tempChart.data.datasets[0].data.push(data.temperature);
            if (tempChart.data.labels.length > maxPoints) {
                tempChart.data.labels.shift();
                tempChart.data.datasets[0].data.shift();
            }
            tempChart.update("none");
        });
    </script>
</body>
</html>
'''

REQUIREMENTS_TXT = '''flask>=3.0.0
flask-socketio>=5.3.6
opencv-python>=4.8.0
numpy>=1.24.0
pillow>=10.0.0
psutil>=5.9.0
'''

README_MD = '''# Real-Time Video Sensor Streaming Dashboard

A web-based network management dashboard streaming live camera video (MJPEG) and sensor telemetry (WebSockets) over local network interfaces.

## Features
- **MJPEG Video Streaming:** Low-latency video transmission via HTTP multipart boundaries (`/video_feed`).
- **Hardware Agnostic:** Automatically binds to OpenCV `VideoCapture(0)` or seamlessly generates synthetic frames with diagnostic overlays if camera hardware is unavailable.
- **WebSocket Telemetry:** Pushes environmental and range telemetry at 1 Hz via Flask-SocketIO.
- **Modern Responsive UI:** Dark-themed dashboard with live metric gauges and sliding 30-second Chart.js historical visualization.

## Architecture
```
[ OpenCV Camera / Sensor Sim ]
               |
               v
     [ Flask Application ]
      /                 \\
(MJPEG stream)    (Socket.IO Telemetry)
    /                     \\
   v                       v
[ Video Canvas ]     [ Live Gauges & Chart.js ]
```

## Quickstart

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Dashboard
```bash
python app.py
```

### 3. Open in Browser
Navigate to `http://localhost:5000` to view the live dashboard.
'''

files = {
    "sensors.py": SENSORS_PY,
    "app.py": APP_PY,
    "templates/index.html": INDEX_HTML,
    "requirements.txt": REQUIREMENTS_TXT,
    "README.md": README_MD,
}

for rel_path, content in files.items():
    file_path = BASE_DIR / rel_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Created {file_path}")

print("Project 2 (Realtime-Video-Sensor-Dashboard) built successfully!")
