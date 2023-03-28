import csv

with open("files/weather.csv") as csvfile:
    readfile = list(csv.reader(csvfile))
    print(readfile)

"""
[['Station', 'Temperature'], ['Kuala Lumpur', '45'], ['New York', '20']]
"""

city = input("Enter a city name: ")
for item in readfile:
    if city in item:
        print(f"Current temp in {city}: {item[1]}")

"""
with open("files/weather.csv",'r') as txtfile:
    print(txtfile.read())
"""
"""
"Station","Temperature"
"Kuala Lumpur","45"
"New York","20"
"""