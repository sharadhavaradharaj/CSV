import csv
from datetime import datetime
import matplotlib.pyplot as plt


def read_csv_file(filename):
    infile = open(filename, "r")
    reader = csv.reader(infile)
    header_row = next(reader)
    tmin_index = header_row.index("TMIN")
    tmax_index = header_row.index("TMAX")
    dates = []
    highs = []
    lows = []

    for row in reader:
        try:
            some_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[tmax_index])
            low = int(row[tmin_index])
        except ValueError:
            print(f"Missing data for {some_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(some_date)

    return dates, highs, lows

def create_combined_graph(dates1, highs1, lows1, dates2, highs2, lows2):
    plt.figure(figsize=(15, 8))
    plt.suptitle("Temperature comparision between Sitka Airport, AK US and Death Valley, CA US ", fontsize=18, y=1.00)
    plt.subplot(2, 1, 1)
    plt.plot(dates1, highs1, c="red", alpha=0.5, label="Sitka Highs")
    plt.plot(dates1, lows1, c="blue", alpha=0.5, label="Sitka Lows")
    plt.fill_between(dates1, highs1, lows1, facecolor="blue", alpha=0.1)
    plt.title("Sitka Airport, AK US- Daily low and high temperatures - 2018", fontsize=16)
    plt.xlabel("Dates", fontsize=12)
    plt.ylabel("Temps (F)", fontsize=12)
    plt.tick_params(axis="both", which="major", labelsize=10)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(dates2, highs2, c="red", alpha=0.5, label="Death Valley Highs")
    plt.plot(dates2, lows2, c="blue", alpha=0.5, label="Death Valley Lows")
    plt.fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)
    plt.title("Death Valley, CA US - Daily low and high temperatures - 2018", fontsize=16)
    plt.xlabel("Dates", fontsize=12)
    plt.ylabel("Temps (F)", fontsize=12)
    plt.tick_params(axis="both", which="major", labelsize=10)
    plt.legend()

    plt.tight_layout(h_pad=2.5)
    plt.show()

if __name__ == "__main__":
    sitka_dates, sitka_highs, sitka_lows = read_csv_file("sitka_weather_2018_simple.csv")
    death_valley_dates, death_valley_highs, death_valley_lows = read_csv_file("death_valley_2018_simple.csv")

    create_combined_graph(sitka_dates, sitka_highs, sitka_lows, death_valley_dates, death_valley_highs, death_valley_lows)
