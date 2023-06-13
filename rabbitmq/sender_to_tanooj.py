import pika

# credentials = pika.PlainCredentials("administrator","admin123")

target_tanooj_pc = pika.ConnectionParameters("192.168.1.103",
                                             5672,
                                             "/")

connection = pika.BlockingConnection(target_tanooj_pc)
print("connected successfully!")

channel = connection.channel()

channel.queue_declare(queue="eswar_pc")

channel.basic_publish(exchange="",
                      routing_key="eswar_pc",
                      body = "Hello tanooj_pc")

print("Message sent to tanooj_pc")

channel.close() 