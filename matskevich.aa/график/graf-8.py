import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data.txt", dtype = int)*(3.3 / 256)

settings = np.loadtxt("settings.txt", dtype = float)
freq = settings[0]
step = settings[1]

X = [i/freq for i in range(len(data))]

fig, ax = plt.subplots(figsize = (8, 5), dpi = 100)

plt.plot(X, data, color='red', label='V(t)')

data_scatter = []
X_scatter = []
for i in range(len(data)):
    if i%3 == 0:
        data_scatter.append(data[i])
        X_scatter.append(X[i])

plt.scatter(X_scatter, data_scatter, color='red', s = 20)
ax.set_title("Процесс заряда конденсатора в RC-цепочке")
ax.legend()
ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")

plt.text(0.7*np.max(X), 0.7*np.max(data), "Время заряда: " +
str(round(X[-1], 2)) + " с", fontsize=11)

major_xticks = np.arange(0, 1.1*np.max(data)+1, 0.5)
minor_xticks = np.arange(0, 1.1*np.max(data), 0.1)
major_yticks = np.arange(0, 1.1*np.max(X), 1)
minor_yticks = np.arange(0, 1.1*np.max(X), 0.2)
ax.set_xticks(major_yticks)
ax.set_xticks(minor_yticks, minor=True)
ax.set_yticks(major_xticks)
ax.set_yticks(minor_xticks, minor=True)

ax.grid(which='minor', alpha=0.2, linestyle='--', c = "black")
ax.grid(which='major', alpha=0.5, c = "black")

ax.set_xlim(0, 1.1*np.max(X))
ax.set_ylim(0, 1.1*np.max(data))

fig.savefig("graf.svg")
plt.show()
