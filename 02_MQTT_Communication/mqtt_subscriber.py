import paho.mqtt.client as mqtt

# MQTT Broker and Topic
broker = "broker.hivemq.com"
topic = "iot/hrishikesh/temp"

# Callback when message received
def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} °C")

# MQTT Client Setup
client = mqtt.Client()
client.connect(broker)
client.subscribe(topic)
client.on_message = on_message

print("Subscribed to MQTT topic. Waiting for data...\n")
client.loop_forever()
