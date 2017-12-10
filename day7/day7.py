class Node:
    def __init__(self):
        self.name = ""
        self.parent = None
        self.children = []
        self.selfWeight = -1

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
        print('line = ' + str(line))

        # Extract node name
        firstWhitespaceIndex = line.index(" ")
        print('firstWhitespaceIndex = ' + str(firstWhitespaceIndex))
        
        nodeName = line[0:firstWhitespaceIndex]
        print('name = "' + nodeName + '"')

        if not nodeName in nodeDict:
            nodeDict[nodeName] = Node()
            nodeDict[nodeName].name = nodeName

        node = nodeDict[nodeName]

        # Extract self weight
        node.selfWeight = int(line[line.index('(') + 1:line.index(')')])        

        # Extract children
        startOfArrowIndex = line.find("->")
        if startOfArrowIndex != -1:
            
            print('startOfArrowIndex = ' + str(startOfArrowIndex))

            childrenText = line[startOfArrowIndex + 3:len(line)]
            print('childrenText = "' + childrenText + '"')

            while True:

                print('looking in string "' + childrenText + '"')
                commaIndex = childrenText.find(',')
                print('Found comma at ' + str(commaIndex))
                foundLastChild = False
                if commaIndex == -1:
                    print('Found last child.')
                    foundLastChild = True

                childName = childrenText[:commaIndex]
                print('childName = "' + childName + '"')

                # Remove child name from children text
                childrenText = childrenText[commaIndex + 2:]

                node.children.append(childName)

                if not childName in nodeDict:                                    
                    print('child not in database, creating...')
                    nodeDict[childName] = Node()
                    nodeDict[childName].name = childName
                else:
                    print('child already in database.')

                nodeDict[childName].parent = nodeName


                if foundLastChild:
                    break

        else:
            print('Node has no children.')

        print('Node = ' + str(node))


# Find root node
currNode = nodeDict[list(nodeDict)[0]]
rootNode = None
while not rootNode:
    if currNode.parent == None:
        rootNode = currNode
    else:
        currNode = nodeDict[currNode.parent]

print('root node = ' + str(rootNode))

def checkEqual1(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

def FindWeight(nodeName):
    print('FindWeight() called. nodeName = ' + nodeName)

    # Sum up children weight
    childWeights = []
    for child in nodeDict[nodeName].children:
        print('Finding weight for child = ' + child)
        childWeight = FindWeight(child)
        if childWeight == None:
            raise NameError('Test')
        childWeights.append(childWeight)
        print('childWeight (' + child + ') = ' + str(childWeight))

    if not checkEqual1(childWeights):
        print('Inbalance found! nodeName = ' + nodeName)
        print('weights = ' + str(childWeights))
        raise NameError('Test')        

    totalChildWeight = -1
    if len(childWeights) == 1:
        totalChildWeight = childWeights.pop()*len(nodeDict[nodeName].children)
    else:
        totalChildWeight = 0

    totalWeight = nodeDict[nodeName].selfWeight + totalChildWeight
    print('totalWeight (' + nodeName + ') = ' + str(totalWeight))

    return totalWeight

FindWeight(rootNode.name)
    

