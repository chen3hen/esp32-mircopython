from wificonnect import WIFI_TEST
from dht11 import *
from socket_srv import TCPLINK_TEST
# from bluetooth_mould import *
from machine import Pin

import socket
import _thread
import json
import array

WIFI_TEST.do_connect()

global p0
# GPIO 0
p0 = Pin(0, Pin.OUT)

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

#温湿度输入读取
global p23
p23 = Pin(23, Pin.IN)

# 连接WiFi
#WIFI_TEST.do_connect()

# 温度和湿度
do_dht()

# TCP服务器
tcplink = TCPLINK_TEST()
tcplink.do_tcplink()

# 连接蓝牙
# do_blutooth()
