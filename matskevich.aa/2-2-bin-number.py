import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

number = [255, 127, 64, 32, 5, 0, 256]

for i in (number):
    n = list(map(int, list(str(bin(i)[2:]))))
    while len(n) < 8:
        n.insert(0, 0)
    print(i,n)
    GPIO.output(dac, n)
    time.sleep(10)
    GPIO.output(dac, 0)

GPIO.cleanup()