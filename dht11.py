import dht
from machine import Pin

def do_dht():
    d = dht.DHT11(Pin(23))
    d.measure()
    temp = d.temperature() # eg. 23 (°C)
    hum = d.humidity()    # eg. 41 (% RH)

    print("\n   Temp: {} C, Hum: {} %".format(temp, hum))