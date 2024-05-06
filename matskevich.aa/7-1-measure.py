import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]

comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

#Перевод сигнала в двоичный код для светодиодов
def decimal2binary(value):
    signal = [int(element) for element in bin(value)[2:].zfill(8)]
    GPIO.output(dac, signal)
    return signal

#Перевод 
def volume(value):
    n = int(value/256 * 8)
    out=[1]*n
    for i in range(8-n):
        out.append(0)
    return out

#Считывание напряжения на конденсаторе с помощью комаратора
def adc():
    n = 128
    value = 0
    
    for i in range(8):
        value += n
        signal = decimal2binary(value)
        time.sleep(0.01)
        compValue = GPIO.input(comp)
        if compValue == 1:
            value -= n
        n = n//2
    signal = decimal2binary(value)
    voltage = value / 256 * 3.3
 #   print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
    return [value, signal, voltage]

#Список для хранения value
data = []

try:
    # Считываем начальное время
    startTime = time.time()

    #Считываем напряжение с конденсатора до максимального напряжения (2.66 В)
    voltage = 0
    GPIO.output(troyka, 1)
    while voltage < 2.66:
        ADC = adc()
        value = ADC[0]
        voltage = ADC[2]
        print(voltage)
        data.append(value)
        # print(volume(value))
        GPIO.output(leds, volume(value))
    # print(data)

    # Считываем конечное время
    endTime = time.time()
    # Время эксперимента
    duration = endTime - startTime
    # print(duration)


    #Строим график
    x = [i for i in range(len(data))]
    plt.scatter(x, data)
    plt.show()

    data_str = [str(i) for i in data]

    #Записываем в файл напряжения
    with open("data.txt", "w") as data_write:
        data_write.write("\n".join(data_str))


    T = duration/len(data)
    freq = 1/T
    step = 3.3/256
    #Записываем в файл среднюю частоту дскретизации и шаг квантования
    with open("settings.txt", "w") as settings_write:
        settings_write.write(str(freq) + "\n" + str(step))



    print("Продолжительность эксперимента, с: ", duration)
    print("Период одного измерения, с: ", T)
    print("Средняя частота дискретизации, Гц: ", freq)
    print("шаг квантования АЦП, В: ", step)
    
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()    