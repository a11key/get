import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while True: 
        number = input()

        if number == "q": break
        try: 
            float(number)
        except:
            print("Введено не число")
            continue
        fl_num = float(number)
        if int(fl_num) != fl_num: print("Введено не целое число")
        if fl_num<0: 
            print("Введено отрицательное число")
        if fl_num>255: 
            print("Введено значение превышающее возможности 8-разрядного ЦАП")
        if fl_num>255 or fl_num<0:
            continue
        GPIO.output(dac, decimal2binary(int(fl_num)))
        voltage = int(fl_num)*3.3/255
        print("Напряжение: ", voltage, " В")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()