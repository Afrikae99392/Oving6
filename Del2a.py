import matplotlib.pyplot as plt
import datetime
import numpy as np

with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r", encoding="UTF8")as file1:
    file1.readline()
    file1.readline()[:-1]
    linjer1 = file1.readlines()

with open("temperatur_trykk_met_samme_rune_time_datasett.csv.txt", "r", encoding="UTF8")as file2:
    file2.readline()
    linjer2 = file2.readlines()
    linjer2 = linjer2[:-2]

tid_liste1 = []
tid_siden_start_liste = []
trykk_liste = []
abs_trykk_liste = []
temp_liste = []

navn_liste = []
stasjon_liste = []
tid_liste2 = []
lufttemp_liste = []
lufttrykk_liste = []

for linje in linjer1:
    tid_liste1.append(linje.split(";")[0])
    tid_siden_start_liste.append(linje.split(";")[1])
    trykk_liste.append((linje.strip().split(";")[2]))
    abs_trykk_liste.append(float(linje.replace(",", ".").strip().split(";")[3]))
    temp_liste.append(float(linje.replace(",", ".").strip().split(";")[4]))

for linje in linjer2:
    navn_liste.append(linje.strip().split(";")[0])
    stasjon_liste.append(linje.strip().split(";")[1])
    tid_liste2.append(linje.split(";")[2])
    lufttemp_liste.append(float(linje.replace(",",".").strip().split(";")[3]))
    lufttrykk_liste.append(float(linje.replace(",",".").strip().split(";")[4]))


plot_tid1 = []
plot_tid2 = []
pm_og_am = []
plot_final = []

for x in tid_liste1:
    if x[-2:] == "pm" and x[11:12] != "12":
        pm_og_am.append(datetime.datetime.strptime(x, "%m/%d/%Y %I:%M:%S %p"))

    elif x[-2:] == "am" or x[-2:] == "pm":
        pm_og_am.append(datetime.datetime.strptime(x[0:19], "%m/%d/%Y %H:%M:%S"))

    elif x[-2:] != "am" and x[-2:] != "pm":
        plot_tid1.append(x)

    else:
        print(x)

for x in plot_tid1:
    plot_final.append(datetime.datetime.strptime(x, "%m.%d.%Y %H:%M"))

for x in pm_og_am:
    plot_final.append(x)

nytid = []
for x in tid_liste2:
    nytid.append(datetime.datetime.strptime(x, "%d.%m.%Y %H:%M"))


nytid3 = []
# Finner tid
teller = 0
for x in tid_liste1:
    
    if x == "06.11.2021 17:31":
        print(teller, x)
        
    elif x == "06.12.2021 03:05":
        print(teller, x)
        break
    
    teller += 1

teller2 = 0
for x in tid_liste2:

    if x == "11.06.2021 17:00":
        print(x, teller2)

    elif x == "12.06.2021 04:00":
        print(x, teller2)
        break

    teller2 += 1

tid_liste2_ny = []

# Indeksen på tidintervallet er 1127, og 4569 fordi det er fra første 6.11.2021 17:31 til første indeks av 6.12.2021 03:05    
    
for x in tid_liste1[1127:4569]:
    nytid3.append(datetime.datetime.strptime(x, "%m.%d.%Y %H:%M"))

tid_liste2_ny.append(nytid3[0])
tid_liste2_ny.append(nytid3[-1])
    
y = np.linspace(temp_liste[1127], temp_liste[4569], 4569-1127)
y2 = []
y2.append(lufttemp_liste[16])
y2.append(lufttemp_liste[26])

plt.plot(plot_final, temp_liste, label = "Tempraturer fra UiS", color = "blue")
plt.plot(nytid, lufttemp_liste, label = "Tempraturer fra Sola værstasjon", color = "red")
plt.plot(nytid3, y, label = "Gjennomsnittlig tempraturfall på intervall", color = "purple")
plt.plot(tid_liste2_ny, y2, label = "Gjennomsnittlig tempraturfall på intervall", color = "yellow")


plt.xlabel("Tid")
plt.ylabel("Tempratur")
plt.legend()
plt.show()
