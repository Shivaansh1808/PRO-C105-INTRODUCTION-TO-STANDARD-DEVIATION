import math
import csv

with open("Coviddata.csv",newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)

data = filedata[0]

n = len(data)
sum = 0

for x in data:
    sum += int(x)

mean = sum/n

squared_list = []

for number in data:
    a = int(number)-mean
    a = a**2
    squared_list.append(a)

sum = 0

for x in squared_list:
    sum+= int(x)

result = sum/n

standard_deviation = math.sqrt(result)
print(standard_deviation)
print(mean)