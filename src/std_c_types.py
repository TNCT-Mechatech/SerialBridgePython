#! /usr/bin/env python
# encoding=utf-8
#
# File:     std_c_types.py
#
# Overview:
#   本スプリクトでは、"int"や"double"といった型名を表す文字列と、
#   'i'や'd'といったStructライブラリの指定子の関連付けを行っています。
#
# Author:   TaiyouKomazawa
#

class std_c_types:
    def __init__(self):

        self.types = (
            self.Int8(),
            self.UInt8(),
            self.Int16(),
            self.UInt16(),
            self.Int(),
            self.Int32(),
            self.UInt32(),
            self.Float32(),
            self.Unknown())

    def to_py_struct(self, names):
        s_names = ''
        s_size = 0
        for i in names:
            for j in self.types:
                if i == j.get_t_name():
                    s_names = s_names + j.get_s_name()
                    s_size = s_size + j.size()
                    break
        return (s_names, s_size)

    class Type(object):
        def __init__(self, type_name, type_name_struct, size):
            self._t_name = type_name
            self._s_name = type_name_struct
            self._size = size

        def get_t_name(self):
            return self._t_name

        def get_s_name(self):
            return self._s_name

        def size(self):
            return self._size

    class Int8(Type):
        INT8_SIZE = 1  # byte

        def __init__(self):
            super(std_c_types.Int8, self).__init__("int8_t", "b", self.INT8_SIZE)

    class UInt8(Type):
        UINT8_SIZE = 1  # byte

        def __init__(self):
            super(std_c_types.UInt8, self).__init__("uint8_t", "B", self.UINT8_SIZE)

    class Int16(Type):
        INT16_SIZE = 2  # byte

        def __init__(self):
            super(std_c_types.Int16, self).__init__("int16_t", "h", self.INT16_SIZE)

    class UInt16(Type):
        UINT16_SIZE = 2  # byte

        def __init__(self):
            super(std_c_types.UInt16, self).__init__("uint16_t", "H", self.UINT16_SIZE)

    class Int(Type):
        INT_SIZE = 4  # byte

        def __init__(self):
            super(std_c_types.Int, self).__init__("int", "i", self.INT_SIZE)

    class Int32(Type):
        INT32_SIZE = 4  # byte

        def __init__(self):
            super(std_c_types.Int32, self).__init__("int32_t", "i", self.INT32_SIZE)

    class UInt32(Type):
        UINT32_SIZE = 4  # byte

        def __init__(self):
            super(std_c_types.UInt32, self).__init__("uint32_t", "I", self.UINT32_SIZE)

    class Float32(Type):
        FLOAT32_SIZE = 4  # byte

        def __init__(self):
            super(std_c_types.Float32, self).__init__("float", "f", self.FLOAT32_SIZE)

    class Unknown(Type):
        def __init__(self):
            super(std_c_types.Unknown, self).__init__("*", "x", 0)

        def get_t_name(self):
            self._error()

        def get_s_name(self):
            self._error()

        def size(self):
            self._error()

        def _error(self):
            raise ValueError("Your struct has nuknown data type.")
