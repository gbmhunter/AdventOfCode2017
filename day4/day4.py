input = open('input.txt')
inputLines = input.readlines()

numValid = 0

def IsAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

for line in inputLines:
    words = line.split()    
    wordDict = {}

    duplicateWordFound = False
    for word in words:
        
        if word in wordDict:
            # Not valid, skip to next passphrase            
            duplicateWordFound = True
        else:
            wordDict[word] = 1
    
    if not duplicateWordFound:
        numValid += 1

print('answer (part 1) = ' + str(numValid))

numValid = 0
for line in inputLines:
    words = line.split()    
    wordDict = {}

    duplicateWordFound = False
    for word in words:
        
        if word in wordDict:
            # Not valid, skip to next passphrase            
            duplicateWordFound = True
        else:
            wordDict[word] = 1

        for word2 in words:
            if word2 == word:
                continue

            if IsAnagram(word, word2):
                duplicateWordFound = True
    
    if not duplicateWordFound:
        numValid += 1

print('answer (part 2) = ' + str(numValid))

        

