#! /usr/bin/env python
#encoding:utf-8

import time
import sys
sys.path.append("../")

import src.message as msg
import src.serial_bridge as pb

vect1 = msg.Message("./vector3.yml")
dev = pb.SerialBridge("TestSimpleVect3", 16, "ttyS", baud_rate=115200)

dev.add_frame(vect1)

while(True):
    if dev.recv() == 0:
        print(vect1.data.x)
        print(vect1.data.y)
        print(vect1.data.z)
        print(" ")
    time.sleep(0.040)