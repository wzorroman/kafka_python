### Alcance con 1 consumer y leer datos JSON:

un script de **consumidor** en Python (`consumer.py`) que lee los datos JSON que se envían al Kafka Topic, procesa el mensaje y extrae los valores de las claves del diccionario (como "nombre", "edad" y "fecha").

### Explicación del código:

1.  **Configuración de Kafka**:
    
    -   Se obtienen las configuraciones como el servidor de Kafka (`KAFKA_BOOTSTRAP_SERVERS`), el nombre del topic (`KAFKA_TOPIC_TEST`), y la versión de la API de Kafka (`KAFKA_API_VERSION`) desde las variables de entorno.
    
2.  **Creación del consumidor Kafka**:
    
    -   El `KafkaConsumer` se configura con las opciones adecuadas, como `auto_offset_reset="earliest"` para comenzar a consumir desde el primer mensaje disponible y `value_deserializer=lambda x: json.loads(x.decode('utf-8'))` para deserializar el mensaje JSON a un diccionario de Python.
3.  **Consumiendo mensajes**:
    
    -   Usamos el método `poll()` para obtener los mensajes de Kafka. Si hay mensajes disponibles, el consumidor procesa cada mensaje.
4.  **Extracción de datos del diccionario**:
    
    -   Una vez que se recibe el mensaje, el valor (que es un diccionario JSON) es procesado. Extraemos los valores asociados a las claves `"nombre"`, `"edad"`, y `"fecha"` del diccionario y los mostramos en la consola.
5.  **Manejo de errores**:
    
    -   Se maneja cualquier error en el procesamiento del mensaje con un bloque `try-except` para capturar excepciones y asegurarse de que el consumidor continúe ejecutándose sin interrupciones.

### Ejecución:

1.  **Iniciar Kafka**: Asegúrate de tener Kafka corriendo en el servidor o entorno especificado (por defecto `localhost:29092`).
    
2.  **Ejecutar el consumidor**:
    
    -   Puedes ejecutar el script `consumer.py` para leer los mensajes desde el Kafka Topic (`test`) y procesarlos.
        `python consumer.py` 
    

Este script consumirá los mensajes que se envíen al topic `test` y mostrará los valores de "nombre", "edad" y "fecha" en la consola.