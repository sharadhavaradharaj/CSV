'''Changing the file to include all the data for a year of 2018.
Changing the title to - Daily low and high temperatures - 2018.
Extract low temps from the file and add to chart.
Shade in the area between high and low'''



import csv
from datetime import datetime

infile = open("sitka_weather_2018_simple.csv" , "r")
reader = csv.reader(infile)
header_row = next(reader)
print(header_row)


for index, col_header in enumerate(header_row):
    print(index, col_header)


# Create an empty list to get the values in list to access easily
highs = []
dates = []
lows = []


# We want to convert date string into a dae object, %Y=year, %m=month, %d=date
some_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(type(some_date))


for row in reader:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    some_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(some_date)


print(highs[:5])
print(dates)
print(lows)



import matplotlib.pyplot as plt

fig = plt.figure()


plt.plot(dates, highs, c = "red",alpha=0.5) # The argument(in this case 'dates' and 'highs') has to be a list of values
plt.plot(dates, lows, c = "blue", alpha=0.5) # Alpha changes the boldness of the line

plt.fill_between(dates,highs,lows, facecolor="blue" , alpha=0.1 ) # Fill on x-values between y1 and y2

plt.title("Daily low and high temperatures,July 2018", fontsize=16)
plt.xlabel("Dates",fontsize=16)
plt.ylabel("Temps in (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate() # Will automatically designs thee length of date , to view it more clearly

plt.show()


plt.subplot(2,1,1)
plt.plot(dates,highs,c="red")
plt.title("Highs")
            
plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows for Sitka, Alaska")

plt.show()