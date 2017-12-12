
class HashEngine:

    def __init__(self, theList, lengths):
        self.skipSize = 0
        self.currPos = 0
        self.theList = theList
        self.lengths = lengths

    def DoRound(self):    
        for length in self.lengths:
            # print('Reordering started, length = ' + str(length) + ', currPos = ' + str(currPos))
            selection = []
            selection = []
            for i in range(0, length):
                index = (self.currPos + i) % len(self.theList)
                # print('index = ' + str(index))
                selection.append(self.theList[index])

            # print('selection = ' + str(selection))

            # Reverse selection
            revSelection = list(reversed(selection))
            # print('revSelection = ' + str(revSelection))

            # Insert selection
            for i in range(0, length):
                index = (self.currPos + i) % len(self.theList)
                self.theList[index] = revSelection[i]

            # print('theList = ' + str(theList))

            
            self.currPos = (self.currPos + length + self.skipSize) % len(self.theList)
            self.skipSize += 1


def Part1():

    lengths = ''
    with open('input.txt', newline='') as file:
        for line in file:
            lengths = line.split(',')

    lengths = list(map(int, lengths))
    # print('lengths = ' + str(lengths))    

    listSize = 256
    theList = list(range(listSize))

    # print('theList = ' + str(theList))

    hashEngine = HashEngine(theList, lengths)
    hashEngine.DoRound()
    mutli = hashEngine.theList[0]*hashEngine.theList[1]
    print('multiplication (answer part 1) = ' + str(mutli))

def Part2():
    data = ''
    with open('input.txt', newline='') as file:
        for line in file:
            data = line

    # print('data = ' + data)

    # Convert each byte into it's ASCII value
    asciiBytes = []
    for singleChar in data:
        asciiBytes.append(ord(singleChar))

    # Append provided additional ASCII bytes
    asciiBytes.extend([17, 31, 73, 47, 23])

    # print('asciiBytes = ' + str(asciiBytes))

    listSize = 256
    theList = list(range(listSize))

    # print('theList = ' + str(theList))

    hashEngine = HashEngine(theList, asciiBytes)
    
    for i in range(0, 64):
        hashEngine.DoRound()

    # Convert from sparse to dense hash
    denseHash = []
    for i in range(0, 16):
        # O.K. to start with 0 when XORing
        value = 0
        for j in range(0, 16):
            value ^= theList[i*16 + j]

        # print('value = ' + str(value))
        denseHash.append(value)

    # print('denseHash = ' + str(denseHash))

    hexString = ''
    for hexVal in denseHash:
        # print('hexVal = ' + str(hexVal))
        hexString += "{0:0{1}x}".format(hexVal, 2)
        # print('hexString = ' + hexString)

    mutli = theList[0]*theList[1]
    print('hex string (answer part 2) = ' + hexString)


Part1()
Part2()