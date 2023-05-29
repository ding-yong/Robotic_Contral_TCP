# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/10/27 14:53 
# ide： PyCharm
import os, sys, inspect
import pandas as pd
import serial
import time
import glove_con

while(1):
    data = glove_con.loop()
    data_y=float(data[0])/10
    data_x=float(data[1])/10
    data_z=float(data[2])/10
    data_figer1=float(data[4])-float(6400)
    if data_figer1<0:
        data_figer1=float(0)
    data_figer2=float(data[6])-float(4760)
    if data_figer2<0:
        data_figer2=float(0)
    data_figer3=float(data[9])-float(5800)
    if data_figer3<0:
        data_figer3=float(0)

    print(data_y,data_x,data_z,data_figer1,data_figer2,data_figer3)
