import csv
import matplotlib.pyplot as plt

file = open("../data/weather_20_21.csv")
weather_csv = csv.reader(file)
header = next(weather_csv)
rows = []
std_week = []
max_temp = []
min_temp = []
rh7 = []
rh2 = []
rainfall = []
num_rainy_days = []

idx = 0
for row in weather_csv:
    idx = idx + 1
    if float(row[0]) >= 18 and float(row[0]) <= 23 and idx > 45:
        rows.append(row)
        std_week.append(row[0])
        max_temp.append(float(row[2]))
        min_temp.append(float(row[3]))
        rh7.append(float(row[4]))
        rh2.append(float(row[5]))
        if(row[6] == ' -   '):
            rainfall.append(float(0))
        else:
            rainfall.append(float(row[6]))
        if(row[7].strip() == '-'):
            num_rainy_days.append(float(0))
        else:
            num_rainy_days.append(float(row[7]))

#print(rainfall)
#print(min_temp)

fig, ax = plt.subplots()
l_rainfall = ax.bar(std_week, rainfall, color="grey")
ax2 = ax.twinx()
l_min_temp, = ax2.plot(std_week, min_temp, '-d', color="orange")
l_max_temp, = ax2.plot(std_week, max_temp, '-p', color="red")
l_num_rainy_days, = ax2.plot(std_week, num_rainy_days, '-v', color="blue")
l_rh7, = ax.plot(std_week, rh7, '-^', color="green")
l_rh2, = ax.plot(std_week, rh2, '-*', color="olive")
plt.legend([l_min_temp, l_max_temp, l_num_rainy_days, l_rainfall,
    l_rh7, l_rh2], ["Min. temp (°C)", "Max. temp (°C)", "No. of rainy days",
        "rainfall (mm)", "RH I (%)", "RH II (%)"], loc='center left',
    bbox_to_anchor=(1.05, 0.5))
ax.set_xlabel("Standard Week", fontsize=12)
ax.set_title("Weather data from April 2021 to June 2021", fontsize=12)
ax.grid(axis = 'y')
plt.tight_layout()
plt.show()

file.close()
