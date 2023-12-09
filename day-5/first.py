fileData = []
seeds = []
maps = {}
lowestLocation = False

with open("input.txt") as file:
    for line in file.readlines():
        if line[len(line)-1] == '\n':
            line = line[: len(line) - 1]
        line += " "
        fileData.append(line.split())

for word in fileData[0]:
    if word.isdigit():
        seeds.append(int(word))

mapReadStatus = False
currentMap = ""
for line in fileData[1:]:
    if line == []:
        continue
    elif "map:" in line:
        mapReadStatus = True
        tempLi = []
        maps[line[0]] = tempLi
        currentMap = line[0]
    else:
        tempLi = []
        for num in line:
            tempLi.append(int(num))
        maps[currentMap].append(tempLi)

for seed in seeds:
    nextVal = seed
    for map in maps.values():
        for element in map:
            if nextVal >= element[1] and nextVal<=element[1]+element[2]-1:
                nextVal = element[0] + (nextVal - element[1])
                break
    if lowestLocation == False:
        lowestLocation = nextVal
    elif lowestLocation > nextVal:
        lowestLocation = nextVal

print(lowestLocation)
