### Alcance con 2 Consumer:

Para implementar un escenario donde tienes dos consumidores (`consumer1.py` y `consumer2.py`), y cada uno debe procesar un solo mensaje de la cola, imprimirlo y luego eliminarlo de la cola para que el otro consumidor no lo imprima, utilizaremos el mecanismo de **offsets manuales** de Kafka. Este mecanismo nos permitirá controlar explícitamente cuándo se marca un mensaje como procesado, y asegurarnos de que solo un consumidor procese cada mensaje.

### Conceptos Claves:

-   **Offset manual**: En lugar de permitir que Kafka haga un "auto-commit" del offset, utilizamos un offset manual para asegurarnos de que solo un consumidor procese un mensaje.
-   **Group ID**: Si ambos consumidores tienen el mismo `group_id`, Kafka les asignará particiones y mensajes de manera que un consumidor reciba mensajes de una partición y el otro de otra.

### Explicación del código:
1.  **Grupo de consumidores**: Ambos consumidores (`consumer1.py` y `consumer2.py`) están configurados para formar parte del mismo grupo de consumidores (`KAFKA_GROUP_ID = "consumer_group"`). Kafka asegura que cada mensaje solo se entrega a un consumidor dentro del grupo.
    
2.  **Deshabilitar el commit automático**: Ambos consumidores tienen `enable_auto_commit=False`, lo que significa que los consumidores deben hacer el commit manualmente para asegurar que el mensaje solo se marque como procesado después de que el consumidor haya terminado de procesarlo.
    
3.  **Commit manual de los offsets**: Después de procesar un mensaje, cada consumidor llama a `consumer.commit()`, lo que confirma que ese mensaje ha sido procesado correctamente y evita que se procese nuevamente.
    
4.  **Deserialización de JSON**: Los mensajes recibidos están en formato JSON, por lo que se deserializan utilizando `json.loads()` para convertirlos en diccionarios de Python.
    
5.  **Control de offsets**: Al deshabilitar el commit automático y realizar el commit manual después de procesar el mensaje, garantizamos que el mensaje no sea procesado nuevamente por otro consumidor, ya que Kafka avanzará el offset solo después de que el commit haya sido hecho.
    

### Ejecución:

1.  **Iniciar Kafka**: Asegúrate de tener Kafka corriendo en el servidor o entorno especificado (por defecto `localhost:29092`).
    
2.  **Ejecutar los consumidores**: Ejecuta ambos consumidores en terminales separadas:
    
    -   En una terminal, ejecuta `python consumer1.py`.
    -   En otra terminal, ejecuta `python consumer2.py`.
    
    De esta manera, ambos consumidores estarán listos para leer los mensajes de la cola, procesarlos y confirmar que el mensaje ha sido procesado, evitando que el otro consumidor lo procese nuevamente.
    

### Conclusión:

-   **Distribución de mensajes**: Como ambos consumidores pertenecen al mismo grupo de consumidores, Kafka distribuye los mensajes entre ellos. Cada consumidor procesa un mensaje, lo imprime, y luego lo confirma.
-   **Offset manual**: Al utilizar `commit()` de manera manual, controlamos explícitamente cuándo un mensaje es procesado y aseguramos que no sea procesado dos veces.