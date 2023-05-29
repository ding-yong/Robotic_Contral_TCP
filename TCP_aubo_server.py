# -*- coding: utf-8 -*-
import socket  # 导入socket模块
import glove_con
import time

host = "192.168.1.167"  # 获取主机地址
print(host)
port = 5001  # 设置端口号
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP/IP套接字
s.bind((host, port))  # 绑定地址(host, port)到套接字
s.listen(1)  # 设置最多连接数
sock, addr = s.accept()  # 被动接收TCP客户端连接
print("连接已建立")

while 1:  # 判断是否退出
    # time.sleep(0.5)
    info = sock.recv(1024).decode()  # 接收客户端数据
    if info:
        print("接收到的内容：" + info)
    if info == "OK":
        data = glove_con.loop()
        data_y = (float(data[0]) - float(1800)) / float(1000)
        data_x = (float(data[1]) - float(1800)) / float(1000)
        data_z = (float(data[2]) - float(1800)) / float(1000)
        print(data_x, data_y, data_z)

        send_data = ",".join([str(data_x), str(data_y), str(data_z)])  # 发送消息
        sock.send(send_data.encode())  # 发送TCP数据


sock.close()  # 关闭客户端套接字
s.close()  # 关闭服务器套接字
