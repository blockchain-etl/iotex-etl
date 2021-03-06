# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/types/transaction_log.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/types/transaction_log.proto',
  package='iotextypes',
  syntax='proto3',
  serialized_options=b'\n\"com.github.iotexproject.grpc.typesP\001Z5github.com/iotexproject/iotex-proto/golang/iotextypes',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!proto/types/transaction_log.proto\x12\niotextypes\"\xfa\x01\n\x0eTransactionLog\x12\x12\n\nactionHash\x18\x01 \x01(\x0c\x12\x17\n\x0fnumTransactions\x18\x02 \x01(\x04\x12<\n\x0ctransactions\x18\x03 \x03(\x0b\x32&.iotextypes.TransactionLog.Transaction\x1a}\n\x0bTransaction\x12\r\n\x05topic\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x11\n\trecipient\x18\x04 \x01(\t\x12,\n\x04type\x18\x05 \x01(\x0e\x32\x1e.iotextypes.TransactionLogType\";\n\x0fTransactionLogs\x12(\n\x04logs\x18\x01 \x03(\x0b\x32\x1a.iotextypes.TransactionLog*\x87\x02\n\x12TransactionLogType\x12\x18\n\x14IN_CONTRACT_TRANSFER\x10\x00\x12\x13\n\x0fWITHDRAW_BUCKET\x10\x01\x12\x11\n\rCREATE_BUCKET\x10\x02\x12\x15\n\x11\x44\x45POSIT_TO_BUCKET\x10\x03\x12\x18\n\x14\x43\x41NDIDATE_SELF_STAKE\x10\x04\x12\x1e\n\x1a\x43\x41NDIDATE_REGISTRATION_FEE\x10\x05\x12\x0b\n\x07GAS_FEE\x10\x06\x12\x13\n\x0fNATIVE_TRANSFER\x10\x07\x12\x1d\n\x19\x44\x45POSIT_TO_REWARDING_FUND\x10\x08\x12\x1d\n\x19\x43LAIM_FROM_REWARDING_FUND\x10\tB]\n\"com.github.iotexproject.grpc.typesP\x01Z5github.com/iotexproject/iotex-proto/golang/iotextypesb\x06proto3'
)

_TRANSACTIONLOGTYPE = _descriptor.EnumDescriptor(
  name='TransactionLogType',
  full_name='iotextypes.TransactionLogType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IN_CONTRACT_TRANSFER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WITHDRAW_BUCKET', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE_BUCKET', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPOSIT_TO_BUCKET', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANDIDATE_SELF_STAKE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANDIDATE_REGISTRATION_FEE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GAS_FEE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NATIVE_TRANSFER', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPOSIT_TO_REWARDING_FUND', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLAIM_FROM_REWARDING_FUND', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=364,
  serialized_end=627,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONLOGTYPE)

TransactionLogType = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONLOGTYPE)
IN_CONTRACT_TRANSFER = 0
WITHDRAW_BUCKET = 1
CREATE_BUCKET = 2
DEPOSIT_TO_BUCKET = 3
CANDIDATE_SELF_STAKE = 4
CANDIDATE_REGISTRATION_FEE = 5
GAS_FEE = 6
NATIVE_TRANSFER = 7
DEPOSIT_TO_REWARDING_FUND = 8
CLAIM_FROM_REWARDING_FUND = 9



_TRANSACTIONLOG_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='iotextypes.TransactionLog.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='iotextypes.TransactionLog.Transaction.topic', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='iotextypes.TransactionLog.Transaction.amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='iotextypes.TransactionLog.Transaction.sender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='iotextypes.TransactionLog.Transaction.recipient', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='iotextypes.TransactionLog.Transaction.type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=175,
  serialized_end=300,
)

_TRANSACTIONLOG = _descriptor.Descriptor(
  name='TransactionLog',
  full_name='iotextypes.TransactionLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionHash', full_name='iotextypes.TransactionLog.actionHash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numTransactions', full_name='iotextypes.TransactionLog.numTransactions', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactions', full_name='iotextypes.TransactionLog.transactions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TRANSACTIONLOG_TRANSACTION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=300,
)


_TRANSACTIONLOGS = _descriptor.Descriptor(
  name='TransactionLogs',
  full_name='iotextypes.TransactionLogs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='logs', full_name='iotextypes.TransactionLogs.logs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=302,
  serialized_end=361,
)

_TRANSACTIONLOG_TRANSACTION.fields_by_name['type'].enum_type = _TRANSACTIONLOGTYPE
_TRANSACTIONLOG_TRANSACTION.containing_type = _TRANSACTIONLOG
_TRANSACTIONLOG.fields_by_name['transactions'].message_type = _TRANSACTIONLOG_TRANSACTION
_TRANSACTIONLOGS.fields_by_name['logs'].message_type = _TRANSACTIONLOG
DESCRIPTOR.message_types_by_name['TransactionLog'] = _TRANSACTIONLOG
DESCRIPTOR.message_types_by_name['TransactionLogs'] = _TRANSACTIONLOGS
DESCRIPTOR.enum_types_by_name['TransactionLogType'] = _TRANSACTIONLOGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionLog = _reflection.GeneratedProtocolMessageType('TransactionLog', (_message.Message,), {

  'Transaction' : _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
    'DESCRIPTOR' : _TRANSACTIONLOG_TRANSACTION,
    '__module__' : 'proto.types.transaction_log_pb2'
    # @@protoc_insertion_point(class_scope:iotextypes.TransactionLog.Transaction)
    })
  ,
  'DESCRIPTOR' : _TRANSACTIONLOG,
  '__module__' : 'proto.types.transaction_log_pb2'
  # @@protoc_insertion_point(class_scope:iotextypes.TransactionLog)
  })
_sym_db.RegisterMessage(TransactionLog)
_sym_db.RegisterMessage(TransactionLog.Transaction)

TransactionLogs = _reflection.GeneratedProtocolMessageType('TransactionLogs', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONLOGS,
  '__module__' : 'proto.types.transaction_log_pb2'
  # @@protoc_insertion_point(class_scope:iotextypes.TransactionLogs)
  })
_sym_db.RegisterMessage(TransactionLogs)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
