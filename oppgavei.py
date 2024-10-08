import matplotlib.pyplot as plt
import datetime
with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r", encoding="UTF8")as file:
    file.readline()[:-1]
    linjer = file.readlines()
    
tid_liste = []
tid_siden_start_liste = []
trykk_liste = []
abs_trykk_liste = []
temp_liste = []

for linje in linjer:
    tid_siden_start_liste.append(linje.split(";")[1])
    trykk_liste.append(linje.replace(",", ".").strip().split(";")[2])
    abs_trykk_liste.append(float(linje.replace(",", ".").strip().split(";")[3]))
    temp_liste.append(float(linje.replace(",", ".").strip().split(";")[4]))

plot_tid1 = []
pm_og_am = []
plot_tidfinal = []
trykkbar_liste = []


for linje in linjer:
    if linje.split(";")[2] != "":
        trykkbar_liste.append(float(linje.replace(",", ".").split(";")[2]))
        tid_liste.append(linje.split(";")[0]) 

for x in tid_liste:
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


plt.plot(plot_tidfinal, trykkbar_liste)
plt.show()