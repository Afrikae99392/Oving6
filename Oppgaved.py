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