import os
from kafka import KafkaConsumer
import json

KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC_TEST = os.environ.get("KAFKA_TOPIC_TEST", "test")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.3.1")

consumer = KafkaConsumer(
    KAFKA_TOPIC_TEST,
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
    api_version=KAFKA_API_VERSION,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    auto_commit_interval_ms=5000
)
while True:
    msg = consumer.poll(timeout_ms=1000)  # Esperar 
    if not msg:
        print("No se recibieron mensajes en este ciclo.")
        continue
    
    for topic_partition, messages in msg.items():
        for message in messages:
            # Asumimos que el mensaje está en formato JSON, 
            # puedes adaptarlo si es diferente
            try:
                message_value = message.value.decode('utf-8')
                print(f"Mensaje recibido (RAW): {message_value}")
                # Si el mensaje es un JSON, lo procesamos
                try:
                    message_json = json.loads(message_value)
                    print(f" - decodificado como JSON: {message_json}")
                    print(f" -- Nombre: {message_json.get('nombre')}")
                except json.JSONDecodeError:
                    print(f"El mensaje no es un JSON válido: {message_value}")
            except Exception as e:
                print(f"Error al procesar el mensaje: {e}")
    
