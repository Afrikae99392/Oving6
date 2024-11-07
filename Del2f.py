import matplotlib.pyplot as plt
import datetime
import math
#importerer fra oving 6 oppgave g slik som oppgavebeskrivelsen krevde
from oppgaveg import calculate_moving_average


# denne funksjonen beregner standardavvik
def calculate_standard_deviation(temperatures, moving_avg_temperatures, n):
    std_devs = []
    for i in range(n, len(temperatures) - n):
        # her beregnes variansen som en del av standardavviket
        variance = sum((temperatures[j] - moving_avg_temperatures[i - n]) ** 2 for j in range(i - n, i + n + 1)) / (2 * n)
        std_dev = math.sqrt(variance)
        std_devs.append(std_dev)
    return std_devs

with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r", encoding="UTF8") as file1:
    file1.readline()  
    file1.readline()  
    linjer1 = file1.readlines()

tid_liste1 = []
temp_liste = []

for linje in linjer1:
    tid_liste1.append(linje.split(";")[0])
    temp_liste.append(float(linje.replace(",", ".").strip().split(";")[4]))

# lager to lister som separerer mellom tidene etter format
# den siste lista brukes til å sortere dem begge sammen
plot_tid1 = []
pm_og_am = []
plot_final = []

# kjører løkka for å skanne alle linjer og sortere dem mellom listene etter tidsformat
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

#glattebredden
n = 30

# gjenopptar data fra oppgave g i øving 6 for å beregne standardavvik
valid_times, avg_temperatures = calculate_moving_average(plot_final, temp_liste, n)

# Kaller funksjonen for å beregne standardavvik
std_devs = calculate_standard_deviation(temp_liste, avg_temperatures, n)

# puttet inn en if name = main for å sikre at plott fra opp.g ikke printes ut
#plotter glattet gjennomsnittstemperatur med feilstolper
plt.errorbar(valid_times, avg_temperatures, yerr=std_devs, errorevery=30, capsize=3, label=f"Gj.temp med feilstolper", color="orange")
#plotter originaltemperaturen
#plt.plot(plot_final, temp_liste, label="Opprinnelig temperatur", color="blue")
plt.xlabel("Tid")
plt.ylabel("Temperatur i celcius")
plt.legend()
plt.show()

