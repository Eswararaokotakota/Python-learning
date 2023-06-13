
import pika

crendentials = pika.PlainCredentials("administrator","admin123")
target_pc = pika.ConnectionParameters("localhost",5672,'/',crendentials)
connection = pika.BlockingConnection(target_pc)

channel = connection.channel()

channel.queue_declare(queue="eswar", durable=True)

channel.basic_publish( exchange="",
                       routing_key="eswar",
                       body = "hello eswar")

print("message sent to receiver")
connection.close()
