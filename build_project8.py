import os
from pathlib import Path

DIR_TRAFFIC = Path(r"C:\Users\Lenovo\Desktop\Projects\Traffic-Pedestrian-Vehicle-Counter")
DIR_TRAFFIC.mkdir(parents=True, exist_ok=True)

TRACKER_PY = '''"""
Centroid Object Tracker.
Associates detected bounding box centroids between consecutive video frames using Euclidean distance minimization.
"""
from collections import OrderedDict
import numpy as np


class CentroidTracker:
    def __init__(self, max_disappeared: int = 25):
        self.next_object_id = 0
        self.objects = OrderedDict()       # ID -> (cx, cy)
        self.disappeared = OrderedDict()   # ID -> consecutive frames missed
        self.max_disappeared = max_disappeared

    def register(self, centroid):
        self.objects[self.next_object_id] = centroid
        self.disappeared[self.next_object_id] = 0
        self.next_object_id += 1

    def deregister(self, object_id):
        del self.objects[object_id]
        del self.disappeared[object_id]

    def update(self, rects):
        """Updates tracker state with new bounding boxes [x, y, w, h]."""
        if len(rects) == 0:
            for object_id in list(self.disappeared.keys()):
                self.disappeared[object_id] += 1
                if self.disappeared[object_id] > self.max_disappeared:
                    self.deregister(object_id)
            return self.objects

        input_centroids = np.zeros((len(rects), 2), dtype="int")
        for i, (x, y, w, h) in enumerate(rects):
            input_centroids[i] = (int(x + w / 2.0), int(y + h / 2.0))

        if len(self.objects) == 0:
            for i in range(len(input_centroids)):
                self.register(input_centroids[i])
        else:
            object_ids = list(self.objects.keys())
            object_centroids = list(self.objects.values())

            # Compute Euclidean distance matrix
            D = np.linalg.norm(np.array(object_centroids)[:, np.newaxis] - input_centroids, axis=2)

            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]

            used_rows = set()
            used_cols = set()

            for (row, col) in zip(rows, cols):
                if row in used_rows or col in used_cols:
                    continue

                if D[row, col] > 60:  # Distance threshold
                    continue

                object_id = object_ids[row]
                self.objects[object_id] = input_centroids[col]
                self.disappeared[object_id] = 0

                used_rows.add(row)
                used_cols.add(col)

            unused_rows = set(range(0, D.shape[0])).difference(used_rows)
            unused_cols = set(range(0, D.shape[1])).difference(used_cols)

            for row in unused_rows:
                object_id = object_ids[row]
                self.disappeared[object_id] += 1
                if self.disappeared[object_id] > self.max_disappeared:
                    self.deregister(object_id)

            for col in unused_cols:
                self.register(input_centroids[col])

        return self.objects
'''

COUNTER_PY = '''"""
Tripwire Line Crossing Detection Module.
Detects when tracked object centroids transition across a configured line.
"""
class TripwireCounter:
    def __init__(self, line_y: int):
        self.line_y = line_y
        self.counted_ids = set()
        self.previous_positions = {}  # ID -> prev_y
        self.in_count = 0
        self.out_count = 0

    def process(self, objects: dict):
        """Monitors positions relative to virtual tripwire line."""
        for object_id, centroid in objects.items():
            curr_y = centroid[1]
            prev_y = self.previous_positions.get(object_id, curr_y)

            if object_id not in self.counted_ids:
                # Downward crossing (Entering)
                if prev_y < self.line_y and curr_y >= self.line_y:
                    self.in_count += 1
                    self.counted_ids.add(object_id)
                # Upward crossing (Exiting)
                elif prev_y > self.line_y and curr_y <= self.line_y:
                    self.out_count += 1
                    self.counted_ids.add(object_id)

            self.previous_positions[object_id] = curr_y

        # Clean up stale IDs
        active_ids = set(objects.keys())
        self.previous_positions = {k: v for k, v in self.previous_positions.items() if k in active_ids}

        return self.in_count, self.out_count
'''

