import pika

credentials = pika.PlainCredentials("administrator","admin123")
target_pc = pika.ConnectionParameters("localhost",5672,"/",credentials)

connection = pika.BlockingConnection(target_pc)

channel = connection.channel()

channel.queue_declare(queue="eswar",durable=True)

def callback(ch, method, process, body):
    print("Received",body)

channel.basic_consume(queue="eswar",
                      auto_ack=True,
                      on_message_callback=callback
)

print("Waiting for message.....")
channel.start_consuming()