from datetime import datetime
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# User model to manage user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Post model to handle diary entries
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)  # Date in ISO format (YYYY-MM-DD)
    project = db.Column(db.String(150), nullable=False)
    what_i_did = db.Column(db.Text, nullable=False)
    what_i_learned = db.Column(db.Text, nullable=False)
    next_steps = db.Column(db.Text)
    mood = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key linking to User
    user = db.relationship('User', backref=db.backref('posts', lazy=True))  # One-to-many relationship

    def __repr__(self):
        return f'<Post {self.project} by {self.user.username}>'
        
        
        



