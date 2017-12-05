import math
input = 277678
# input = 9

print('input = ' + str(input))
input = input - 1

print('adjInput = ' + str(input))

sqrtInput = math.sqrt(input)

sqrtFloor = math.floor(sqrtInput)

print('sqrtFloor = ' + str(sqrtFloor))

if sqrtFloor % 2 == 0:
    squaresOnPrevBoxEdge = sqrtFloor - 1
else:
    squaresOnPrevBoxEdge = sqrtFloor

thisStart = math.pow(squaresOnPrevBoxEdge, 2)

squaresOnBoxEdge = squaresOnPrevBoxEdge + 2
print('squaresOnBoxEdge = ' + str(squaresOnBoxEdge))


print('thisStart = ' + str(thisStart))

indexInBox = input - thisStart
print('indexInBox = ' + str(indexInBox))

squaresPerEdge = squaresOnBoxEdge - 1

modIndexInBox = indexInBox % squaresPerEdge
print('modIndexInBox = ' + str(modIndexInBox))

radius = squaresPerEdge/2
print('radius = ' + str(radius))

distanceFromMiddleOfEdge = math.fabs(modIndexInBox - (radius - 1))
print('distanceFromMiddleOfEdge = ' + str(distanceFromMiddleOfEdge))
distanceFromCenter = distanceFromMiddleOfEdge + radius
print('distanceFromCenter = ' + str(distanceFromCenter))