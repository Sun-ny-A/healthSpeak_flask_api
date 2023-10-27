from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from associations.associations import followers,forum_response



class DoctorModel(db.Model):

    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key = True)
    doctor_name = db.Column(db.String, unique=True, nullable=False) 
    specialization = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String)
    accepting_patients = db.Column(db.Boolean, nullable=False)
    profile_bio = db.Column(db.String)
    answers = db.relationship('DoctorAnsModel', back_populates='doctor')

    # Doctors following and being followed
    followed_doctors = db.relationship(
        'DoctorModel',
        secondary=followers,
        primaryjoin=id == followers.c.doctor_follower_id,
        secondaryjoin=id == followers.c.doctor_followed_id,
        back_populates='follower_doctors'
    )
    
    follower_doctors = db.relationship(
        'DoctorModel',
        secondary=followers,
        primaryjoin=id == followers.c.doctor_followed_id,
        secondaryjoin=id == followers.c.doctor_follower_id,
        back_populates='followed_doctors'
    )
    
    
    def __repr__(self):
        return f'<Doctor: {self.doctor_name}'
    
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
    
    def is_following(self, doctor):
       return self.follower_doctors.filter(doctor.id == followers.c.doctor_followed_id).count()>0

    def follow_doctor(self, doctor):
        if not self.is_following(doctor):
            self.followed.append(doctor)
            self.save()
  
    def unfollow_doctor(self, doctor):
        if self.is_following(doctor):
            self.followed.remove(doctor)
            self.save()


    