#! /usr/bin/env python
# encoding=utf-8
#
# File:     Message.py
#
# Overview:
#   本スプリクトでは、serial_bridgeに渡すメッセージの生成を行います。
#
# Author:   TaiyouKomazawa
#

import struct
from collections import namedtuple

import src.std_c_types as sct
import src.LoadStruct as ls


class Message:
    def __init__(self, msg_path):
        loadStruct = ls.LoadStruct(msg_path)
        str_list = loadStruct.get_struct()

        names = [i[0] for i in str_list.get_variable_list()]
        types = [i[1] for i in str_list.get_variable_list()]
        str_types = sct.std_c_types().to_py_struct(types)

        self._msg_id = str_list.get_msg_id()
        self._size = str_types[1]
        self._struct = struct.Struct('<' + str_types[0])

        self.Data = namedtuple('Data', names)

    def set(self, **args):
        self.data = self.Data(**args)

    def msg_id(self):
        return self._msg_id

    def size(self):
        return self._size

    def _write_bytes(self):
        return self._struct.pack(*self.data)

    def _read_bytes(self, data):
        self.data = self.Data(*self._struct.unpack(data))  # [0:self._size]
