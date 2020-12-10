#! /usr/bin/env python

import time
import sys
sys.path.append("../")

import src.message as msg
import src.serial_bridge as pb

vect1 = msg.Message("./vector3.yml")
vect2 = msg.Message("./vector3.yml")
dev = pb.SerialBridge("TestVect3", 16, "ttyS")

dev.add_frame(vect2)

while(True):
    vect1.set(x= 0.321, y = 0.654, z = 0.123)
    dev.send(0, vect1)
    print(dev.recv())
    print(vect2.data.x)
    print(vect2.data.y)
    print(vect2.data.z)
    time.sleep(0.020)