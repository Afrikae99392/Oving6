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
ampm_6 = []
tidplot_6 = []

for linje in linjer:
    tid_liste.append(linje.strip().split(";")[0])
    tid_siden_start_liste.append(linje.split(";")[1])
    trykk_liste.append(linje.replace(",", ".").strip().split(";")[2])
    abs_trykk_liste.append(float(linje.replace(",", ".").strip().split(";")[3]))
    temp_liste.append(float(linje.replace(",", ".").strip().split(";")[4]))

plot_tid1 = []
pm_og_am = []
plot_tidfinal = []


for x in tid_liste:
    if x[-2:] == "pm" and x[11:12] != "12":
        pm_og_am.append(x)

    elif x[-2:] == "am" or x[-2:] == "pm":
        pm_og_am.append(x)

    elif x[-2:] != "am" and x[-2:] != "pm":
        plot_tid1.append(x)
    


for x in range(0, len(plot_tid1), 6):
    plot_tidfinal.append(datetime.datetime.strptime(plot_tid1[x], "%m.%d.%Y %H:%M"))

for x in pm_og_am:
    if x[17:22] == "08 pm":
        ampm_6.append(datetime.datetime.strptime(x, "%m/%d/%Y %I:%M:%S %p"))

    elif x[17:22] == "08 am":
        ampm_6.append(datetime.datetime.strptime(x[0:19], "%m/%d/%Y %H:%M:%S"))


trykkbar_liste = []
for x in trykk_liste:
    if x != "":
        trykkbar_liste.append(x)

