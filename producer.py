import os
import json
from kafka import KafkaProducer
from dotenv import load_dotenv
load_dotenv()

KAFKA_ENDPOINT = os.getenv("KAFKA_ENDPOINT")
KAFKA_USER = os.getenv("KAFKA_USER")
KAFKA_PASS = os.getenv("KAFKA_PASS")

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_ENDPOINT],
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username=KAFKA_USER,
    sasl_plain_password=KAFKA_PASS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    # key_serializer=lambda v: json.dumps(v).encode('utf-8')
)
# code here
producer.send('topic1', key=b"abc", value={"message": "1235"})
producer.flush()

producer.close()
