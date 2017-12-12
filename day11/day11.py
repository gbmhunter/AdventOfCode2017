directions = []
with open('input.txt', newline='') as file:
    for line in file:
        directions = line.split(',')
# directions = ['n', 'ne']

def GetManhattanDistance(x, y, z):
    return (abs(x) + abs(y) + abs(z)) / 2

x = 0
y = 0
z = 0
furthestDistance = 0
for direction in directions:
    if direction == 'n':
        y += 1
        z -= 1
    elif direction == 'ne':
        x += 1
        z -= 1
    elif direction == 'se':
        x += 1
        y -= 1
    elif direction == 's':
        y -= 1
        z += 1
    elif direction == 'sw':
        x -= 1
        z += 1
    elif direction == 'nw':
        x -= 1
        y += 1
    else:    
        assert False

    distance = GetManhattanDistance(x, y, z)
    if distance > furthestDistance:
        furthestDistance = distance

# Calculate Manhattan distance
distance = GetManhattanDistance(x, y, z)
print('final distance (part 1 answer) = ' + str(distance))
print('furthest distance (part 2 answer) = ' + str(furthestDistance))