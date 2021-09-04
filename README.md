环境搭建
python3.8.10
python -m pip install --upgrade pip
pip install esptool


mode		查看COM口


===========================================================
			windows powershell
===========================================================
		清空flash
esptool.py.exe --port COM3 erase_flash
进bin目录

		刷micropython
esptool.py --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 .\esp32-20210715-unstable-v1.16-92-g98c570302-dirty.bin

		安装rshell
pip3 install rshell






				连接开发板
===========================================================


rshell --buffer-size 512 --editor C:\WINDOWS\system32\notepad.exe -p COM3


===========================================================
ls /pyboard/
//运行模式1.boot.py 2.main.py
edit /pyboard/boot.py
新建main.py

cp boot.py /pyboard/boot.py
cp main.py /pyboard/main.py
cp bluetooth_mould.py /pyboard/bluetooth_mould.py
cp wificonnect.py /pyboard/wificonnect.py
cp socket_srv.py /pyboard/socket_srv.py
cp dht22.py /pyboard/dht22.py
cp update_time.py /pyboard/update_time.py

rm /pyboard/main.py	删除指定文件
rm  /pyboard/		删除所有


===========================================================
		repl调试ctrl+x退出		按重启按钮，查看回显
				查看剩余内存
===========================================================	
import gc
gc.mem_free()

用文本编辑器实时编写代码
edit /pyboard/main.py
$:Retrieving / pyboard/main.py ...
$:Updating / pyboard/main.py ...
保存

utime.localtime()


===========================================================
				安装实例
===========================================================
repl
import upip
upip.install("umqtt.simple")

import umqtt.simple


===========================================================
				pwm频率freq = 频率 = hz
===========================================================
pwm可以在所有输出引脚上使用，他们使用同一个频率（范围1~78125HZ）占空比在0~1023之间
duty = 占空比 = 在mircopython里面在0~1023之间

1023/2 = 511.5=50%占空比（duty）
在0~3.3v高低电平中，511占空比=3.3v/50%=1.6v左右
		
		实例
import machine
p4 = machine.Pin(4, machine.Pin.OUT)
pwm4 = machine.PWM(p4)
pwm4.freq(38000)
pwm4.duty(100)


===========================================================
				继电器
===========================================================
低电平触发
machinePin.value(0)开
machinePin.calue(1)关

高电平触发
machinePin.value(0)关
machinePin.calue(1)开

GPIO	两种模式IN OUT
IN:ESP32对应的GPIO口接受外设发送的数据
OUT:ESP对应的GPIO口发送高低电平给外设
import machine
g16 = machine.Pin(16, machine.Pin.OUT)
g16.value()		查看g16端口当前值
g16.value(1)		改为高电平


配置python37或者38环境

电脑端如果加密库Crypto报错

需要进入Python\Python37\Lib\site-packages\crypto
文件名更改为Python\Python37\Lib\site-packages\Crypto

没做配网界面

大约可以支持27个设备


rshell --buffer-size 512 --editor C:\WINDOWS\system32\notepad.exe -p COM6
COM口在设备管理器中查看



