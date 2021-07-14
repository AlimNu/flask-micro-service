import pika


params = pika.URLParameters('amqps://xywqkakv:n09rwGm9XBtXaBYNjYmFQwGIqGt_H_MV@snake.rmq2.cloudamqp.com/xywqkakv')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('recieve in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Start Consuming')

channel.start_consuming()

channel.close()
