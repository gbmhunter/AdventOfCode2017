class Node:
    def __init__(self):
        self.name = ""
        self.parent = {}
        self.children = []

    def __str__(self):
        output = '{ '
        output += 'name = ' + self.name
        output += ', parent = ' + str(self.parent)
        output += ', children = ' + str(self.children)
        output += ' }'
        return output

with open('input.txt', newline='') as file:
    for line in file:
        print('line = ' + str(line))

        # Extract node name
        firstWhitespaceIndex = line.index(" ")
        print('firstWhitespaceIndex = ' + str(firstWhitespaceIndex))

        node = Node()
        node.name = line[0:firstWhitespaceIndex]
        print('name = "' + node.name + '"')

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

                if foundLastChild:
                    break

        else:
            print('Node has no children.')

        print('Node = ' + str(node))


print('Test')