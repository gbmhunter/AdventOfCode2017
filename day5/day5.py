
input = open('input.txt')
inputLines = input.readlines()

instrList = []
for line in inputLines:
    instrList.append(int(line))

canExit = False
index = 0
steps = 0
while True:

    if index < 0 or index >= len(instrList):
        break

    instr = instrList[index]
    # print('instr = ' + str(instr))

    # Increment current instruction by 1
    instrList[index] = instr + 1

    # Update index
    index += instr   

    steps += 1

print('answer (part 1) = ' + str(steps)) 

instrList = []
for line in inputLines:
    instrList.append(int(line))

canExit = False
index = 0
steps = 0
while True:

    if index < 0 or index >= len(instrList):
        break

    instr = instrList[index]
    # print('instr = ' + str(instr))

    # Perform instruction update rules
    if instr >= 3:
        instrList[index] = instr - 1
    else:
        instrList[index] = instr + 1

    # Update index
    index += instr   

    steps += 1

print('answer (part 2) = ' + str(steps)) 