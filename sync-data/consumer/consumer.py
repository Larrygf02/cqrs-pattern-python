import pika
import json
from sync import upsert_data

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='products', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='products', queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, payload):
    print(" [x] %r" % payload)
    upsert_data(json.loads(payload))
    

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()