import network
import utime

class WIFI_TEST():

    # 连网
    def do_connect():

        # WiFi账户和密码
        ssid = "test"
        password = "zhika888"

        # 以工作站 (station) 模式运行，需要创建一个工作站Wi-Fi接口的实例
        # 工作站模式（ESP32连接到路由器）， AP模式提供接入服务（其他设备连接到ESP32）。
        sta_if = network.WLAN(network.STA_IF)

        if not sta_if.isconnected():
            print('\n   connecting to network...')
            sta_if.active(True)    
            # 使用connect方法连接到Wi-Fi网络。该方法以SSID（网络名称）和密码作为输入值
            sta_if.connect(ssid, password)
            while not sta_if.isconnected():
                utime.sleep(1)
                print('   connecting ...')

        IP_info=sta_if.ifconfig()
        print("\n   IP: "+IP_info[0])
        print("   Subnet Mask: "+IP_info[1])
        print("   GateWay: "+IP_info[2])
        print("   DNS: "+IP_info[3])