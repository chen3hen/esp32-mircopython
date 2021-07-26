import socket
import _thread
import json
import array
import os
import ucryptolib
import ubinascii
import uhashlib
from machine import Pin

#全开全关定义
# GPIO 18 5 17 16对应紫蓝绿黄
global p19
p19 = Pin(19, Pin.OUT)

global p18
p18 = Pin(18, Pin.OUT)

global p17
p17 = Pin(17, Pin.OUT)

global p16
p16 = Pin(16, Pin.OUT)

# GPIO 25 26 27 14对应紫蓝绿黄
global p25
p25 = Pin(25, Pin.OUT)

global p26
p26 = Pin(26, Pin.OUT)

global p27
p27 = Pin(27, Pin.OUT)

global p14
p14 = Pin(14, Pin.OUT)



class TCPLINK_TEST():

    def __init__(self):

        # 补全key
        self.key = self.pad_key("zhika888")
        pass

    # 补全key
    def pad_key(self, key):
        key = bytes(key, "utf-8")
        while len(key) % 16 != 0:
            key += b'\0'
        return key

    # TCP_LINK
    def do_tcplink(self):

        # socket连接实例化
        sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 监听允许所有ip连接
        sock_tcp.bind(("0.0.0.0", 60000))

        # 最多100个连接
        sock_tcp.listen(100)

        while True:

            # 开始连接
            print("\n   Start listening....")

            # 别人的IP
            conn, addr = sock_tcp.accept()

            # 多线程，函数名和参数
            _thread.start_new_thread(self.tcplink, (conn, addr))

    # link子函数
    def tcplink(self, conn, addr):
        
        # 打印地址和socket对象
        print("addr: ", addr)
        print("conn: ", conn)

        # 循环读取
        while True:

            # 读取数据
            data = conn.recv(1024)

            # 数据为0，则break
            if not data:
                break

            # 转为2进制
            data = bytes(data,"utf-8")

            # 解密key
            data = self.aesCryptMode(data)

            # 得到数据，并执行cmd
            print(data)

            # 将字符串转化为字典
            recvDict = json.loads(data)

            print(type(recvDict))

            if recvDict["Type"] == "exec":
                print(recvDict["cmd"])

                # 直接运行
                exec(recvDict["cmd"]) 


            #全开
            if recvDict["Type"] == "open":
                p25.value(1)
                p26.value(1)
                p27.value(1)
                p14.value(1)
                p19.value(1)
                p18.value(1)
                p17.value(1)
                p16.value(1)
            #全关
            elif recvDict["Type"] == "close":
                # 直接运行
                p25.value(0)
                p26.value(0)
                p27.value(0) 
                p14.value(0) 
                p19.value(0) 
                p18.value(0) 
                p17.value(0) 
                p16.value(0) 

            else:
                print("error!")

            # if recvDict == "1":
            #     p2.value(1)
            # elif recvDict == "0":
            #     p2.value(0)
            # else:
            #     print("error!")
                  
        # 连接关掉
        conn.close()

    # aes加密和解密
    def aesCryptMode(self, data:bytes,mode="decrypt"):
        '''
        data必须bytes： bytes("data","utf-8")
        eKey: 必须是bytes，而且必须是16位 len(key) == 16;
        '''

        # cbc 使用空格补齐16长度
        padding_len = 16 - len(data) % 16
        data = data + b" " * padding_len

        # 加密
        if mode == "encrypt":

            # 实例化aes加密
            aes = ucryptolib.aes(self.key, 2, self.key)
            encrypt_data = aes.encrypt(data)

            # base64编码的数据
            data = ubinascii.b2a_base64(data)

            # 转换为str值
            str_data = str(data,"utf8")

            return str_data

        elif mode == "decrypt":
            # 解密
            # iv_ = data[0:16]

            # 解码base64编码的数据
            data = ubinascii.a2b_base64(data)

            # 实例化aes加密
            aes = ucryptolib.aes(self.key, 2, self.key)
            data = aes.decrypt(data)

            # 转换为str值
            str_data = str(data,"utf8")

            return str_data
        else:
            print("error:110")