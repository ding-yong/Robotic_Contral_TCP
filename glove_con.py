# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/10/23 16:22
# ide： PyCharm
import os, sys, inspect
import pandas as pd
import serial
import time


def port_get(port, bps, time):  # port：端口号，bps：波特率，time：超时时间
    try:
        ser = serial.Serial(port, bps, timeout=time)  # 打开串口
        print("串口已连接，当前串口：{0}".format(port))
        print("串口详情参数：", ser)

        return ser
    except Exception as e:  # 如果出现异常
        print("串口连接失败，失败分析:", e)


def serload(ser):
    if ser.in_waiting:
        str1 = ser.readline().decode("utf-8")  # 读一行，以/n结束。

        # char1 = ser.read(size=1).hex()  # 从串口读size个字节
        return str1


def _split(_sig):
    dst = str.split(_sig[:-3], ",")
    if len(dst) != 15:
        print("dst!=15")
        return False
    else:
        return dst


portx = "COM6"  # input('输入端口号')  # 例如：端口 = "COM8"
ser = port_get(portx, 115200, None)


def loop():
    while 1:
        ser.flushInput()  # 清空串口输入缓冲区
        sig = serload(ser)
        if sig is None:
            continue
        _data = []
        _data.extend(str.split(sig[:-3], ","))
        # print(_data)
        global data
        data = _data
        return data


def main():
    data = loop()
    print(data)
    print("Press Enter to quit ")
    t = time.time()
    try:
        sys.stdin.readline()
    except KeyboardInterrupt == "q":
        pass
    finally:
        print(time.time() - t)


if __name__ == "__main__":
    main()
