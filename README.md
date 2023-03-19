# Free Kafka upstash

Upstash provide severless data for kafka including free plans with no credit card required

# Pre-requirement

1. You need to register upstash first [Click Here](https://upstash.com/)
2. Create kafka cluster
3. Add config Endpoint, Username, Password in .env (change .env-example to .env) file **keep it secret**

# Comamnd

```bash
# install libraries
pip install -r requirements.txt

# run consumer
python consumer.py

# run producer
python producer.py
```

# More detail (gerated by chatgpt)

Ask: give me an code python for kafka produce and consume with best practice
Ans: Sure, here is an example of how to produce and consume messages using Kafka in Python, following some best practices:

```python
from kafka import KafkaProducer, KafkaConsumer
import json

# Define Kafka producer configuration
producer_config = {
    "bootstrap_servers": ["localhost:9092"],
    "value_serializer": lambda x: json.dumps(x).encode("utf-8")
}

# Define Kafka consumer configuration
consumer_config = {
    "bootstrap_servers": ["localhost:9092"],
    "value_deserializer": lambda x: json.loads(x.decode("utf-8")),
    "auto_offset_reset": "latest", # set to earliest if you want to consume from the beginning
    "enable_auto_commit": True,
    "auto_commit_interval_ms": 5000 # adjust to your needs
}

# Example function to produce messages to Kafka
def produce_messages():
    producer = KafkaProducer(**producer_config)
    for i in range(10):
        message = {"message": f"This is message {i}"}
        producer.send("test-topic", message)
        print(f"Produced message {i}")
    producer.close()

# Example function to consume messages from Kafka
def consume_messages():
    consumer = KafkaConsumer("test-topic", **consumer_config)
    for message in consumer:
        print(f"Consumed message: {message.value}")
    consumer.close()

# Main function
if __name__ == "__main__":
    produce_messages()
    consume_messages()
```

Some notes about this example:

- The `KafkaProducer` and `KafkaConsumer` classes are used to respectively produce and consume messages from Kafka.
- The producer configuration includes a `value_serializer` function to serialize the message payload as JSON before sending it to Kafka.
- The consumer configuration includes a `value_deserializer` function to deserialize the message payload as JSON when consuming messages from Kafka.
- The `auto_offset_reset` parameter is set to latest to consume only new messages, but you can set it to earliest to consume from the beginning.
- The consumer is set to automatically commit the offsets every 5 seconds, but you can adjust this value to your needs.
- The `produce_messages` function produces 10 messages to the test-topic topic.
- The `consume_messages` function consumes messages from the test-topic topic and prints them to the console.
- The main function calls both the `produce_messages` and `consume_messages` functions.

This is just a simple example, and there are many other options and parameters that you can configure when working with Kafka in Python. I recommend checking out the official kafka-python documentation for more information and examples: https://kafka-python.readthedocs.io/
