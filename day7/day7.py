class Node:
    def __init__(self):
        self.name = ""
        self.parent = None
        self.children = []

    def __str__(self):
        output = '{ '
        output += 'name = ' + self.name
        output += ', parent = ' + str(self.parent)
        output += ', children = ' + str(self.children)
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