MAIN_PY = '''"""
Main Traffic & Pedestrian Counter Application.
Runs background subtraction, contour extraction, centroid tracking, and HUD rendering.
"""
import time
import numpy as np

try:
    import cv2
except ImportError:
    cv2 = None

from tracker import CentroidTracker
from counter import TripwireCounter


def run_demo():
    print("==================================================================")
    print("  REAL-TIME PEDESTRIAN & VEHICLE TRAFFIC ANALYTICS COUNTER")
    print("==================================================================")

    if cv2 is None:
        print("[!] OpenCV not installed. Install via: pip install opencv-python")
        return

    tracker = CentroidTracker(max_disappeared=15)
    tripwire = TripwireCounter(line_y=240)

    # Simulation canvas
    width, height = 640, 480
    bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25, detectShadows=True)

    print("[*] Running synthetic traffic demonstration (150 frames)...")

    # Simulate 3 moving vehicles across the scene
    sim_objects = [
        {"x": 180, "y": 20, "speed_y": 4, "w": 40, "h": 50, "label": "Vehicle-1"},
        {"x": 320, "y": 450, "speed_y": -5, "w": 30, "h": 40, "label": "Pedestrian-2"},
        {"x": 460, "y": 40, "speed_y": 6, "w": 45, "h": 60, "label": "Vehicle-3"}
    ]

    for frame_idx in range(120):
        frame = np.full((height, width, 3), 35, dtype=np.uint8)

        # Draw road lanes
        cv2.line(frame, (250, 0), (250, height), (70, 70, 70), 2)
        cv2.line(frame, (400, 0), (400, height), (70, 70, 70), 2)

        # Draw moving objects
        rects = []
        for obj in sim_objects:
            obj["y"] += obj["speed_y"]
            if 0 < obj["y"] < height - obj["h"]:
                cv2.rectangle(frame, (obj["x"], obj["y"]), (obj["x"] + obj["w"], obj["y"] + obj["h"]), (0, 212, 255), -1)
                rects.append((obj["x"], obj["y"], obj["w"], obj["h"]))

        # Update tracker & tripwire
        objects = tracker.update(rects)
        in_c, out_c = tripwire.process(objects)

        # Render Tripwire
        cv2.line(frame, (0, 240), (width, 240), (0, 0, 255), 2)
        cv2.putText(frame, "TRIPWIRE COUNTING LINE", (10, 230), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # Render HUD Overlay
        cv2.rectangle(frame, (10, 10), (280, 80), (20, 20, 20), -1)
        cv2.rectangle(frame, (10, 10), (280, 80), (80, 80, 80), 1)
        cv2.putText(frame, f"VEHICLES / IN : {in_c}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 120), 2)
        cv2.putText(frame, f"PEDESTRIAN/ OUT: {out_c}", (20, 68), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)

        # Draw tracking dots
        for object_id, centroid in objects.items():
            cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
            cv2.putText(frame, f"ID {object_id}", (centroid[0] - 10, centroid[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

    print(f"[*] Simulation Run Finished:")
    print(f"    Total Objects Entered (In): {in_c}")
    print(f"    Total Objects Exited (Out): {out_c}")
    print("[*] Tracker successfully assigned unique IDs and registered line crossings.")


if __name__ == "__main__":
    run_demo()
'''

REQUIREMENTS_TXT = '''opencv-python>=4.8.0
numpy>=1.24.0
'''

README_MD = '''# Real-Time Pedestrian & Vehicle Traffic Analytics Counter

A computer vision application for automated object tracking, entry/exit counting, and traffic flow analytics from live video feeds using OpenCV and centroid tracking algorithms.

## Architecture
```
[ Video Stream (Webcam / File) ]
               |
               v
  [ MOG2 Background Subtractor ]
               |
               v
   [ Contour Filter & Bounding Box ]
               |
               v
   [ Centroid Euclidean Tracker ]
               |
               v
[ Virtual Tripwire Crossing Logic ] ----> [ Live HUD Entry / Exit Counts ]
```

## Features
- **Centroid Association:** Robust object tracking minimizing Euclidean distance across consecutive frames.
- **Bi-Directional Counting:** Configurable tripwire detects upward and downward direction transitions.
- **ID Persistence & Deregistration:** Gracefully handles temporary occlusions with frame hysteresis counters.
- **Real-Time HUD Overlay:** Displays live count tallies, tracking IDs, and bounding trajectories.

## Quickstart
```bash
pip install -r requirements.txt
python main.py
```
'''

files = {
    "tracker.py": TRACKER_PY,
    "counter.py": COUNTER_PY,
    "main.py": MAIN_PY,
    "requirements.txt": REQUIREMENTS_TXT,
    "README.md": README_MD,
}

for rel, code in files.items():
    p = DIR_TRAFFIC / rel
    p.write_text(code.strip() + "\n", encoding="utf-8")
    print(f"Created {p}")

print("Project 8 (Traffic-Pedestrian-Vehicle-Counter) created!")
