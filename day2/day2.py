import csv

sum = 0
with open('input.txt', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in csvReader:
        rowAsInt = [int(numeric_string) for numeric_string in row]
        diff = max(rowAsInt) - min(rowAsInt)        
        sum += diff

print('output = ' + str(sum))
