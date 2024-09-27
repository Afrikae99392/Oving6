import matplotlib.pyplot as plt

with open("temperatur_trykk_met_samme_rune_time_datasett.csv.txt", "r", encoding="UTF8")as file:
    file.readline()
    linjer = file.readlines()
    linjer = linjer[:-2]

navn_liste = []
stasjon_liste = []
tid_liste = []
lufttemp_liste = []
lufttrykk_liste = []


new_temp = []
for linje in linjer:
    navn_liste.append(linje.strip().split(";")[0])
    stasjon_liste.append(linje.strip().split(";")[1])
    tid_liste.append(linje.strip().split(";")[2])
    lufttemp_liste.append(float(linje.replace(",",".").strip().split(";")[3]))
    lufttrykk_liste.append(float(linje.replace(",",".").strip().split(";")[4]))
    

print(lufttrykk_liste)


plt.plot(tid_liste, lufttemp_liste)
plt.legend()
plt.show()

