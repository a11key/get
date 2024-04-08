import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]

comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def decimal2binary(value):
    signal = [int(element) for element in bin(value)[2:].zfill(8)]
    GPIO.output(dac, signal)
    return signal


def volume(value):
    n = int(value/256 * 8)
    out=[1]*n
    for i in range(8-n):
        out.append(0)
    return out

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
    signal = decimal2binary(value)
    voltage = value / 256 * 3.3
    print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
    return value

try:
    while True:
        value = adc()
        print(volume(value))
        GPIO.output(leds, volume(value))


finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()    