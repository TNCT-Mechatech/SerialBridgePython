#! /usr/bin/env python

import time
import sys
sys.path.append("../")

import src.message as msg
import src.serial_bridge as pb
import src.bools as bools

buttons = msg.Message("./buttons.yml",(bools.Bools8Type,bools.Bools16Type))

swh0 = bools.Bools8Type
swh1 = bools.Bools8Type

dev = pb.SerialBridge("TestBools", 16, "ttyS")

dev.add_frame(buttons)

while(True):
    print(dev.recv())
    swh0.data.set_bytes(buttons.data.sw0)
    swh1.data.set_bytes(buttons.data.sw1)
    print(swh0.data.get_bits())
    print(swh1.data.get_bits())
    time.sleep(0.020)