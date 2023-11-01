from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from resources.patients.UserModel import UserModel

from .UserQuesModel import UserQuesModel
from schemas import UserQuesModelSchema
from . import bp


@bp.route('/')
class QuestionList(MethodView):
  
  @jwt_required()
  @bp.response(200, UserQuesModelSchema(many=True))
  def get(self):
    return UserQuesModel.query.all()

  @jwt_required()
  @bp.arguments(UserQuesModelSchema)
  @bp.response(200, UserQuesModelSchema)
  def post(self, question_data): #input validation
    user_id = get_jwt_identity()
    p = UserQuesModel(**question_data)
    u = UserModel.query.get(user_id)
    if u:
      p.save()
      return p
    else:
      abort(400, message="Invalid username")
  
@bp.route('/<question_id>')
class Question(MethodView):

  @jwt_required()
  @bp.response(200, UserQuesModelSchema)
  def get(self, question_id):
    p = UserQuesModel.query.get(question_id)
    if p:
      return p
    abort(400, message='Invalid question id')

  @jwt_required()
  @bp.arguments(UserQuesModelSchema)#input validation
  @bp.response(200, UserQuesModelSchema)
  def put(self, question_data, question_id): #arguments before dynamic url
    p = UserQuesModel.query.get(question_id)
    if p and question_data['forum_question']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.forum_question = question_data['forum_question']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Post Data')

  def delete(self, question_id):
    user_id = get_jwt_identity()
    p = UserQuesModel.query.get(question_id)
    if p:
      if p.user_id == user_id:
        p.delete()
        return {'message' : 'Post Deleted'}, 202
      abort(400, message='User doesn\'t have rights')
    abort(400, message='Invalid Post Id')