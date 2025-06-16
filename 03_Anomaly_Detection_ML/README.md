# Step 3: Anomaly Detection with Machine Learning + Streamlit Visualization

This step connects real-time IoT sensor data (simulated via MQTT) to a Python-based ML pipeline using **Isolation Forest** for anomaly detection, and visualizes the results live using **Streamlit**.

---

## 🎯 Objectives
- Receive temperature data in real-time via MQTT
- Detect anomalies using Isolation Forest (unsupervised ML)
- Visualize data and anomalies on a live graph
- Deploy as a Streamlit web app

---

## 🛠️ Tools & Technologies

| Purpose        | Tool/Library             |
|----------------|--------------------------|
| Data stream    | MQTT (broker.hivemq.com) |
| ML Model       | scikit-learn (Isolation Forest) |
| UI             | Streamlit                |
| Visualization  | Matplotlib               |
| Language       | Python 3.x               |

---

## 🚀 How to Run Locally

### 1. Set Up Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

Install Required Packages
pip install -r requirements.txt

Run the Streamlit App
streamlit run streamlit_app.py