import pika
import json

def callback(ch, method, properties, body):
    event_type = method.routing_key
    data = json.loads(body)

    if event_type == "user.registered":
        print(f"Send welcome email to {data['email']}")
    elif event_type == "user.updated":
        print(f"Log user update: {data}")
    else:
        print(f"Unknown event: {event_type}")

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.exchange_declare(exchange='events', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='events', queue=queue_name, routing_key="user.*")

print(' [*] Waiting for events. To exit press CTRL+C')
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
