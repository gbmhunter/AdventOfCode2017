import csv

input = []
with open('input.txt', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter='\t')
    for row in csvReader:
        banks = [int(numeric_string) for numeric_string in row]
              
# banks = [ 0, 2, 7, 0 ]

print('banks = ' + str(banks))

duplicateDict = {}
numRedisCycles = 0
while True:
    # Find bank with lowest num of blocks
    index = banks.index(max(banks))

    print('index = ' + str(index))

    # Pull out blocks from this min bank
    blocksToRedis = banks[index]

    # Set to 0
    banks[index] = 0
    
    for i in range(0, blocksToRedis):
        limIndex = (index + 1 + i)%len(banks)
        print('limIndex = ' + str(limIndex))
        banks[limIndex] += 1

    print('Finished redistributing. banks = ' + str(banks))

    numRedisCycles += 1

    # Create tuple from list
    banksAsTuple = tuple(banks)

    if banksAsTuple in duplicateDict:
        # Duplicate bank configuration found!
        break
    else:
        print('Bank configuration is unique. Performing redistribution cycle again...')
        duplicateDict[banksAsTuple] = 1
        

print('Redistribution complete. Num cycles = ' + str(numRedisCycles))


