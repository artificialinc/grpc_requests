# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dependency1.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import dependency2_pb2 as dependency2__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x64\x65pendency1.proto\x12\x0c\x64\x65pendencies\x1a\x11\x64\x65pendency2.proto\"H\n\x0b\x44\x65pendency1\x12\x0e\n\x06\x66ield1\x18\x01 \x01(\t\x12)\n\x06\x66ield2\x18\x02 \x01(\x0b\x32\x19.dependencies.Dependency2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dependency1_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DEPENDENCY1']._serialized_start=54
  _globals['_DEPENDENCY1']._serialized_end=126
# @@protoc_insertion_point(module_scope)
