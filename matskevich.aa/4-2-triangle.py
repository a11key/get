import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while True:
        print("Введите период треугольного сигнала")
        inp = input()
        if inp == "q": break
        delay = float(inp)/512
        for i in range(256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(delay)
        for i in range(256):
            GPIO.output(dac, decimal2binary(255-i))
            time.sleep(delay)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()