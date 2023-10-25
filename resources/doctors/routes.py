
from flask import request
from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import get_jwt_identity, jwt_required

from schemas import DoctorAnsModelSchema, DoctorModelSchema, DoctorModelSchemaNested, UpdateDoctorModelSchema, AuthDoctorModelSchema
from . import bp
from .DoctorModel import DoctorModel


@bp.route('/doctor')
class DoctorList(MethodView):

  @bp.response(200, DoctorModelSchema(many = True))
  def get(self):
    doctors = DoctorModel.query.all()
    return doctors


  @jwt_required()
  @bp.arguments(AuthDoctorModelSchema)
  def delete(self, doctor_data):
    doctor_id = get_jwt_identity()
    doctor = DoctorModel.query.get(doctor_id)
    if doctor and doctor.doctor_name == doctor_data['doctor_name'] and doctor.check_password(doctor_data['password']):
      doctor.delete()
      return {'message':f'{doctor_data["email"]} deleted'}, 202
    abort(400, message='Name or password invalid')

  @jwt_required()
  @bp.arguments(UpdateDoctorModelSchema)
  @bp.response(202, DoctorModelSchema)
  def put(self, doctor_data):
    doctor_id = get_jwt_identity()
    doctor = DoctorModel.query.get_or_404(doctor_id, description='Doctor Not Found')
    if doctor and doctor.check_password(doctor_data['password']):
      try:
        doctor.from_dict(doctor_data)
        doctor.save()
        return doctor
      except IntegrityError:
        abort(400, message='Name or Email already Taken')


@bp.route('/doctor/<doctor_id>')
class Doctor(MethodView):

  @bp.response(200, DoctorModelSchemaNested)
  def get(self, doctor_id):
    if doctor_id.isdigit():
      doctor = DoctorModel.query.get(doctor_id)
    else:
      doctor = DoctorModel.query.filter_by(doctor_name=doctor_id).first()
    if doctor:
      return doctor
    abort(400, message="Please enter valid name or id")

@bp.route('/doctor/follow/<followed_id>')
class FollowDoctor(MethodView):
  
  @jwt_required()
  @bp.response(200, DoctorModelSchema(many=True))
  def post(self, followed_id):
    follower_id = get_jwt_identity()
    doctor = DoctorModel.query.get(follower_id)
    doctor_to_follow = DoctorModel.query.get(followed_id)
    if doctor and doctor_to_follow:
      doctor.follow_doctor(doctor_to_follow)
      return doctor.followed.all()
    abort(400, message='Invalid user info')

  @jwt_required()
  def put(self, followed_id):
    follower_id = get_jwt_identity()
    doctor = DoctorModel.query.get(follower_id)
    doctor_to_unfollow = DoctorModel.query.get(followed_id)
    if doctor and doctor_to_unfollow:
      doctor.unfollow_doctor(doctor_to_unfollow)
      return {'message': f'User: {doctor_to_unfollow.username} unfollowed'}, 202
    abort(400, message='Invalid user info')  