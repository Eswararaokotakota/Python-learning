import pika, sys, os

def main():

    def on_message_received(ch, method, properties, body):
         print(body)
#creating a connection to locally running rabbitmq broker
    connection_parameters = pika.ConnectionParameters('localhost')#if you are using another pc for consumer you can enter the ip address of the pc

#creating connection to rabbitmq
    connection = pika.BlockingConnection(connection_parameters)
#now we have a connection
#then now we create a channel for that

    channel = connection.channel()
#done connection

#Now declaring the queue for data queue
    channel.queue_declare(queue="letterbox")

#consuming means receiving the message here (in the producer publish is used understood?)
    channel.basic_consume(queue="letterbox", auto_ack=True, on_message_callback= on_message_received)

    print("started consuming")

    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except:
            os._exit(0)

