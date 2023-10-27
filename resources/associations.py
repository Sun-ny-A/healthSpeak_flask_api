from app import db

# Many-to-many relationship b/w doctors and questions
forum_response = db.Table(
    'forum_response',
    db.Column('doctor_id', db.Integer, db.ForeignKey('doctors.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id'))
)

# Many-to-many relationship among doctors following and being followed by each other
followers = db.Table(
    'followers',
    db.Column('doctor_follower_id', db.Integer, db.ForeignKey('doctors.id')),
    db.Column('doctor_followed_id', db.Integer, db.ForeignKey('doctors.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)



