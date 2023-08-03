import csv
from datetime import datetime

infile = open("sitka_weather_07-2018_simple.csv" , "r")

reader = csv.reader(infile)
header_row = next(reader)

print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs = []
dates = []

some_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(type(some_date))


for row in reader:
    highs.append(int(row[5]))
    some_date = datetime.strptime(row[2], "%Y-%m-%d")
    print(type(some_date))
    dates.append(some_date)
     
    # dateVal = datetime.strptime(row[2], "%Y-%m-%d")
    
    

print(highs[:5]) # From 0 to 4
print(dates[:5])



import matplotlib.pyplot as plt

fig = plt.figure()


plt.plot(dates, highs, c = "red")
plt.title("Daily high temps,July 2018", fontsize=16)
plt.xlabel("Dates",fontsize=16)
plt.ylabel("Temps in (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()





