from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

users = ["Alice", "Bob", "Charlie", "David"]
actions = ["click", "search", "view", "purchase"]

while True:
    event = {
        "user": random.choice(users),
        "action": random.choice(actions),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    producer.send("user_events", value=event)
    print(f"Sent: {event}")
    time.sleep(1)

