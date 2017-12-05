import csv

sum = 0
part2Sum = 0
with open('input.txt', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in csvReader:
        rowAsInt = [int(numeric_string) for numeric_string in row]
        diff = max(rowAsInt) - min(rowAsInt)        
        sum += diff        

        for index1, firstValue in enumerate(rowAsInt):
            for index2, secondValue in enumerate(rowAsInt):
                if index1 == index2:
                    continue
            
                modulus = firstValue % secondValue                
                if modulus == 0:                    
                    part2Sum += firstValue / secondValue                            


print('part 1 answer = ' + str(sum))
print('part 2 answer = ' + str(part2Sum))
