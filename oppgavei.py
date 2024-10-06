import matplotlib.pyplot as plt
import datetime
with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r", encoding="UTF8")as file:
    file.readline()
    linjer = file.readlines()
    linjer = linjer[:-2]

tid_liste = []
tid_siden_start_liste = []
trykk_liste = []
abs_trykk_liste = []
temp_liste = []

for linje in linjer:
    tid_liste.append(linje.split(";")[0])
    tid_siden_start_liste.append(linje.split(";")[1])
    
    abs_trykk_liste.append(float(linje.replace(",", ".").strip().split(";")[3]))
    temp_liste.append(float(linje.replace(",", ".").strip().split(";")[4]))

for linje2 in linjer:
    if linje2.split(";")[2] != "":
        trykk_liste.append(linje2.split(";")[2])


sekunder = []
for x in linjer:
    if (float(x.split(";")[1]) % 6 == 0.0):
        sekunder.append(float(x.split(";")[1]))
    

ref_tid = datetime.datetime(2021, 6, 11, 14 , 23)

tid_etter_start_final = [ref_tid + datetime.timedelta(seconds= s) for s in sekunder]

"""plt.plot(tid_etter_start_final, trykk_liste, label = "Barometer trykk hvert 60. sekund", color= "green")
plt.show()
"""
print(trykk_liste[-1])