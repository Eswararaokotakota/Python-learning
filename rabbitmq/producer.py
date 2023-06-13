import pika

credentials = pika.PlainCredentials("eswar","eswar")
#creating a connection to locally running rabbitmq broker
connection_parameters = pika.ConnectionParameters('localhost',5627,"/",credentials)#if you are using another pc for consumer you can enter the ip address of the pc

#creating connection to rabbitmq
connection = pika.BlockingConnection(connection_parameters)
#now we have a connection
#then now we create a channel for that

channel = connection.channel()
#done connection

#Now declaring the queue for data queue
channel.queue_declare(queue="letterbox")

#now we will write the msg tobe sent
message = "Hello eswar this the message from producer"

#sending on channel by using basic publish method
channel.basic_publish(exchange='',routing_key='letterbox',body=message)
print(f"Sent message:{message}")

#cloasing connection
connection.close()
