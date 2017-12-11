lengths = ''
with open('input.txt', newline='') as file:
    for line in file:
        lengths = line.split(',')

lengths = list(map(int, lengths))
print('lengths = ' + str(lengths))
# lengths = [3,4,1,5]

listSize = 256
theList = list(range(listSize))

print('theList = ' + str(theList))


currPos = 0
skipSize = 0
for length in lengths:
    print('Reordering started, length = ' + str(length) + ', currPos = ' + str(currPos))
    selection = []
    selection = []
    for i in range(0, length):
        index = (currPos + i) % len(theList)
        print('index = ' + str(index))
        selection.append(theList[index])

    print('selection = ' + str(selection))

    # Reverse selection
    revSelection = list(reversed(selection))
    print('revSelection = ' + str(revSelection))

    # Insert selection
    for i in range(0, length):
        index = (currPos + i) % len(theList)
        theList[index] = revSelection[i]

    print('theList = ' + str(theList))

    
    currPos = (currPos + length + skipSize) % len(theList)
    skipSize += 1

# Multiply first two elements together
mutli = theList[0]*theList[1]
print('multiplication (answer part 1) = ' + str(mutli))
