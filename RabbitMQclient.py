__author__ = 'root'

import pika
import sys


class RabbitMQClient:
    def __int__(self):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

    def create_direct_exchange(self, exchange_name):
        self.channel.exchange_declare(exchange=exchange_name, type='direct')

    def send_data_over_direct_exchange(self, message, exchange_name, message_routing_key):
        self.channel.basic_publish(exchange=exchange_name,
                              routing_key= message_routing_key,
                              body=message)

        print(" [x] Sent %r:%r" % (message_routing_key, message))



    """
    def callback(ch, method, properties, body):
            print(" [x] %r:%r" % (method.routing_key, body))
    """
    def receive_direct_message(self, callback, message_routing_keys):
        result = self.channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        for rKey in message_routing_keys:
            self.channel.queue_bind(exchange='direct_logs',
                               queue=queue_name,
                               routing_key=rKey)

        self.channel.basic_consume(callback,
                              queue=queue_name,
                              no_ack=True)

        self.channel.start_consuming()


    def close(self):
        self.connection.close()
