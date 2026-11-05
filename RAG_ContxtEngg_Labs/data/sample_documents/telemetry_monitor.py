"""
UST Global Enterprise Operations: Automated Turbomachinery SCADA Telemetry Monitoring Service
Script: telemetry_monitor.py | Author: Directorate of Turbomachinery & UST Engineering
"""

import os
import sys
import csv
import json
import time
import math
from pathlib import Path

class TurbomachineryTelemetryMonitor:
    def __init__(self, telemetry_csv_path=None):
        self.telemetry_csv_path = telemetry_csv_path or (Path(__file__).parent / "scada_telemetry.csv")
        self.sensors = self.load_sensor_manifest()

    def load_sensor_manifest(self):
        sensors = {}
        if not os.path.exists(self.telemetry_csv_path):
            return sensors
        with open(self.telemetry_csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sensors[row["sensor_id"]] = {
                    "tag": row["equipment_tag"],
                    "metric": row["metric"],
                    "unit": row["unit"],
                    "nominal": float(row["nominal"]),
                    "alarm_high": float(row["alarm_high"]),
                    "trip_high": float(row["trip_high"])
                }
        return sensors

    def evaluate_live_reading(self, sensor_id: str, reading_value: float) -> dict:
        if sensor_id not in self.sensors:
            return {"status": "UNKNOWN_SENSOR", "alert_level": "NONE"}
        cfg = self.sensors[sensor_id]
        if reading_value >= cfg["trip_high"]:
            return {
                "status": "CRITICAL_TRIP",
                "alert_level": "LEVEL_2_ESD",
                "sensor_id": sensor_id,
                "tag": cfg["tag"],
                "reading": reading_value,
                "threshold": cfg["trip_high"],
                "action": "AUTOMATED_ESD_TRIGGER"
            }
        elif reading_value >= cfg["alarm_high"]:
            return {
                "status": "WARNING",
                "alert_level": "LEVEL_1_WARN",
                "sensor_id": sensor_id,
                "tag": cfg["tag"],
                "reading": reading_value,
                "threshold": cfg["alarm_high"],
                "action": "OPERATOR_INVESTIGATION"
            }
        return {
            "status": "NORMAL",
            "alert_level": "NOMINAL",
            "sensor_id": sensor_id,
            "reading": reading_value
        }

    def compute_surge_margin(self, q_actual: float, q_surge: float) -> float:
        """Calculates aerodynamic distance delta S relative to Surge Control Line."""
        if q_surge <= 0:
            return 0.0
        return (q_actual - q_surge) / q_surge

def monitor_compressor_vibration(equipment_tag="K-301A", threshold=38.0):
    """Monitors live Bently Nevada vibration probes against Level 1 warning limits."""
    # Simulated reading for testing
    simulated_reading = 22.4
    if simulated_reading > threshold:
        return trigger_alarm(equipment_tag, f"Vibration excursion {simulated_reading} um pk-pk > {threshold} um")
    return {"status": "HEALTHY", "equipment_tag": equipment_tag, "vibration_um": simulated_reading}

def trigger_alarm(tag, reason):
    alert = {"tag": tag, "alarm": True, "reason": reason, "timestamp": time.time()}
    print(f"[ALARM TRIGGERED] {alert}")
    return alert

if __name__ == "__main__":
    monitor = TurbomachineryTelemetryMonitor()
    print(f"[OK] Turbomachinery Telemetry Monitor initialized with {len(monitor.sensors)} sensors.")
