import os
import json
from kafka import KafkaConsumer
from dotenv import load_dotenv
load_dotenv()

KAFKA_ENDPOINT = os.getenv("KAFKA_ENDPOINT")
KAFKA_USER = os.getenv("KAFKA_USER")
KAFKA_PASS = os.getenv("KAFKA_PASS")

consumer = KafkaConsumer(
    bootstrap_servers=[KAFKA_ENDPOINT],
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username=KAFKA_USER,
    sasl_plain_password=KAFKA_PASS,
    # key_deserializer=lambda v: json.loads(v.decode('utf-8')),
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest'
)
consumer.subscribe(topics='topic1')
for msg in consumer:
    print(f"topic: {msg.topic}, partition: {msg.partition}, offset: {msg.offset}, key: {msg.key} ,value: {msg.value}")
consumer.close()
