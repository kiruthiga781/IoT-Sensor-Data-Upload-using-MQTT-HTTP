"""
IoT Sensor Data Upload using MQTT
Subscriber Script
Author: Kiruthiga
Description: Subscribes to MQTT topic and displays incoming sensor data.
"""

import paho.mqtt.client as mqtt

# MQTT Broker Configuration
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/sensor/data"

# Callback function when message arrives
def on_message(client, userdata, msg):
    print(f"📩 Received → {msg.payload.decode()}")

# Create client
client = mqtt.Client(
    client_id="Python_IoT_Subscriber",
    protocol=mqtt.MQTTv311,
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

# Set message callback
client.on_message = on_message

# Connect and subscribe
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("✅ Connected to MQTT Broker and subscribed to topic:", TOPIC)
print("🔍 Waiting for incoming messages...\n")

# Keep the subscriber running
client.loop_forever()
