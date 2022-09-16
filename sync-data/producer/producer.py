import pika
import json


def produce_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='products', exchange_type='fanout')
    channel.basic_publish(exchange='products', routing_key='', body=json.dumps(message))

    connection.close()