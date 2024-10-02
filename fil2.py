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
    trykk_liste.append((linje.strip().split(";")[2]))
    abs_trykk_liste.append(float(linje.replace(",", ".").strip().split(";")[3]))
    temp_liste.append(float(linje.replace(",", ".").strip().split(";")[4]))


plot_tid1 = []
plot_tid2 = []
pm_og_am = []
plot_final = []

for x in tid_liste:
    if x[-2:] == "pm":
        y = x[0:11] + "12" + x[13:19]
        pm_og_am.append(datetime.datetime.strptime(y, "%m/%d/%Y %H:%M:%S"))

    elif x[-2:] == "am":
        pm_og_am.append(datetime.datetime.strptime(x[0:19], "%m/%d/%Y %H:%M:%S"))

    elif x[-2:] != "am" and x[-2:] != "pm":
        plot_tid1.append(x)

    else:
        print(x)

for x in plot_tid1:
    plot_final.append(datetime.datetime.strptime(x, "%m.%d.%Y %H:%M"))

for x in pm_og_am:
    plot_final.append(x)

plt.plot(plot_final, temp_liste)
plt.show()