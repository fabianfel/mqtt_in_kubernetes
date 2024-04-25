import os
import psycopg2
import paho.mqtt.client as mqtt
import time
import json
from dotenv import load_dotenv

# load env variables if existing
load_dotenv()

# read variables from env
db_host = os.environ.get('PG_HOST')
db_port = os.environ.get('PG_PORT')

db_name = os.environ.get('PG_DATABASE')
db_user = os.environ.get('PG_USER')
db_password = os.environ.get('PG_PASSWORD')

mqtt_broker = os.environ.get('MQTT_BROKER')
mqtt_port = os.environ.get('MQTT_PORT')
mqtt_topic = os.environ.get('MQTT_TOPIC')

# connect to database
try:
    conn = psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port
    )
    print('Verbindung zur Datenbank hergestellt!')
except psycopg2.OperationalError as e:
    print(f'Fehler beim Verbinden mit der Datenbank: {e}')


def on_message(client, userdata, message):
    # read message from broker and insert into table
    
    try:
        resp = json.loads(message.payload)

        try:
            cur = conn.cursor()
            cur.execute(
                'INSERT INTO staging.messung(payload) VALUES (%s)', (json.dumps(resp),)
            )
            conn.commit()
            cur.close()
            print('Message saved to DB: ' + str(resp))
            
        except:
            print('failed to save message to DB')
    except:
        print('failed to parse message')


mqttc = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    'Z2l0QGdpdGh1Yi5jb206Sm9uYXNTdG8vZHdoLmdpdA==',
    clean_session=False,
)

mqttc.on_message = on_message

mqttc.connect(mqtt_broker, int(mqtt_port), 5)
print("connected to broker")

mqttc.subscribe(mqtt_topic, qos=1)

try: 
    mqttc.loop_forever()
except KeyboardInterrupt:
    print('exiting')
    mqttc.loop_stop()
    mqttc.disconnect()
    exit(0)