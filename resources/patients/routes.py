from flask import request
from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import get_jwt_identity, jwt_required

from schemas import AuthUserModelSchema, UserModelSchema, UserModelSchemaNested, UserQuesModelSchema, UpdateUserModelSchema
from . import bp
from .UserModel import UserModel


@bp.route('/user')
class UserList(MethodView):

  @bp.response(200, UserModelSchema(many = True))
  def get(self):
    users = UserModel.query.all()
    return users
  
  @jwt_required()
  @bp.arguments(AuthUserModelSchema)
  def delete(self, user_data):
    user_id = get_jwt_identity()
    user = UserModel.query.get(user_id)
    if user and user.username == user_data['username'] and user.check_password(user_data['password']):
      user.delete()
      return {'message':f'{user_data["username"]} deleted'}, 202
    abort(400, message='Username or Password Invalid')

  @jwt_required()
  @bp.arguments(UpdateUserModelSchema)
  @bp.response(202, UserModelSchema)
  def put(self, user_data):
    user_id = get_jwt_identity()
    user = UserModel.query.get_or_404(user_id, description='User Not Found')
    if user and user.check_password(user_data['password']):
      try:
        user.from_dict(user_data)
        user.save()
        return user
      except IntegrityError:
        abort(400, message='Username or Email already Taken')


@bp.route('/user/<user_id>')
class User(MethodView):

  @bp.response(200, UserModelSchemaNested)
  def get(self, user_id):
    user = UserModel.query.get_or_404(user_id, description='User Not Found')
    return user
  
@bp.route('/user/follow/<followed_id>')
class FollowDoctor(MethodView):
  
  @jwt_required()
  @bp.response(200, UserModelSchema(many=True))
  def post(self, followed_id):
    follower_id = get_jwt_identity()
    user = UserModel.query.get(follower_id)
    doctor_to_follow = UserModel.query.get(followed_id)
    if user and doctor_to_follow:
      user.follow_doctor(doctor_to_follow)
      return user.followed.all()
    abort(400, message='Invalid user info')

  @jwt_required()
  def put(self, followed_id):
    follower_id = get_jwt_identity()
    user = UserModel.query.get(follower_id)
    doctor_to_unfollow = UserModel.query.get(followed_id)
    if user and doctor_to_unfollow:
      user.unfollow_doctor(doctor_to_unfollow)
      return {'message': f'User: {doctor_to_unfollow.username} unfollowed'}, 202
    abort(400, message='Invalid user info')  