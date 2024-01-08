import math
import re

nodeData = {}
totalStepCount = {}

with open("input.txt") as file:
    file.readline()
    file.readline()
    for line in file.readlines():
        words = re.findall(r"(\w+)", line)
        nodeData[words[0]] = (words[1], words[2])

for node in nodeData:
    if node.endswith("Z"):
        if node in totalStepCount:
            totalStepCount[node] += 1
        else:
            totalStepCount[node] = 1
        print(node)
    for nodeVals in nodeData[node]:
        if nodeVals.endswith("Z"):
            if nodeVals in totalStepCount:
                totalStepCount[nodeVals] += 1
            else:
                totalStepCount[nodeVals] = 1
            print(nodeVals)

print(math.prod(totalStepCount.values()))
print(totalStepCount)
