import matplotlib.pyplot as plt
import datetime

with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r", encoding="UTF8")as file:
    file.readline()[:-1]
    linjer = file.readlines()
    

with open("temperatur_trykk_met_samme_rune_time_datasett.csv.txt", "r", encoding="UTF8")as file2:
    file2.readline()
    linjer2 = file2.readlines()
    linjer2 = linjer2[:-2]


tid_liste_uis = []
tid_siden_start_liste = []
trykk_liste = []
abs_trykk_liste = []
temp_liste = []
tid_liste_uis2 = []

navn_liste = []
stasjon_liste = []
tid_liste_sola = []
lufttemp_liste = []
lufttrykk_liste = []


for linje in linjer:
    tid_liste_uis.append(linje.split(";")[0])
    tid_siden_start_liste.append(linje.split(";")[1])
    trykk_liste.append(linje.replace(",", ".").strip().split(";")[2])
    abs_trykk_liste.append(float(linje.replace(",", ".").strip().split(";")[3]) * 10)
    temp_liste.append(float(linje.replace(",", ".").strip().split(";")[4]))

new_temp = []
for x in linjer2:
    navn_liste.append(x.strip().split(";")[0])
    stasjon_liste.append(x.strip().split(";")[1])
    tid_liste_sola.append(x.split(";")[2])
    lufttemp_liste.append(float(x.replace(",",".").strip().split(";")[3]))
    lufttrykk_liste.append(float(x.replace(",",".").strip().split(";")[4]))


plot_tid1 = []
pm_og_am = []
plot_tidfinal = []
trykkbar_liste = []


for linje in linjer:
    if linje.split(";")[2] != "":
        trykkbar_liste.append(float(linje.replace(",", ".").split(";")[2]) * 10)
        tid_liste_uis2.append(linje.split(";")[0]) 

for x in tid_liste_uis2:
    if x[-2:] == "pm":
        pm_og_am.append(x)

    elif x[-2:] == "am":
        pm_og_am.append(x)

    elif x[-2:] != "am" and x[-2:] != "pm":
        plot_tid1.append(x)
    

for x in plot_tid1:
    plot_tidfinal.append(datetime.datetime.strptime(x, "%m.%d.%Y %H:%M"))

for x in pm_og_am:
    if x[17:22] == "08 pm":
        plot_tidfinal.append(datetime.datetime.strptime(x, "%m/%d/%Y %I:%M:%S %p"))

    elif x[17:22] == "08 am":
        plot_tidfinal.append(datetime.datetime.strptime(x[0:19], "%m/%d/%Y %H:%M:%S"))

plot_tid1 = []
pm_og_am = []
plot_final = []

for x in tid_liste_uis:
    if x[-2:] == "pm" and x[11:12] != "12" :
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
for x in tid_liste_sola:
    nytid.append(datetime.datetime.strptime(x, "%d.%m.%Y %H:%M"))

plt.plot(nytid, lufttrykk_liste)
plt.plot(plot_final, abs_trykk_liste)

plt.plot(plot_tidfinal, trykkbar_liste)
plt.show()