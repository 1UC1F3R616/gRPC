# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users_types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='users_types.proto',
  package='users',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11users_types.proto\x12\x05users\")\n\x04User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\r\"F\n\x11\x43reateUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"-\n\x10\x43reateUserResult\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\",\n\x0fGetUsersRequest\x12\x19\n\x04user\x18\x01 \x03(\x0b\x32\x0b.users.User\"+\n\x0eGetUsersResult\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.Userb\x06proto3')
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='users.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='users.User.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='users.User.user_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=69,
)


_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='users.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='users.CreateUserRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='users.CreateUserRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='users.CreateUserRequest.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=141,
)


_CREATEUSERRESULT = _descriptor.Descriptor(
  name='CreateUserResult',
  full_name='users.CreateUserResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='users.CreateUserResult.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=188,
)


_GETUSERSREQUEST = _descriptor.Descriptor(
  name='GetUsersRequest',
  full_name='users.GetUsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='users.GetUsersRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=234,
)


_GETUSERSRESULT = _descriptor.Descriptor(
  name='GetUsersResult',
  full_name='users.GetUsersResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='users.GetUsersResult.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=279,
)

_CREATEUSERRESULT.fields_by_name['user'].message_type = _USER
_GETUSERSREQUEST.fields_by_name['user'].message_type = _USER
_GETUSERSRESULT.fields_by_name['user'].message_type = _USER
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreateUserResult'] = _CREATEUSERRESULT
DESCRIPTOR.message_types_by_name['GetUsersRequest'] = _GETUSERSREQUEST
DESCRIPTOR.message_types_by_name['GetUsersResult'] = _GETUSERSRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'users_types_pb2'
  # @@protoc_insertion_point(class_scope:users.User)
  })
_sym_db.RegisterMessage(User)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'users_types_pb2'
  # @@protoc_insertion_point(class_scope:users.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserResult = _reflection.GeneratedProtocolMessageType('CreateUserResult', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERRESULT,
  '__module__' : 'users_types_pb2'
  # @@protoc_insertion_point(class_scope:users.CreateUserResult)
  })
_sym_db.RegisterMessage(CreateUserResult)

GetUsersRequest = _reflection.GeneratedProtocolMessageType('GetUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERSREQUEST,
  '__module__' : 'users_types_pb2'
  # @@protoc_insertion_point(class_scope:users.GetUsersRequest)
  })
_sym_db.RegisterMessage(GetUsersRequest)

GetUsersResult = _reflection.GeneratedProtocolMessageType('GetUsersResult', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERSRESULT,
  '__module__' : 'users_types_pb2'
  # @@protoc_insertion_point(class_scope:users.GetUsersResult)
  })
_sym_db.RegisterMessage(GetUsersResult)


# @@protoc_insertion_point(module_scope)
