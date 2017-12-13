connections = []

with open('input.txt', newline='') as file:
    for line in file:
        connPrograms = line[line.index('>') + 2:]                    
        connPrograms = [x.strip() for x in connPrograms.split(',')]
        connPrograms = list(map(int, connPrograms))        
        connections.append(connPrograms)


def FindGroup(startProgram):
    group = []
    WalkPipes(startProgram, group)
    return group

def WalkPipes(index, group):    
    group.append(index)

    connPrograms = connections[index]

    for connProgram in connPrograms:
        # Make sure we havn't already visited this program!
        if not connProgram in group:
            WalkPipes(connProgram, group)


group0 = FindGroup(0)
print('num of programs in group 0 (part 1 answer) = ' + str(len(group0)))

def FindNumGroups():
    groups = []

    for index, connection in enumerate(connections):
        # First, check if this program (index) is already part
        # of a group
        alreadyInGroup = False
        for group in groups:
            if index in group:
                alreadyInGroup = True
                break

        if not alreadyInGroup:            
            group = FindGroup(index)
            groups.append(group)                    

    return len(groups)

numGroups = FindNumGroups()
print('numGroups (part 2 answer) = ' + str(numGroups))