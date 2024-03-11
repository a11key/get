import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

GPIO.output(20, GPIO.input(24))