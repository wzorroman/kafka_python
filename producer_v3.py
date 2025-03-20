import os
import time
import random
import json
from kafka import KafkaProducer

KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC_TEST = os.environ.get("KAFKA_TOPIC_TEST", "test")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.9.0")

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
    api_version=KAFKA_API_VERSION,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

i = 0
print("Producer 3 Generando ... \n")
while i <= 300:    
    fecha_random = f"2024-{random.randint(1, 12)}-{random.randint(1, 30)}"
    data = {
        "edad": random.randint(10, 50),
        "nombre": f"wilson {i}",
        "fecha": fecha_random,
    }

    # Enviar el mensaje
    producer.send(KAFKA_TOPIC_TEST, value=data)
    print(f"Mensaje enviado: {json.dumps(data)}")
    i += 1
    # time.sleep(random.randint(2, 5))
    
# Asegurarse de que el mensaje se haya enviado
producer.flush()

# Cerrar el productor después de enviar
producer.close()