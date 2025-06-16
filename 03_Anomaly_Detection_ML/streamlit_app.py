import csv
from datetime import datetime
import os
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import paho.mqtt.client as mqtt
from collections import deque

# Set up Streamlit layout
st.set_page_config(layout="wide")
st.title("🌡️ IoT Temperature Anomaly Detector")
status_placeholder = st.empty()
chart_placeholder = st.empty()

# Settings
MQTT_BROKER = "broker.hivemq.com"
MQTT_TOPIC = "iot/hrishikesh/temp"
WINDOW_SIZE = 30
data_window = deque(maxlen=WINDOW_SIZE)
anomalies = deque(maxlen=WINDOW_SIZE)

# ML Model
model = IsolationForest(contamination=0.1)

def detect_anomaly(latest_value):
    if len(data_window) < WINDOW_SIZE:
        return None  # Not enough data
    X = np.array(data_window).reshape(-1, 1)
    model.fit(X)
    pred = model.predict([[latest_value]])
    return pred[0] == -1  # True if anomaly

def log_to_csv(temp, is_anomaly):
    file_exists = os.path.isfile("temp_log.csv")
    with open("temp_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Temperature", "Anomaly"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp, is_anomaly])
        
# MQTT callback
def on_message(client, userdata, msg):
    try:
        temp = float(msg.payload.decode())
        data_window.append(temp)
        is_anomaly = detect_anomaly(temp)
        anomalies.append(temp if is_anomaly else np.nan)
        
        # ✅ Log to CSV
        log_to_csv(temp, is_anomaly)

        # Update status
        status = "🔴 Anomaly Detected!" if is_anomaly else "🟢 Normal"
        status_placeholder.markdown(f"### Latest Reading: **{temp:.2f} °C** — {status}")

        # Update live chart
        fig, ax = plt.subplots()
        ax.plot(data_window, label="Temperature", color="blue")
        ax.plot(anomalies, label="Anomalies", color="red", linestyle="None", marker="o")
        ax.set_ylabel("Temperature (°C)")
        ax.set_xlabel("Time")
        ax.legend()
        chart_placeholder.pyplot(fig)
    except Exception as e:
        st.error(f"Error: {e}")


# Start MQTT
client = mqtt.Client()
client.connect(MQTT_BROKER)
client.subscribe(MQTT_TOPIC)
client.on_message = on_message
client.loop_start()

st.success("✅ Subscribed to MQTT topic and running in background...")

# Keep the app alive
while True:
    pass
