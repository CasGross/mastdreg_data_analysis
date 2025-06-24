import numpy as np
import matplotlib.pyplot as plt

# 34 Zeilen überspringen
daten = np.loadtxt(r"C:\Users\caspa\Documents\Uni ab SoSe25\PV2\2025_Gruppe A\IV-Kurve\17-503-75-74_TLM_SUM.dat", skiprows=35)

x1 = daten[:7,1]
y1 = daten[:7, 4]
x2 = daten[7:,1]
y2 = daten[7:, 4]
print(x1)
print(y1)
print(y2)

mittelwert = np.mean(y1)
print(mittelwert)
std_abw = (np.std(np.sort(y1)) / mittelwert) *100
print(std_abw)



m, b = np.polyfit(x1, (y1+y2[::-1])/2, 1)
x_fit = np.linspace(x1[0],0,100)
y_fit = m * x_fit + b
kontaktwiederstand = np.linspace(b,b,100)

print(y_fit)

plt.plot(x_fit, kontaktwiederstand, label = round(b,3))
plt.plot(x1, y1,"xg")
plt.plot(x2, y2, "xg", label = "Messwerte")
plt.plot(x_fit, y_fit, label = "Regressionsgerade")

plt.xlabel("d [µm] ")
plt.ylabel("R [Ohm]")
plt.legend()
plt.title("Kontaktwiederstand")
plt.grid("on")
plt.show()

