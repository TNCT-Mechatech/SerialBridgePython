#! /usr/bin/env python
#encoding=utf-8
#
# File:     Message.py
#
# Overview:
#   本スプリクトでは、serial_bridgeに渡すメッセージの生成を行います。
#
# Author:   TaiyouKomazawa
#

import struct

import std_c_types as sct
import LoadStruct as ls

class Message():
    def __init__(self, msg_path):
        loadStruct = ls.LoadStruct(msg_path)
        str_list = loadStruct.get_struct()

        types = [i[1] for i in str_list.get_variable_list()]
        str_types = sct.std_c_types().to_py_struct(types)

        self._msg_id = str_list.get_msg_id()
        self._size = str_types[1]
        self._strcut = struct.Struct('<'+str_types[0])

    def msg_id(self):
        return self._msg_id
    def size(self):
        return self._size

    def write_bytes(self, data):
        return self._strcut.pack(*data)

    def read_bytes(self, data):
        return self._strcut.unpack(data)[0:self._size]

