from app import db
from datetime import datetime
from associations.associations  import followers,forum_response


class DoctorAnsModel(db.Model):

    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    forum_answer = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))

    # Explicit relationship with doctors
    doctor = db.relationship('DoctorModel', back_populates='answers')
    forum_responses = db.relationship('UserQuesModel', secondary=forum_response, back_populates='forum_responses')


    def __repr__(self):
        return f'<Answer: {self.forum_response}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()