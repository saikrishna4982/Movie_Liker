import pika,json,os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()
from movies.models import Movie
from pika.connection import PRODUCT
params=pika.URLParameters('amqps://xfppnauw:fSmY1Xp-KwFXOFnaJ2xUTC6cmjijGOTj@puffin.rmq2.cloudamqp.com/xfppnauw')
connection=pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Received in admin")
    id=json.loads(body)
    print(id)
    movie=Movie.object.get(id=id)
    movie.likes=movie.likes+1
    movie.save()
    print('Movie Likes Increased')



channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)
print("Started Consuming")
channel.start_consuming()
channel.close()