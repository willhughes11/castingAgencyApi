from ..app.app import db, json

class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime, nullable=False)
    casts = db.relationship('Cast', backref='movie', lazy=True)

    def mov_short(self):
        return {
            'id': self.id,
            'title': self.title,
        }

    def mov_long(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    def __repr__(self):
        return f'<Movie ID: {self.id}, Movie Name: {self.title}, Release Date: {self.release_date}>'

class Actor(db.Model):
    __tablename__ = "actor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    casts = db.relationship('Cast', backref='actor', lazy=True)

    def act_short(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def act_long(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
    
    def __repr__(self):
        return f'<Actor ID: {self.id}, Actor Name: {self.name}, Actor Age: {self.age}, Actor Gender: {self.gender}>'

class Cast(db.Model):
    __tablename__ = "movie_cast"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'), nullable=False)
    role = db.Column(db.String)

    def cast_short(self):
        return {
            'id': self.id,
            'role': self.role,
        }

    def cast_long(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'actor_id': self.actor_id,
            'role': self.role
        }

    def __repr__(self):
        return f'<Cast ID: {self.id}, Movie ID: {self.movie_id}, Actor ID: {self.actor_id}, Role: {self.role}>'

def insert(self):
    db.session.add(self)
    db.session.commit()

def update(self):
    db.session.commit()
    
def delete(self):
    db.session.delete(self)
    db.session.commit()