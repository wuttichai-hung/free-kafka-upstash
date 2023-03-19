# Free Kafka upstash

Upstash provide severless data for kafka including free plans with no credit card required

# Pre-requirement

1. register upstash [here](https://upstash.com/)
2. create kafka cluster
3. add config Endpoint, Username, Password in .env (change .env-example to .env) file **keep it secret**

# Install packages

```bash
pip install -r requirements.txt
```

# Run consumer

```bash
python consumer.py
```

# Run producer

```bash
python producer.py
```
