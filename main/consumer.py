import pika,json
from main import Movie,db
params=pika.URLParameters('amqps://xfppnauw:fSmY1Xp-KwFXOFnaJ2xUTC6cmjijGOTj@puffin.rmq2.cloudamqp.com/xfppnauw')
connection=pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("Received in main")
    data=json.loads(body)
    print(data)
    if properties.content_type == "movie_created":
        movie=Movie(id = data["id"], title=data["title"], image=data["image"])
        db.session.add(movie)
        db.session.commit()
        print("Movie Created")

    elif properties.content_type == "movie_updated":
        movie = Movie.query.get(data['id'])
        movie.title = data["title"]
        movie.image = data["image"]
        db.session.commit()
        print("Movie Updated")

    elif properties.content_type == "movie_deleted":
        movie = Movie.query.get(data)
        db.session.delete(movie)
        db.session.commit()
        print("Movie Deleted")

channel.basic_consume(queue='main', on_message_callback=callback,auto_ack=True)
print("Started Consuming")
channel.start_consuming()
channel.close()