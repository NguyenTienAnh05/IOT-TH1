import json
import random
import time
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"
DEVICE_ID = "sensor01"

def main():
    client = mqtt.Client()
    
    try:
        client.connect(BROKER, PORT, 60)
        client.loop_start()
        
        while True:
            temperature = round(random.uniform(25.0, 38.0), 1)
            humidity = round(random.uniform(35.0, 80.0), 1)
            
            payload_data = {
                "device_id": DEVICE_ID,
                "temperature": temperature,
                "humidity": humidity
            }
            
            payload = json.dumps(payload_data)
            client.publish(TOPIC, payload)
            print(f"Đã gửi: {payload}")
            
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\nĐã dừng chương trình Sensor Publisher.")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
