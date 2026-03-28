from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

i = 0
while True:
    data = {"message": f"Hello Kafka {i}"}
    producer.send('test-topic', value=data)
    print("Sent:", data)
    i += 1
    time.sleep(2)