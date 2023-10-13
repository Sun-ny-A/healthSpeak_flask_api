from app import db
from datetime import datetime


#many-to-many relationship b/w doctors and questions
forum_response = db.Table(
    'forum_response',
    db.Column('doctor_id', db.Integer, db.ForeignKey('doctors.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id'))
)

class DoctorAnsModel(db.Model):

    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    forum_answer = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.String, default = datetime.utcnow)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    forum_responses = db.relationship('UserQuesModel', secondary=forum_response, primaryjoin=(forum_response.c.doctor_id == id), secondaryjoin=(forum_response.c.question_id == id), lazy='dynamic', overlaps='forum_responses')


    def __repr__(self):
        return f'<Answer: {self.forum_response}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()