import paho.mqtt.client as mqtt
from sklearn.ensemble import IsolationForest
from collections import deque
import numpy as np
import time

# MQTT settings
broker = "broker.hivemq.com"
topic = "iot/hrishikesh/temp"

# Data buffer (rolling window)
window_size = 20
data_window = deque(maxlen=window_size)

# Isolation Forest model
model = IsolationForest(contamination=0.1)

def detect_anomaly(latest_value):
    if len(data_window) < window_size:
        return "Waiting for more data..."

    X = np.array(data_window).reshape(-1, 1)
    model.fit(X)
    pred = model.predict([[latest_value]])
    return "🔴 Anomaly" if pred[0] == -1 else "🟢 Normal"

# MQTT message handler
def on_message(client, userdata, msg):
    try:
        value = float(msg.payload.decode())
        data_window.append(value)
        result = detect_anomaly(value)
        print(f"Received: {value:.2f} °C → {result}")
    except ValueError:
        print("Invalid data received")

# MQTT setup
client = mqtt.Client()
client.connect(broker)
client.subscribe(topic)
client.on_message = on_message

print("🚀 Subscribed to MQTT topic. Waiting for sensor data...\n")
client.loop_forever()
