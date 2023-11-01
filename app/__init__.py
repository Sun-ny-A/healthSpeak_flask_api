from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from Config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

from resources.doctors import bp as doctor_bp
api.register_blueprint(doctor_bp)
from resources.patients import bp as patient_bp
api.register_blueprint(patient_bp)
from resources.doctor_ans import bp as answer_bp
api.register_blueprint(answer_bp)
from resources.patient_ques import bp as question_bp
api.register_blueprint(question_bp)

from resources.doctors import routes
from resources.patients import routes
from resources.patient_ques import routes
from resources.doctor_ans import routes

from resources.patients.UserModel import UserModel
from resources.doctors.DoctorModel import DoctorModel
from resources.doctor_ans.DoctorAnsModel import DoctorAnsModel
from resources.patient_ques.UserQuesModel import UserQuesModel