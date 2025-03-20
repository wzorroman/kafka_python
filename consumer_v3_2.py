# consumer Nro 2 que solo imprime los mensajes recibidos y borra de la cola
import os
from kafka import KafkaConsumer
import json

# Configuración de los parámetros de Kafka
KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC_TEST = os.environ.get("KAFKA_TOPIC_TEST", "test")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.3.1")
KAFKA_GROUP_ID = "consumer_group"  # Asegúrate de que ambos consumidores estén en el mismo grupo

# Crear el consumidor de Kafka
consumer = KafkaConsumer(
    KAFKA_TOPIC_TEST,
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
    api_version=(int(KAFKA_API_VERSION.split('.')[0]), int(KAFKA_API_VERSION.split('.')[1]), int(KAFKA_API_VERSION.split('.')[2])),
    group_id=KAFKA_GROUP_ID,
    auto_offset_reset="earliest",  # Empezar desde el primer mensaje disponible
    enable_auto_commit=False,  # Deshabilitar commit automático para manejar los offsets manualmente
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserializar JSON
)

print("Consumer 2 está listo para recibir mensajes...")
while True:
    msg = consumer.poll(timeout_ms=1000)  # Timeout de 1 segundo
    if msg:
        for topic_partition, messages in msg.items():
            for message in messages:
                try:
                    # El valor del mensaje es un diccionario JSON que contiene los datos
                    data = message.value
                    print(f"Consumer 2 recibió el mensaje: {data}")
                    
                    # Procesamiento de los datos
                    nombre = data.get("nombre")
                    edad = data.get("edad")
                    fecha = data.get("fecha")
                    
                    print(f"Nombre: {nombre}, Edad: {edad}, Fecha: {fecha}")

                    # Confirmamos que el mensaje fue procesado
                    consumer.commit()
                    print("Consumer 2 ha procesado y confirmado el mensaje.")
                except Exception as e:
                    print(f"Error al procesar el mensaje: {e}")
    else:
        print("No se recibieron mensajes en este ciclo.")
