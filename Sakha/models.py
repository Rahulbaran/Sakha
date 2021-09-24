from datetime import datetime
from flask_login import UserMixin
from Sakha import db, login_manager




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    gender = db.Column(db.Text, nullable=False)
    account_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    dob = db.Column(db.DateTime)
    about_user = db.Column(db.Text)
    profile_pic = db.Column(db.String(100), nullable=False, default='default.png')
    header_pic = db.Column(db.String(100), nullable=False, default='header.jpg')