from flask import Flask, json,jsonify,abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_cors import CORS
from dataclasses import dataclass
import requests
from producer import publish


app=Flask(__name__)
app.config["SQLALCHEMY_DATABSE_URI"]='mysql://root:root@db/main'
CORS(app)
db = SQLAlchemy(app)
@dataclass
class Movie(db.Model):
    id: int
    title: str
    image : str
    id = db.Column(db.Integer, primary_key= True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
@dataclass
class Movieuser(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    UniqueConstraint('user_id', 'movie_id', name = 'user_movie_unique')


@app.route('/api/movies')
def index():
    return jsonify(Movie.query.all())

@app.route('/api/movies/<int:id>/like')
def like(id):
    req=requests.get("http://docker.for.windows.localhost:8000/api/user")
    json=req.json()
    try:
        movieUser=Movieuser(user_id=json['id'],movie_id=id)
        db.session.add(movieUser)
        db.session.commit()
        publish("movie_liked",id)
    except:
        abort(400,"you already liked this movie")

    return jsonify({
        'message':'success'
    })

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')