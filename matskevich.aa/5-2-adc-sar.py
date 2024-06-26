import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    signal = [int(element) for element in bin(value)[2:].zfill(8)]
    GPIO.output(dac, signal)
    return signal


def adc():
    n = 128
    value = 0
    for i in range(8):
        value += n
        signal = decimal2binary(value)
        time.sleep(0.1)
        compValue = GPIO.input(comp)
        if compValue == 1:
            value -= n
        n = n//2
    voltage = value / 256 * 3.3
    print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))

try:
    while True:
        adc()

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()    