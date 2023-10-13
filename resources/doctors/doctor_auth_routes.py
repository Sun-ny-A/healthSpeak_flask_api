from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token

from schemas import DoctorModelSchema, AuthDoctorModelSchema
from . import bp
from .DoctorModel import DoctorModel


@bp.route('/register/doctor', methods=['POST'])
@bp.arguments(DoctorModelSchema)
@bp.response(201, DoctorModelSchema)
def register_doctor(doctor_data): #post through auth reg instead of routes
  doctor = DoctorModel()
  doctor.from_dict(doctor_data)
  try:
    doctor.save()
    return doctor_data
  except IntegrityError:
    abort(400, message='Name or Email already Taken')

@bp.post('/login/doctor')
@bp.arguments(AuthDoctorModelSchema)
def login(login_info):
  if 'doctor_name' not in login_info and 'email' not in login_info:
    abort(400, message='Please include name or email!')
  if 'doctor_name' in login_info:
    doctor = DoctorModel.query.filter_by(doctor_name=login_info['doctor_name']).first()
  else:
    doctor = DoctorModel.query.filter_by(email=login_info['email']).first()
  if doctor and doctor.check_password(login_info['password']):
    access_token = create_access_token(identity=doctor.id)
    return {'access_token':access_token}
  abort(400, message='Invalid Name Or Password')