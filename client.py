# 客户端
import socket
import json
import time


# aes加密
from Crypto.Cipher import AES
from binascii import b2a_base64, a2b_base64
  
class Prpcrypt(object):
    def __init__(self,key):

        self.mode = AES.MODE_CBC
        self.key = self.pad_key(key)
 
    def pad(self,text):
        text = bytes(text,encoding="utf8")
        while len(text) % 16 != 0:
            text += b'\0'
        return text
 
    def pad_key(self,key):
        key = bytes(key, encoding="utf8")
        while len(key) % 16 != 0:
            key += b'\0'
        return key
 
    def encrypt(self,text):
        texts = self.pad(text)
        aes = AES.new(self.key, self.mode,self.key)
        res = aes.encrypt(texts)
        return str(b2a_base64(res),encoding= "utf-8")
        # return str(b2a_base64(res), encoding="utf-8")
 
    def decrypt(self,text):
        texts = a2b_base64(self.pad(text))
        aes = AES.new(self.key, self.mode,self.key)
        res = str(aes.decrypt(texts),encoding="utf8")
        return res
 
 
if __name__ == "__main__":
    # 加密秘钥
    key = "zhika888"

    # socket连接实例化
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接对象
    ret = sock_tcp.connect(("192.168.8.36", 60000))
    #ip地址改为esp32输出的ip

    # 返回0，打印连接成功
    if not ret:
        print("连接成功")

    # 要发送的数据
    Testdict = {"Type":"exec", "cmd":"p26.value(1)"}

    # Testdict = {"Type":"open"}
    # Testdict = {"Type":"close"}
    

    Testdict = json.dumps(Testdict)

    # 加密
    send_text = Prpcrypt(key).encrypt(Testdict)

    # 解密
    get_text = Prpcrypt(key).decrypt(send_text)
    print(send_text)
    X = json.loads(Testdict)
    print(type(X))
    print(get_text)


    # 以utf-8格式发送数据
    sock_tcp.sendall(bytes(send_text, "utf-8"))

    time.sleep(1)