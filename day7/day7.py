class Node:
    def __init__(self):
        self.name = ""
        self.parent = None
        self.children = []
        self.selfWeight = -1
        self.totalWeight = -1

    def __str__(self):
        output = '{ '
        output += 'name = ' + self.name
        output += ', parent = ' + str(self.parent)
        output += ', children = ' + str(self.children)
        output += ', selfWeight = ' + str(self.selfWeight)
        output += ' }'
        return output

nodeDict = {}
with open('input.txt', newline='') as file:
    for line in file:        

        # Extract node name
        firstWhitespaceIndex = line.index(" ")        
        
        nodeName = line[0:firstWhitespaceIndex]        

        if not nodeName in nodeDict:
            nodeDict[nodeName] = Node()
            nodeDict[nodeName].name = nodeName

        node = nodeDict[nodeName]

        # Extract self weight
        node.selfWeight = int(line[line.index('(') + 1:line.index(')')])        

        # Extract children
        startOfArrowIndex = line.find("->")
        if startOfArrowIndex != -1:                    
            childrenText = line[startOfArrowIndex + 3:len(line)]

            while True:
                
                commaIndex = childrenText.find(',')                
                foundLastChild = False
                if commaIndex == -1:                    
                    foundLastChild = True

                childName = childrenText[:commaIndex]
                # print('childName = "' + childName + '"')

                # Remove child name from children text
                childrenText = childrenText[commaIndex + 2:]

                node.children.append(childName)

                if not childName in nodeDict:                                    
                    # print('child not in database, creating...')
                    nodeDict[childName] = Node()
                    nodeDict[childName].name = childName

                nodeDict[childName].parent = nodeName


                if foundLastChild:
                    break

        # print('Node = ' + str(node))


# Find root node
currNode = nodeDict[list(nodeDict)[0]]
rootNode = None
while not rootNode:
    if currNode.parent == None:
        rootNode = currNode
    else:
        currNode = nodeDict[currNode.parent]

print('root node (part 1 answer) = ' + rootNode.name)

def checkEqual1(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

def FindWeight(nodeName):
    # print('FindWeight() called. nodeName = ' + nodeName)

    # Sum up children weight
    childWeights = []
    for child in nodeDict[nodeName].children:
        # print('Finding weight for child = ' + child)
        childWeight = FindWeight(child)
        childWeights.append(childWeight)
        # print('childWeight (' + child + ') = ' + str(childWeight))

    if not checkEqual1(childWeights):
        # print('Inbalance found! nodeName = ' + nodeName)
        # print('weights = ' + str(childWeights))

        # Find the one weight that does not match the others!
        correctWeight = -1
        incorrectWeight = -1
        for childWeight in childWeights:
            if childWeights.count(childWeight) == 1:                
                incorrectWeight = childWeight
            else:
                correctWeight = childWeight

        # print('Found incorrect weight of ' + str(incorrectWeight) + ', correct weight = ' + str(correctWeight))

        # Get node with incorrect weight
        childIndex = childWeights.index(incorrectWeight)
        childName = nodeDict[nodeName].children[childIndex]
        # print('incorrect child = ' + str(nodeDict[childName]))

        # Get incorrect child
        incorrectChildTotalWeight = nodeDict[childName].totalWeight
        # print('incorrectChildTotalWeight = ' + str(incorrectChildTotalWeight))

        weightDiff = correctWeight - incorrectWeight

        correctedChildSelfWeight = nodeDict[childName].selfWeight + weightDiff
        print('correctedChildSelfWeight (part 2 answer) = ' + str(correctedChildSelfWeight))

        raise NameError('Test')        

    totalChildWeight = -1
    if len(childWeights) >= 1:
        totalChildWeight = childWeights[0]*len(nodeDict[nodeName].children)
    else:
        totalChildWeight = 0

    totalWeight = nodeDict[nodeName].selfWeight + totalChildWeight
    # print('totalWeight (' + nodeName + ') = ' + str(totalWeight))

    nodeDict[nodeName].totalWeight = totalWeight

    return totalWeight

try:
    FindWeight(rootNode.name)
except NameError as e:
    pass

    

