from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    character_favorite = db.relationship('CharacterFavorite', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "CharacterFavorite": list(map(lambda x: x.serialize(), self.character_favorite))
        }
            # do not serialize the password, its a security breach
        

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    birth_year = db.Column(db.String(80), nullable=False)
  
    def __repr__(self):
        return '<Character %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            # do not serialize the password, its a security breach
        }

class CharacterFavorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship('User', lazy=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character = db.relationship('Character', lazy=True )
       
    def __repr__(self):
        return '<Character %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "character.id": self.character_id,
         
            # do not serialize the password, its a security breach
        }
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    climate = db.Column(db.String(80), nullable=False)
  
    def __repr__(self):
        return '<Planet %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            # do not serialize the password, its a security breach
        }

class PlanetFavorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship('User', lazy=True)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship('Planet', lazy=True )
       
    def __repr__(self):
        return '<Planet %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "planet.id": self.character_id,
         
            # do not serialize the password, its a security breach
        }
