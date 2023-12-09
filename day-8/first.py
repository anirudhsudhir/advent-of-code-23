import re

nodeData = {}
directionData = ""
currentDirectionMarker = 0
totalStepCount = 0


def direction():
    global currentDirectionMarker
    if currentDirectionMarker == len(directionData):
        currentDirectionMarker = 0
    dir = directionData[currentDirectionMarker]
    currentDirectionMarker += 1
    if dir == "L":
        return 0
    return 1


with open("input.txt") as file:
    directionData = re.findall(r"\w+", file.readline())[0]
    file.readline()
    for line in file.readlines():
        words = re.findall(r"(\w+)", line)
        nodeData[words[0]] = (words[1], words[2])

start = "AAA"
while start != "ZZZ":
    tempDirection = direction()
    start = nodeData[start][tempDirection]
    totalStepCount += 1

print(totalStepCount)
