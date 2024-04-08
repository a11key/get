# https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT) #R-C
GPIO.setup(9, GPIO.OUT) #led

p = GPIO.PWM(9, 1000)




try:
    
    while True:
        print("Введите коэффициент заполнения")
        dc = float(input())
        voltage = 0.01*3.3*dc
        print("Напряжение: ", voltage, " В")
    
        p.start(dc)




finally:
    GPIO.cleanup()