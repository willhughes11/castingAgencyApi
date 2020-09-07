import os
import sys
import psycopg2
from flask_moment import Moment
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import cast, String, func, distinct, ARRAY, DateTime
from sqlalchemy.dialects import postgresql
from flask_migrate import Migrate
from flask_cors import CORS
import json
from .auth.auth import AuthError, requires_auth
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_pyfile('config/config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

from .database.models import Movie, Actor, Cast, update, insert, delete


#----------------------------------------------------------------------------#
# After request decorators to set Access-Control-Allow
#----------------------------------------------------------------------------#
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Headers', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
  response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
  return response

#----------------------------------------------------------------------------#
# Endpoints.
#----------------------------------------------------------------------------#


#  Actors
# ----------------------------------------------------------------

@app.route('/actors')
def get_actors():
  actors = Actor.query.all()

  if len(actors) == 0:
    abort(404)
  
  return jsonify({
    'success': True,
    'actors': [actor.act_short() for actor in actors]
  })

@app.route('/actor-details', methods=['GET'])
@requires_auth('get:actor-details')
def get_actor_details(jwt):
  actors = Actor.query.all()

  if len(actors) == 0:
    abort(404)

  return jsonify({
    'success': True,
    'actors': [actor.act_long() for actor in actors]
  })

@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def create_actors(jwt):
  data = request.get_json()

  if 'name' and 'age' and 'gender' not in data:
    abort(422)
  
  actors = Actor(id=data['id'], name=data['name'], age=data['age'], gender=data['gender'])

  try:
    insert(actors)
  except:
    abort(422)

  return jsonify({
    'success': True,
    'actors': [actors.act_long()]
  })

@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def edit_actors(jwt,actor_id):
  actors = Actor.query.get(actor_id)
  data = request.get_json()

  try:
    if actors is None:
      abort(404)

    if 'name' in data:
      actors.name = data['name']
    if 'age' in data:
      actors.age = data['age']
    if 'gender' in data:
      actors.gender = data['gender']
    update(actors)

  except:
    abort(422)
  
  return jsonify({
    'success': True,
    'actors': [actors.act_long()]
  })

@app.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors(jwt,actor_id):
  try:
    actors = Actor.query.get(actor_id)

    if actors is None:
      abort(404)
    
    delete(actors)

    return jsonify({
      'success': True,
      'deleted': actors.id
    })
  except:
    abort(422)

#  Movies
#  ----------------------------------------------------------------

@app.route('/movies')
def get_movies():
  movies = Movie.query.all()

  if len(movies) == 0:
    abort(404)

  return jsonify({
    'success': True,
    'movies': [movie.mov_short() for movie in movies]
  })

@app.route('/movie-details', methods=['GET'])
@requires_auth('get:movie-details')
def get_movie_details(jwt):
  movies = Movie.query.all()

  if len(movies) == 0:
    abort(404)

  return jsonify({
    'success': True,
    'movies': [movie.mov_long() for movie in movies]
  })

@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def create_movies(jwt):
  data = request.get_json()

  if 'title' and 'release_date' not in data:
    abort(422)
  
  movies = Movie(id=data['id'], title=data['title'], release_date=data['release_date'])

  try:
    insert(movies)
  except:
    abort(422)

  return jsonify({
    'success': True,
    'actors': [movies.mov_long()]
  })

@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def edit_movies(jwt,movie_id):
  movies = Movie.query.get(movie_id)
  data = request.get_json()

  try:
    if movies is None:
      abort(404)

    if 'title' in data:
      movies.title = data['title']
    if 'release_date' in data:
      movies.release_date = data['release_date']
    update(movies)

  except:
    abort(422)

  return jsonify({
      'success': True,
      'actors': [movies.mov_long()]
    })

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(jwt,movie_id):
  try:
    movies = Movie.query.get(movie_id)

    if movies is None:
      abort(404)
    
    delete(movies)

    return jsonify({
      'success': True,
      'deleted': movies.id
    })
  except:
    abort(422)

#  Cast
#  ----------------------------------------------------------------

@app.route('/movie/casts')
def get_movie_cast():
  casts = db.engine.execute('''
  select row_to_json(movie_cast) as movie_cast
  from(
  select b.id as movie_id, b.title as movie_title,
    (select json_agg(actor) as cast
    from (
      select a.id, c.role, a.name from actor as a 
      join movie_cast as c on (a.id = c.actor_id)
    ) actor
    )from movie as b) movie_cast;
  ''')
  cast = [dict(cast) for cast in casts]

  if len(cast) == 0:
    abort(404)
  
  return jsonify(
    cast,
    {'success': True}
    )

@app.route('/actor/roles')
def get_actor_roles():
  roles = db.engine.execute('''
  select row_to_json(movie_cast) as actor_roles
  from(
  select a.id as actor_id, a.name as actor_name,
    (select json_agg(movie) as movie_roles
    from(
      select b.id as movie_id, b.title as movie_title, 
      c.role as movie_role from movie as b
      join movie_cast as c on (a.id = c.actor_id)
    )movie
    )from actor as a
  )movie_cast;
  ''')

  role = [dict(role) for role in roles]

  if len(role) == 0:
    abort(404)

  return jsonify(
    role,
    {'success': True}
  )

#----------------------------------------------------------------------------#
# Error handlers
#----------------------------------------------------------------------------#
  
@app.errorhandler(400)
def bad_request(error):
  return jsonify({
    'success': False,
    'error': 400,
    'message':'bad request'
  }), 400

@app.errorhandler(404)
def not_found(error):
  return jsonify({
    'success': False,
    'error': 404,
    'message':'resource not found'
  }), 404

@app.errorhandler(405)
def not_allowed(error):
  return jsonify({
    'success': False,
    'error': 405,
    'message':'method not allowed'
  }), 405

@app.errorhandler(422)
def unprocessable(error):
  return jsonify({
    'success': False,
    'error': 422,
    'message':'unprocessable'
  }), 422

@app.errorhandler(500)
def server_error(error):
  return jsonify({
    'success': False,
    'error': 500,
    'message':'internal server error'
  }), 500

@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify(
      error.__dict__
    ),401

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)