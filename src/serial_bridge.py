#! /usr/bin/env python
#encoding=utf-8
#
# File:     serial_bridge.py
# 
# Author:   TaiyouKomazawa
#

import sys
import serial
import time

from src.message import Message

class SerialBridge:
    BAUD_RATE = 9600

    HEDER_LEN = 2
    FOOTER_LEN = 2

    STRUCT_MAX_NUM  = 5

    #制御用のcharacter
    HEADER      =':'
    END         ='\n'

    #Message objects
    _strs = []

    def __init__(self, device_name, serach_range=5, tty_head="ttyUSB", serach_min=0):
        self.dev = self._search_node(device_name, serach_range, tty_head, min_num=serach_min)

    def _write(self, data):
        self.dev.write(str(data))
        return sum(ord(i) for i in data)

    def _read(self, size = 1):
        result = self.dev.read(size)
        return sum(ord(i) for i in result), result

    def close(self):
        self.dev.close()

    def add_frame(self, message):
        if len(self._strs) >= self.STRUCT_MAX_NUM:
            return None #error!
        self._strs.append(message)

    def send(self, id, message):
        data_sum = 0
        data_sum += self._write(self.HEADER)
        data_sum += self._write(chr(id))
        data_sum += self._write(chr(message.msg_id()))
        data_sum += self._write(message._write_bytes())
        data_sum += ord(self.END)
        self._write(chr(data_sum & 0xFF)+self.END)

    def recv(self):
        [check_sum, got_char] = self._read()
        if got_char == self.HEADER:
            tmp = self._read(self.HEDER_LEN)
            id = ord(tmp[1][0])
            msg_id = ord(tmp[1][1])
            check_sum += tmp[0]
            if id >= self.STRUCT_MAX_NUM:
                return -1
            if msg_id != self._strs[id].msg_id():
                return -1
            
            tmp = self._read(self._strs[id].size())
            data = tmp[1]
            check_sum += tmp[0]
            tmp = self._read(self.FOOTER_LEN)
            data_sum = ord(tmp[1][0])
            frame_end = tmp[1][1]
            check_sum += tmp[0]
            if frame_end != self.END:
                return -1

            check_sum = (check_sum - data_sum) & 0xFF

            if (check_sum - data_sum) == 0:
                self._strs[id]._read_bytes(data)
                return id
            else:
                return -1
        else:
            return -1

    def _search_node(self, name, num, tty_head="ttyUSB", timeout=3.0, retries=3, min_num=0):
        for i in range(retries):
            for j in range(min_num,num):
                file_path = ''.join(['/dev/', tty_head, str(j)])
                try:
                    dev = serial.Serial(file_path, 9600, timeout=1.0, exclusive=True)
                    t = time.time()
                    while (time.time() - t) < timeout:
                        got_name = dev.readline().decode()
                        if name in got_name:
                            print(file_path+" is "+name+"-SerialBridgeNode.")
                            for w in 'OK\n':
                                dev.write(w.encode())
                            return dev
                except:
                    pass
            time.sleep(0.05)
        raise Exception("Your SerialBridgeNode is not found!")