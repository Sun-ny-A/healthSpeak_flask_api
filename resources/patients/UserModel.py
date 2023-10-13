from app import db
from resources.doctors.DoctorModel import followers
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    questions = db.relationship('UserQuesModel', backref='author', lazy='dynamic', cascade='all, delete')
    following_doctors = db.relationship(
        'DoctorModel',
        secondary=followers,
        primaryjoin=(followers.c.user_id == id) & (followers.c.doctor_followed_id == id),
        secondaryjoin=(followers.c.user_id == id) & (followers.c.doctor_followed_id == id),
        backref=db.backref('user_followers', lazy='dynamic'),
        lazy='dynamic')

    def __repr__(self):
        return f'<User: {self.username}'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
     return check_password_hash(self.password_hash, password)
    
    def from_dict(self, dict):
        password = dict.pop('password')
        self.hash_password(password)
        for k,v in dict.items():
           setattr(self, k,v )
    
    def save(self):
       db.session.add(self)
       db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def is_following_doctor(self, doctor):
        return self.following_doctors.filter(doctor.id == followers.c.doctor_followed_id).count() > 0

    def follow_doctor(self, doctor):
        if not self.is_following_doctor(doctor):
            self.following_doctors.append(doctor)
            self.save()

    def unfollow_doctor(self, doctor):
        if self.is_following_doctor(doctor):
            self.following_doctors.remove(doctor)
            self.save()