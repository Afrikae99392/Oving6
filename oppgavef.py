import matplotlib.pyplot as plt
import datetime

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

plt.plot(plot_final, temp_liste, label = "Tempraturer fra Uis", color = "blue")
plt.plot(nytid, lufttemp_liste, label = "Tempraturer fra Sola værstasjon", color = "red")
plt.xlabel("Tid")
plt.ylabel("Tempratur")
plt.legend()
plt.show()