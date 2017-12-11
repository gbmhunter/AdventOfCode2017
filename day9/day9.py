stream = ''
with open('input.txt', newline='') as file:
    for line in file:
        stream = line

def Process(stream):
    print('Process() called with stream = ' + stream)

    ignoreNextChar = False
    inGarbage = False
    groupDepth = 0
    totalScore = 0
    for char in stream:

        print('char = ' + char + ', groupDepth = ' + str(groupDepth) + ', totalScore = ' + str(totalScore))

        if ignoreNextChar:
            print('Ignoring this char.')
            ignoreNextChar = False            
        elif char == '!':
            print('Found "!", ignoring next char...')
            ignoreNextChar = True            
        elif char == '<' and not inGarbage:
            print('Found start of garbage...')
            inGarbage = True            
        elif char == '>' and inGarbage:
            print('Found end of garbage.')
            inGarbage = False          
        elif char == '{' and not inGarbage:
            print('Found start of group.')
            groupDepth += 1
            totalScore += groupDepth
        elif char == '}' and not inGarbage:
            print('Found end of group.')
            groupDepth -= 1            
        else:
            print('Found garbage.')

    return totalScore

assert Process('{}') == 1
assert Process('{{{}}}') == 6    
assert Process('{{},{}}') == 5    
assert Process('{{{},{},{{}}}}') == 16    
assert Process('{<a>,<a>,<a>,<a>}') == 1
assert Process('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
assert Process('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9 
assert Process('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3
score = Process(stream)
print('score = ' + str(score))