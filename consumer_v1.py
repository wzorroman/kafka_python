import os
from kafka import KafkaConsumer

KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC_TEST = os.environ.get("KAFKA_TOPIC_TEST", "test")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.3.1")

# Create a KafkaConsumer instance
consumer = KafkaConsumer(
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS], 
    auto_offset_reset='earliest', 
    enable_auto_commit=False
)

# Subscribe to a specific topic
consumer.subscribe(topics=[KAFKA_TOPIC_TEST])

# Poll for new messages
while True:
    # msg = consumer.poll(timeout_ms=1000)
    raw_msgs = consumer.poll(timeout_ms=1000)
    if raw_msgs:
        for topic_partition, messages in raw_msgs.items():
            for message in messages:
                msg_p = f"Topic: {topic_partition.topic}"
                msg_p += f"| Partition: {topic_partition.partition}"
                msg_p += f"| Offset: {message.offset} | Key: {message.key}"
                msg_p += f"| Value: {message.value}"
                        
                print(msg_p)
    else:
        print("No new messages")