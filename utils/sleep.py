from machine import Pin
import time


def sleep(n=6):
    """睡眠灯泡闪烁"""
    led = Pin(2, Pin.OUT)

    while True:
        if n <= 0:
            break
            
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

        n -= 2
