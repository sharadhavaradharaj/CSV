import csv

infile = open("sitka_weather_07-2018_simple.csv" , "r")

reader = csv.reader(infile)
header_row = next(reader)

print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs = []
for row in reader:
    highs.append(int(row[5]))

print(highs[:5])

import matplotlib.pyplot as plt

plt.plot(highs, c = "red")
plt.title("Daily high temps,July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temps (F)", fontsize=36)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()




