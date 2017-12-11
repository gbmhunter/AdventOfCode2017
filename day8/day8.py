
class Instruction:
    def __str__(self):
        output = '{ '
        output += 'targetReg = ' + self.targetReg
        output += ', incOrDec = ' + self.incOrDec
        output += ', amount = ' + str(self.amount)
        output += ', ifReg = ' + self.ifReg
        output += ', ifOperator = ' + self.ifOperator
        output += ', ifAmount = ' + str(self.ifAmount)
        output += ' }'
        return output

instructions = []

with open('input.txt', newline='') as file:
    for line in file: 
        symbols = line.split()
        instruction = Instruction()
        instruction.targetReg = symbols[0]
        instruction.incOrDec = symbols[1]
        instruction.amount = int(symbols[2])
        instruction.ifReg = symbols[4]
        instruction.ifOperator = symbols[5]
        instruction.ifAmount = int(symbols[6])
        instructions.append(instruction)

regValues = {}
highestValueEver = None

# Instructions have been decoded, now run them
for instruction in instructions:

    # First check if if statment True or False
    if not instruction.ifReg in regValues:
        regValues[instruction.ifReg] = 0

    ifResult = None
    if instruction.ifOperator == '>':        
        ifResult = regValues[instruction.ifReg] > instruction.ifAmount
    elif instruction.ifOperator == '<':        
        ifResult = regValues[instruction.ifReg] < instruction.ifAmount
    elif instruction.ifOperator == '>=':        
        ifResult = regValues[instruction.ifReg] >= instruction.ifAmount
    elif instruction.ifOperator == '<=':        
        ifResult = regValues[instruction.ifReg] <= instruction.ifAmount
    elif instruction.ifOperator == '==':        
        ifResult = regValues[instruction.ifReg] == instruction.ifAmount
    elif instruction.ifOperator == '!=':        
        ifResult = regValues[instruction.ifReg] != instruction.ifAmount
    else:
        raise NameError('Unrecognized if operator. operator = ' + instruction.ifOperator)
    
    if not ifResult:
        # If false, skip to next instruction
        continue

    # If result must be true

    if not instruction.targetReg in regValues:
        regValues[instruction.targetReg] = 0

    if instruction.incOrDec == 'inc':
        regValues[instruction.targetReg] += instruction.amount
    elif instruction.incOrDec == 'dec':
        regValues[instruction.targetReg] -= instruction.amount
    else:
        raise NameError('Unrecognized inc or dec symbol.')

    if highestValueEver == None:
        highestValueEver = regValues[instruction.targetReg]
    else:
        if regValues[instruction.targetReg] > highestValueEver:
            highestValueEver = regValues[instruction.targetReg]


# Find maximum reg value
maxRegValue = max(regValues.values())
print('maxRegValue (part 1 answer) = ' + str(maxRegValue))
print('highest value ever (part 2 answer) = ' + str(highestValueEver))
