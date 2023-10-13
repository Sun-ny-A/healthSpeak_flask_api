from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from resources.doctors.DoctorModel import DoctorModel

from .DoctorAnsModel import DoctorAnsModel
from schemas import DoctorAnsModelSchema
from . import bp


@bp.route('/')
class Answerlist(MethodView):

  @jwt_required()
  @bp.response(200, DoctorAnsModelSchema(many=True))
  def get(self):
    return DoctorAnsModel.query.all()

  @jwt_required()
  @bp.arguments(DoctorAnsModelSchema)
  @bp.response(200, DoctorAnsModelSchema)
  def post (self, answer_data): #input validation
    doctor_id = get_jwt_identity()
    p = DoctorAnsModel(**answer_data)
    u = DoctorModel.query.get(doctor_id)
    if u:
      p.save()
      return p
    else:
      abort(400, message="Invalid Doctor Id")

@bp.route('/<answer_id>')
class Answer(MethodView):

  @bp.response(200, DoctorAnsModelSchema)
  def get(self, answer_id):
    p = DoctorAnsModel.query.get(answer_id)
    if p:
      return p
    abort(400, message='Invalid answer id')

  @jwt_required()
  @bp.arguments(DoctorAnsModelSchema)
  @bp.response(200, DoctorAnsModelSchema)
  def put(self, answer_data, answer_id): #input validation
    p = DoctorAnsModel.query.get(answer_id)
    if p and answer_data['forum_answer']:
      doctor_id = get_jwt_identity()
      if p.doctor_id == doctor_id:
        p.forum_answer = answer_data['forum_answer']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Post Data')

  # @bp.arguments(DoctorAnsModelSchema)
  # @bp.response(200, DoctorAnsModelSchema)
  # def put(self, answer_data, answer_id): #input validation
  #   if answer_id in answers:
  #     answer = answers[answer_id]
  #     if answer_data['doctor_id'] != answer['doctor_id']:
  #       abort(400, message='Cannot edit another doctor\'s response. Please provide a valid id.')
  #     if answer_data['doctor_name'] != answer['doctor_name']:
  #       abort(400, message='Cannot edit another doctor\'s response. Please provide a valid name.')
  #     answer['forum_response'] = answer_data['forum_response']
  #     return answer, 200
  #   abort(404, message='Post not found')

  def delete(self, answer_id):
    doctor_id = get_jwt_identity()
    p = DoctorAnsModel.query.get(answer_id)
    if p:
      if p.doctor_id == doctor_id:
        p.delete()
        return {'message' : 'Post Deleted'}, 202
      abort(400, message='User doesn\'t have rights')
    abort(400, message='Invalid Post Id')