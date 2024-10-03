import matplotlib.pyplot as plt
import datetime
import numpy as np

with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r", encoding="UTF8")as file:
    file.readline()
    file.readline()[:-1]
    linjer = file.readlines()

tid_liste = []
tid_siden_start_liste = []
trykk_liste = []
abs_trykk_liste = []
temp_liste = []

plot_tid1 = []
plot_tid2 = []
pm_og_am = []
plot_final = []


for linje in linjer:
    tid_liste.append(linje.split(";")[0])
    tid_siden_start_liste.append(linje.split(";")[1])
    trykk_liste.append((linje.strip().split(";")[2]))
    abs_trykk_liste.append(float(linje.replace(",", ".").strip().split(";")[3]))
    temp_liste.append(float(linje.replace(",", ".").strip().split(";")[4]))


tid_intervall_11_12 = []
nytid3 = []


# Finner tid
teller = 0
for x in tid_liste:
    
    if x == "06.11.2021 17:31":
        print(teller, x)
        
    elif x == "06.12.2021 03:05":
        print(teller, x)
    teller += 1
# Indeksen på tidintervallet er 1127, og 4569 fordi det er fra første 6.11.2021 17:31 til første indeks av 6.12.2021 03:05    
    
for x in tid_liste[1127:4569]:
    nytid3.append(datetime.datetime.strptime(x, "%m.%d.%Y %H:%M"))
    
y = np.linspace(temp_liste[1127], temp_liste[4569], 4569-1127)

for x in tid_liste:
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

plt.plot(plot_final, temp_liste, color = "purple")
plt.plot(nytid3, y, color = "red")

plt.show()

print(temp_liste[4569], temp_liste[1127])