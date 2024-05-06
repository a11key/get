import matplotlib.pyplot as plt
import numpy as np
with open("data.txt", "r") as f:
    data_str = f.read()
    data = list(map(int, data_str.split()))
data = [i / 256 * 3.3 for i in data]

with open("settings.txt", "r") as f:
    settings_str = f.read()
    settings = list(map(int, data_str.split()))
    freq = settings[0]
    step = settings[1]
X = [i/freq for i in range(len(data))]

fig, ax = plt.subplots()

plt.plot(X, data, color='red', marker='o', markersize=3, label='V(t)')
ax.set_title("Процесс заряда конденсатора в RC-цепочке")
ax.legend()
ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")

plt.text(3, 1.5, "Время заряда: " + str(round(X[-1], 2)), fontsize=9) #подправить координаты numpy

major_ticks = np.arange(0, 101, 20) #подправить макс numpy
minor_ticks = np.arange(0, 101, 5) #подправить макс numpy
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

ax.set_xlim(0, 1.1*np.max(X))
ax.set_ylim(0, 1.1*np.max(data))

plt.show()
