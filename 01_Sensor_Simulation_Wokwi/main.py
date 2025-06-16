import dht
import machine
import time

sensor = dht.DHT22(machine.Pin(15))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature:", temp, "°C")
        print("Humidity:", hum, "%")
    except OSError as e:
        print("Sensor error:", e)
    time.sleep(2)
