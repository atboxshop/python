# Need install RabbitMQ before using this code
import pika
msgs = []
credentials = pika.PlainCredentials('user1', 'user')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.30',virtual_host='testvhost',credentials=credentials))
chl = connection.channel()
#queue = chl.queue_declare(queue="Hello World",passive= True, durable=True,auto_delete = False)
while True:
    method_frame, header_frame, body = chl.basic_get(queue='Hello World',auto_ack=True)
    if method_frame:
        print("body : ", body)
        print("header frame : ", header_frame)
        print("method frame : ", method_frame)
        #print("total queued messages are : ", queue.method.message_count)
        print("the remaning messages is:", method_frame.message_count)
        msgs.append(body)
    else:
        print("No more messages returned")
        #print(msgs.__getitem__(0))
        connection.close()
        break