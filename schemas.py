from marshmallow import Schema, fields


class UserQuesModelSchema(Schema):
  id = fields.Str(dump_only=True)#dumping=we are sending info to user--> user is not sending us this (they are required to send forum_question and user_id)
  forum_question = fields.Str(required=True) #input validation
  user_id = fields.Int(dump_only=True) #input validation
  timestamp = fields.Str(dump_only=True)
  doctor_id = fields.Int()
  forum_responses = fields.Nested('DoctorAnsModelSchema', many=True, dump_only=True)

class DoctorAnsModelSchema(Schema):
  id = fields.Str(dump_only=True)
  forum_responses = fields.Str(required=True)#input validation
  doctor_id = fields.Int(dump_only=True)#input validation
  doctor_name = fields.Str(required=True)#input validation
  timestamp = fields.Str(dump_only=True)
  user_id = fields.Int()
  forum_question = fields.Nested('UserQuesModelSchema', many=True, dump_only=True)

class DoctorModelSchema(Schema):
  id = fields.Str(dump_only=True)
  doctor_name = fields.Str(required=True)#input validation
  specialization = fields.Str(required=True)#input validation
  email = fields.Str(required=True)#input validation
  password = fields.Str(required=True, load_only=True)#load_only=not inluded in output/for sensitive info
  phone_number = fields.Str()
  accepting_patients = fields.Bool(required=True)#input validation
  profile_bio = fields.Str()

class DoctorModelSchemaNested(DoctorModelSchema):
  answers = fields.List(fields.Nested(DoctorAnsModelSchema), dump_only=True)
  followed = fields.List(fields.Nested(DoctorModelSchema), dump_only=True)
  following = fields.List(fields.Nested(DoctorModelSchema), dump_only=True)

class UserModelSchema(Schema):
  id = fields.Str(dump_only=True)
  username = fields.Str(required=True)#input validaton
  email = fields.Str(required=True)#input validation
  password = fields.Str(required=True, load_only=True)
  first_name = fields.Str()
  last_name = fields.Str()

class UserModelSchemaNested(UserModelSchema):
  questions = fields.List(fields.Nested(UserQuesModelSchema), dump_only=True)
  following = fields.List(fields.Nested(UserModelSchema), dump_only=True)

class UpdateUserModelSchema(Schema): #no id because we're not using this to send anything
  username = fields.Str()#not required-> user has option to send username or email
  email = fields.Str()
  password = fields.Str(required=True, load_only=True)
  new_password = fields.Str()
  first_name = fields.Str()
  last_name = fields.Str()

class UpdateDoctorModelSchema(Schema):
  doctor_name = fields.Str()
  specialization = fields.Str()
  email = fields.Str()
  password = fields.Str(required=True, load_only=True)
  new_password = fields.Str()
  phone_number = fields.Str()
  accepting_patients = fields.Bool()
  profile_bio = fields.Str()

class AuthUserModelSchema(Schema):
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(required = True, load_only = True)

class AuthDoctorModelSchema(Schema):
  doctor_name = fields.Str()
  email = fields.Str()
  password = fields.Str(required = True, load_only = True)