# IoT Sensor Data Upload using MQTT (Python)

This project demonstrates how to collect and upload IoT sensor data (temperature and humidity) using the MQTT protocol in Python.

## 🚀 Features
- Publishes simulated sensor data (temperature, humidity)
- Uses MQTT for lightweight IoT communication
- Real-time message receiving via subscriber script
- Works with free public broker `broker.hivemq.com`

## 🧩 Files
- `publisher.py` → Sends data to MQTT broker  
- `subscriber.py` → Receives and prints messages  

## ⚙️ Requirements
Install dependencies:
```bash
pip install paho-mqtt
