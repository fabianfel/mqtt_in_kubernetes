import json
import random
import time
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()

mqttc = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    "aHR0cHM6Ly9naXRodWIuY29tL0pvbmFzU3RvL2R3aC5naXQ=",
    clean_session=False,
)

mqtt_broker = os.environ.get('MQTT_BROKER')
mqtt_port = os.environ.get('MQTT_PORT')
mqtt_topic = os.environ.get('MQTT_TOPIC')

fin = os.environ.get('FIN')

mqttc.connect(mqtt_broker, int(mqtt_port), 5)
mqttc.loop_start()

print("connected to broker")

# send message every 5 seconds
while True:
    try:
        
        message = {
            "fin": fin,
            "zeit": int(time.time()),
            "geschwindigkeit": random.randint(0, 50),
        }
        
        mqttc.publish(mqtt_topic, json.dumps(message), qos=1)

        # sleep for 5 seconds
        time.sleep(5)
    except KeyboardInterrupt:
        mqttc.loop_stop()
        mqttc.disconnect()
        print("exiting")
        exit(0)
