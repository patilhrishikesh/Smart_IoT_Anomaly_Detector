# Step 1: Sensor Simulation using Wokwi (ESP32 + DHT22)

This step simulates a real-world temperature and humidity sensor (DHT22) using the ESP32 microcontroller inside the Wokwi online simulator.

### 🛠 Tools & Technologies
- Wokwi Simulator (https://wokwi.com)
- ESP32 (MicroPython)
- DHT22 Sensor
- Python (MicroPython syntax)

### ⚙️ Setup Instructions
1. Go to [Wokwi](https://wokwi.com)
2. Click **New Project** → Choose **MicroPython on ESP32**
3. Replace `main.py` with the code in this repo
4. Add a **DHT22 sensor**, and wire:
   - VCC → 3V3
   - GND → GND
   - DATA → GPIO 15
5. Click the green ▶️ "Play" button to simulate

### 💡 Output (Example)

