from app import db
from datetime import datetime
from associations.associations import followers,forum_response



class UserQuesModel(db.Model):

  __tablename__ = 'questions'
 
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  forum_question = db.Column(db.String, nullable = False)
  timestamp = db.Column(db.String, default = datetime.utcnow)
  doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
  forum_responses = db.relationship('DoctorAnsModel', secondary=forum_response, back_populates='forum_responses')
  

  def __repr__(self):
    return f'<Question:{self.forum_question}>'
  
  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()