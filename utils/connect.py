import network
from utils.sleep import sleep
from config import WIFI_SSID, WIFI_PASSWORD


def connect(n=3):
    # 连接网络
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    while not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        sleep(6)
        n -= 1
        
        if n < 0:
            break
        
    if not wlan.isconnected():
        return {"msg": "连接失败", "status": False}
    else:
        return {"msg": wlan.ifconfig(), "status": True}
