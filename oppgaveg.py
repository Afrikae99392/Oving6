import matplotlib.pyplot as plt
import datetime


def calculate_moving_average(times, temperatures, n):
    valid_times = []
    avg_temperatures = []
    
   
    for i in range(n, len(temperatures) - n):
        valid_times.append(times[i])
        
        
        avg_temp = sum(temperatures[i - n:i + n + 1]) / (2 * n + 1)
        avg_temperatures.append(avg_temp)
    
    return valid_times, avg_temperatures


with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r", encoding="UTF8") as file1:
    file1.readline()
    file1.readline()[:-1]
    linjer1 = file1.readlines()

tid_liste1 = []
temp_liste = []


for linje in linjer1:
    tid_liste1.append(linje.split(";")[0])
    temp_liste.append(float(linje.replace(",", ".").strip().split(";")[4]))

plot_tid1 = []
pm_og_am = []
plot_final = []


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


n = 30
valid_times, avg_temperatures = calculate_moving_average(plot_final, temp_liste, n)

if __name__ == "__main__":
    plt.plot(plot_final, temp_liste, label="Original Temperature", color="blue")
    plt.plot(valid_times, avg_temperatures, label=f"Moving Average (n={n})", color="orange")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.show()