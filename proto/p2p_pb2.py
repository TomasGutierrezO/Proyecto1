# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: p2p.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'p2p.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tp2p.proto\"1\n\x0b\x46ileRequest\x12\x0f\n\x07peer_id\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\"2\n\x10\x46ileListResponse\x12\r\n\x05\x66iles\x18\x01 \x03(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"2\n\x0c\x46ileResponse\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2j\n\nP2PService\x12-\n\x08GetFiles\x12\x0c.FileRequest\x1a\x11.FileListResponse\"\x00\x12-\n\x0c\x44ownloadFile\x12\x0c.FileRequest\x1a\r.FileResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'p2p_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILEREQUEST']._serialized_start=13
  _globals['_FILEREQUEST']._serialized_end=62
  _globals['_FILELISTRESPONSE']._serialized_start=64
  _globals['_FILELISTRESPONSE']._serialized_end=114
  _globals['_FILERESPONSE']._serialized_start=116
  _globals['_FILERESPONSE']._serialized_end=166
  _globals['_P2PSERVICE']._serialized_start=168
  _globals['_P2PSERVICE']._serialized_end=274
# @@protoc_insertion_point(module_scope)
