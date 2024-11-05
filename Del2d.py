import matplotlib.pyplot as plt
import datetime

with open("temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt", "r", encoding="UTF8")as fil3:
    fil3.readline()
    linjer3 = fil3.readlines()
    linjer3 = linjer3[:-2]

liste_sauda = []
liste_sirdal = []
stasjon_sauda = []
stasjon_sirdal = []
tid_sauda = []
tid_sirdal = []
temperatur_sauda = []
temperatur_sirdal = []
trykket_sauda = []
trykket_sirdal = []




for linje in linjer3:
    if len(linje.split(";")[0]) > 5:
        liste_sirdal.append(linje.strip().split(";")[0])
        stasjon_sirdal.append(linje.strip().split(";")[1])
        tid_sirdal.append(linje.strip().split(";")[2])
        temperatur_sirdal.append(float(linje.replace(",", ".").strip().split(";")[3]))
        trykket_sirdal.append(float(linje.replace(",", ".").strip().split(";")[4]))

    else:
        liste_sauda.append(linje.split(";")[0])
        stasjon_sauda.append(linje.strip().split(";")[1])
        tid_sauda.append(linje.strip().split(";")[2])
        temperatur_sauda.append(float(linje.replace(",", ".").strip().split(";")[3]))
        trykket_sauda.append(float(linje.replace(",", ".").strip().split(";")[4]))


plot_tid_sauda = []
plot_tid_sirdal = []

for x in tid_sauda:
    plot_tid_sauda.append(datetime.datetime.strptime(x, "%d.%m.%Y %H:%M"))

for x in tid_sirdal:
    plot_tid_sirdal.append(datetime.datetime.strptime(x, "%d.%m.%Y %H:%M"))

plt.subplot(2,1,1)
plt.plot(plot_tid_sirdal, temperatur_sirdal, label="Tempratur for Sirdal", color = "blue")
plt.plot(plot_tid_sauda, temperatur_sauda, label= "Temperaturen for Sauda", color = "red")
plt.legend()

plt.subplot(2,1,2)
plt.plot(plot_tid_sirdal, trykket_sirdal, label="Trykket for Sirdal", color = "purple")
plt.plot(plot_tid_sauda, trykket_sauda, label="Trykket for Sauda", color = "green")
plt.legend()

plt.show()