import pika,json

from pika.amqp_object import Method
params=pika.URLParameters('amqps://xfppnauw:fSmY1Xp-KwFXOFnaJ2xUTC6cmjijGOTj@puffin.rmq2.cloudamqp.com/xfppnauw')
connection=pika.BlockingConnection(params)
channel = connection.channel()
def publish(method,body):
    properties=pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body),properties=properties)
