import csv

data1 = []
data2 = []

with open('finalstarsnew.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data1.append(row)

with open('dwarfplan2.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data2.append(row)
        
headers1 = data1[0]
planet_data1 = data1[1:]

headers2 = data2[0]
planet_data2 = data2[1:]

headers = headers1 + headers2
planet_data = []

for i in planet_data1:
    planet_data.append(i)

for i in planet_data2:
    planet_data.append(i)
    
with open('final.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)