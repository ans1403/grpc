# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"\x16\n\x14UserSelectAllRequest\"Q\n\x15UserSelectAllResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x18\n\x04user\x18\x03 \x03(\x0b\x32\n.user.User\"#\n\x15UserSelectByIdRequest\x12\n\n\x02id\x18\x01 \x01(\r\"R\n\x16UserSelectByIdResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x18\n\x04user\x18\x03 \x01(\x0b\x32\n.user.User\"3\n\x04User\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tuser_type\x18\x03 \x01(\r2\xa0\x01\n\x0bUserService\x12\x46\n\tselectAll\x12\x1a.user.UserSelectAllRequest\x1a\x1b.user.UserSelectAllResponse\"\x00\x12I\n\nselectById\x12\x1b.user.UserSelectByIdRequest\x1a\x1c.user.UserSelectByIdResponse\"\x00\x62\x06proto3')



_USERSELECTALLREQUEST = DESCRIPTOR.message_types_by_name['UserSelectAllRequest']
_USERSELECTALLRESPONSE = DESCRIPTOR.message_types_by_name['UserSelectAllResponse']
_USERSELECTBYIDREQUEST = DESCRIPTOR.message_types_by_name['UserSelectByIdRequest']
_USERSELECTBYIDRESPONSE = DESCRIPTOR.message_types_by_name['UserSelectByIdResponse']
_USER = DESCRIPTOR.message_types_by_name['User']
UserSelectAllRequest = _reflection.GeneratedProtocolMessageType('UserSelectAllRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERSELECTALLREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserSelectAllRequest)
  })
_sym_db.RegisterMessage(UserSelectAllRequest)

UserSelectAllResponse = _reflection.GeneratedProtocolMessageType('UserSelectAllResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERSELECTALLRESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserSelectAllResponse)
  })
_sym_db.RegisterMessage(UserSelectAllResponse)

UserSelectByIdRequest = _reflection.GeneratedProtocolMessageType('UserSelectByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERSELECTBYIDREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserSelectByIdRequest)
  })
_sym_db.RegisterMessage(UserSelectByIdRequest)

UserSelectByIdResponse = _reflection.GeneratedProtocolMessageType('UserSelectByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERSELECTBYIDRESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserSelectByIdResponse)
  })
_sym_db.RegisterMessage(UserSelectByIdResponse)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.User)
  })
_sym_db.RegisterMessage(User)

_USERSERVICE = DESCRIPTOR.services_by_name['UserService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERSELECTALLREQUEST._serialized_start=20
  _USERSELECTALLREQUEST._serialized_end=42
  _USERSELECTALLRESPONSE._serialized_start=44
  _USERSELECTALLRESPONSE._serialized_end=125
  _USERSELECTBYIDREQUEST._serialized_start=127
  _USERSELECTBYIDREQUEST._serialized_end=162
  _USERSELECTBYIDRESPONSE._serialized_start=164
  _USERSELECTBYIDRESPONSE._serialized_end=246
  _USER._serialized_start=248
  _USER._serialized_end=299
  _USERSERVICE._serialized_start=302
  _USERSERVICE._serialized_end=462
# @@protoc_insertion_point(module_scope)
