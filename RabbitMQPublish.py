# Need install RabbitMQ before using this code
import pika
credentials = pika.PlainCredentials('user1', 'user')
server = "192.168.31.30"
connection = pika.BlockingConnection(pika.ConnectionParameters(host = server,virtual_host = 'testvhost',credentials = credentials))
channel = connection.channel()
#channel.queue_declare(queue='Hello Wolrd')
for i in range(5000):
    msg = "Hello World! Message " + str(i)
    channel.basic_publish(exchange = '',
                      routing_key = 'Hello World',
                      body = msg)
    print("Sent message number:",i)
print("Sent Messages Successful")
connection.close()