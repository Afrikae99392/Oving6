with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r", encoding="UTF8")as file:
    file.readline()
    file.readline()[:-1]
    linjer = file.readlines()


navn_liste = []
stasjon_liste = []
tid_liste = []
lufttemp_liste = []
lufttrykk_liste = []

for linje in linjer:
    navn_liste.append(linje.split(";")[0])
    stasjon_liste.append(linje.split(";")[1])
    tid_liste.append(linje.split(";")[2])
    lufttemp_liste.append(linje.split(";")[3])
    lufttrykk_liste.append(linje.split(";")[4])
    
print(tid_liste)