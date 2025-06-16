import dht
import machine
import time
import network
from umqtt.simple import MQTTClient

# MQTT Broker Details
MQTT_BROKER = "broker.hivemq.com"
MQTT_TOPIC = "iot/hrishikesh/temp"

# Connect to Wokwi WiFi (Simulated)
print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Connected!")

# DHT Sensor Setup
sensor = dht.DHT22(machine.Pin(15))

# MQTT Setup
client = MQTTClient("esp32_client", MQTT_BROKER)
client.connect()

# Main Loop
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        message = str(temp)
        print("Sending:", message)
        client.publish(MQTT_TOPIC, message)
    except OSError as e:
        print("Sensor Error:", e)
    time.sleep(2)
