import matplotlib.pyplot as plt
import datetime
with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r", encoding="UTF8")as file:
    file.readline()
    file.readline()[:-1]
    linjer = file.readlines()


tid_liste = []
tid_siden_start_liste = []
trykk_liste = []
abs_trykk_liste = []
temp_liste = []

for linje in linjer:
    tid_liste.append(linje.split(";")[0])
    tid_siden_start_liste.append(linje.split(";")[1])
    trykk_liste.append(linje.split(";")[2])
    abs_trykk_liste.append(linje.split(";")[3])
    temp_liste.append(linje.split(";")[4])


plot_tid1 = []
plot_tid2 = []
pm_og_am = []

for x in tid_liste:
    if x[-2:] == "am" and x[11:13] == "00":
        y = x[0:11] + "12" + x[13:19]
        pm_og_am.append(y)

    elif x[-2:] == "pm":
        pm_og_am.append(x[0:19])

    else:
        plot_tid1.append(x)

for x in pm_og_am:
    plot_tid2.append(datetime.datetime.strptime(x, "%m/%d/%Y %I:%M:%S"))



for x in plot_tid2:
    plot_tid1.append(x)

print(len(trykk_liste), len(plot_tid1))
print(pm_og_am)
"""plt.plot(plot_tid1, trykk_liste)"""
