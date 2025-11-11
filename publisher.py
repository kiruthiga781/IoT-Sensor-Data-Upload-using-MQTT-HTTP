"""
IoT Sensor Data Upload using MQTT
Publisher Script
Author: Kiruthiga
Description: Publishes simulated temperature and humidity data to MQTT broker.
"""

import time
import json
import random
import paho.mqtt.client as mqtt

# MQTT Broker Configuration
BROKER = "broker.hivemq.com"   # Public MQTT broker
PORT = 1883
TOPIC = "iot/sensor/data"

# Create MQTT client (compatible with latest Paho version)
client = mqtt.Client(
    client_id="Python_IoT_Publisher",
    protocol=mqtt.MQTTv311,
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

# Connect to broker
client.connect(BROKER, PORT, 60)

print("✅ Connected to MQTT Broker successfully!")
print("📡 Publishing data to topic:", TOPIC)
print("-------------------------------------------")

# Main loop
while True:
    # Simulated sensor data (replace with actual sensor values if available)
    temperature = round(random.uniform(25.0, 35.0), 2)
    humidity = round(random.uniform(40.0, 60.0), 2)

    # Create JSON message
    data = {"temperature": temperature, "humidity": humidity}
    payload = json.dumps(data)

    # Publish to MQTT topic
    client.publish(TOPIC, payload)
    print(f"Data sent → {payload}")

    # Wait before sending next data
    time.sleep(5)
