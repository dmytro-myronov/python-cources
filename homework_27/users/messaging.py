import pika
import json

def publish_event(event_type, payload):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.exchange_declare(exchange='events', exchange_type='topic')

    message = json.dumps(payload)
    routing_key = f"user.{event_type}"
    channel.basic_publish(exchange='events', routing_key=routing_key, body=message)
    connection.close()
