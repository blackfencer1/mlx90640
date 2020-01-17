# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:48:03 2020

@author: user
"""


import smbus
bus = smbus.SMBus(1)

data = bus.read_i2c_block_data(0x33, 32)
        arraySize = len(data)
        print(arraySize)

        num = 0
        while(num != arraySize):
            print(data[num])
            num+= 1
           
  