# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: carrierId.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63\x61rrierId.proto\x12\x15\x63\x61rrierIdentification\"T\n\x0b\x43\x61rrierList\x12\x34\n\ncarrier_id\x18\x01 \x03(\x0b\x32 .carrierIdentification.CarrierId\x12\x0f\n\x07version\x18\x02 \x01(\x05\"\x98\x01\n\tCarrierId\x12\x14\n\x0c\x63\x61nonical_id\x18\x01 \x01(\x05\x12\x14\n\x0c\x63\x61rrier_name\x18\x02 \x01(\t\x12\x42\n\x11\x63\x61rrier_attribute\x18\x03 \x03(\x0b\x32\'.carrierIdentification.CarrierAttribute\x12\x1b\n\x13parent_canonical_id\x18\x04 \x01(\x05\"\xc9\x01\n\x10\x43\x61rrierAttribute\x12\x14\n\x0cmccmnc_tuple\x18\x01 \x03(\t\x12\x1c\n\x14imsi_prefix_xpattern\x18\x02 \x03(\t\x12\x0b\n\x03spn\x18\x03 \x03(\t\x12\x0c\n\x04plmn\x18\x04 \x03(\t\x12\x0c\n\x04gid1\x18\x05 \x03(\t\x12\x0c\n\x04gid2\x18\x06 \x03(\t\x12\x15\n\rpreferred_apn\x18\x07 \x03(\t\x12\x14\n\x0ciccid_prefix\x18\x08 \x03(\t\x12\x1d\n\x15privilege_access_rule\x18\t \x03(\t')



_CARRIERLIST = DESCRIPTOR.message_types_by_name['CarrierList']
_CARRIERID = DESCRIPTOR.message_types_by_name['CarrierId']
_CARRIERATTRIBUTE = DESCRIPTOR.message_types_by_name['CarrierAttribute']
CarrierList = _reflection.GeneratedProtocolMessageType('CarrierList', (_message.Message,), {
  'DESCRIPTOR' : _CARRIERLIST,
  '__module__' : 'carrierId_pb2'
  # @@protoc_insertion_point(class_scope:carrierIdentification.CarrierList)
  })
_sym_db.RegisterMessage(CarrierList)

CarrierId = _reflection.GeneratedProtocolMessageType('CarrierId', (_message.Message,), {
  'DESCRIPTOR' : _CARRIERID,
  '__module__' : 'carrierId_pb2'
  # @@protoc_insertion_point(class_scope:carrierIdentification.CarrierId)
  })
_sym_db.RegisterMessage(CarrierId)

CarrierAttribute = _reflection.GeneratedProtocolMessageType('CarrierAttribute', (_message.Message,), {
  'DESCRIPTOR' : _CARRIERATTRIBUTE,
  '__module__' : 'carrierId_pb2'
  # @@protoc_insertion_point(class_scope:carrierIdentification.CarrierAttribute)
  })
_sym_db.RegisterMessage(CarrierAttribute)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CARRIERLIST._serialized_start=42
  _CARRIERLIST._serialized_end=126
  _CARRIERID._serialized_start=129
  _CARRIERID._serialized_end=281
  _CARRIERATTRIBUTE._serialized_start=284
  _CARRIERATTRIBUTE._serialized_end=485
# @@protoc_insertion_point(module_scope)
