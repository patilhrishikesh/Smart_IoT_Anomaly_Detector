# Step 2: MQTT Communication – Sending Sensor Data to Python

This step builds on the previous simulation by enabling real-time communication between the simulated ESP32 device and a Python script using the MQTT protocol.

## 📌 Objective
- Publish temperature data from a DHT22 sensor (simulated in Wokwi) to an MQTT broker.
- Receive and display that data in real-time using a Python subscriber script.

---

## 🧰 Tools & Technologies
- Wokwi (MicroPython on ESP32)
- DHT22 Sensor
- MQTT Protocol (broker.hivemq.com)
- Python 3
- `paho-mqtt` Python package

---

## 🚀 Setup Instructions

### 1. Simulated ESP32 + MQTT Publisher (Wokwi)
- Open your Wokwi project
- Use `MicroPython on ESP32`
- Add and wire a DHT22 sensor:
  - VCC → 3V3
  - GND → GND
  - DATA → GPIO 15

- Update `main.py` with the following code:

```python
import dht
import machine
import time
import network
from umqtt.simple import MQTTClient

MQTT_BROKER = "broker.hivemq.com"
MQTT_TOPIC = "iot/hrishikesh/temp"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    time.sleep(0.1)

sensor = dht.DHT22(machine.Pin(15))
client = MQTTClient("esp32_client", MQTT_BROKER)
client.connect()

while True:
    sensor.measure()
    temp = sensor.temperature()
    print("Sending:", temp)
    client.publish(MQTT_TOPIC, str(temp))
    time.sleep(2)
