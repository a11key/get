# https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

p = GPIO.PWM(21, 1000)




try:
    
    while True:
        print("Введите коэффициент заполнения")
        dc = float(input())
        voltage = 0.01*3.3*dc
        print("Напряжение: ", voltage, " В")
    
        p.start(dc)




finally:
    GPIO.cleanup()