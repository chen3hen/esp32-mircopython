import time
import ntptime  # 校准时间库

class TIME_TEST():

    def do_update_time():
        ntptime.NTP_DELTA = 3155644800
        ntptime.host = 'ntp1.aliyun.com'
        ntptime.settime()
        print("TIME:%s" %str(time.localtime()))
        # nowtime = time.localtime()
        # print("lock-in time: " + nowtime)        
        # del message