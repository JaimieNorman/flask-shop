from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from pyapp import db, loginManager
from datetime import datetime
from flask_login import UserMixin


@loginManager.user_loader
def loadUser(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    image_file = db.Column(db.String(32), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # backref is similar to adding another column to the post model and lazy loads the data in one go
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        # Function to determine how the 'User' will look when printed out
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        # Function to determine how the 'Post' will look when printed out
        return f"Post('{self.title}', '{self.date_posted}')"


class StoreItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.DECIMAL, nullable=False)
    image = db.Column(db.String(32), nullable=False, default='default_item.jpg')
    sale = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        # Function to determine how the 'StoreItem' will look when printed out
        return f"StoreItem('{self.name}', '{self.price}', '{self.image}')"


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    marital_state = db.Column(db.String(16), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    race = db.Column(db.String(128), nullable=False)
    nationality = db.Column(db.String(128), nullable=False)
    blood_group = db.Column(db.String(2), nullable=False)
    organ_donor = db.Column(db.BOOLEAN, nullable=False)
    disabilities = db.Column(db.String(128), nullable=False, default='None')
    occupation = db.Column(db.String(128), nullable=False)
    street_address = db.Column(db.String(128), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(128), nullable=False)
    province = db.Column(db.String(128), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    progress_notes = db.relationship('ProgressNote', backref='progress_report', lazy=True)


class ProgressNote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    hospital = db.Column(db.String(128), nullable=False)
    ward = db.Column(db.String(100), nullable=False)
    progress_note = db.Column(db.Text)
    investigation = db.Column(db.Text)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
