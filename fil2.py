import matplotlib.pyplot as plt

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
    
print(tid_liste)

