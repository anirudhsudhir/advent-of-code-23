inputData = []
engineGearSum = 0
engineGearCombinations = {}

with open("input.txt") as file:
    for line in file.readlines():
        line =line[:len(line)-1]
        tempLi = []
        for char in line:
            tempLi.append(char)
        inputData.append(tempLi)

for i in range(len(inputData)):
    countFinished = True
    currentNum = ""
    for j in range(len(inputData[i])):
        char = inputData[i][j]
        if char.isdigit():
            countFinished = False
            currentNum += char
        elif (not char.isdigit()) and countFinished == False:
            countFinished = True
        if j == len(inputData[i]) - 1:
            countFinished = True
        if currentNum != "" and countFinished == True:
            for row in range(i-1,i+2):
                for col in range(j-1-len(currentNum),j+1):
                    if row<0 or row>=len(inputData) or col<0 or col>=len(inputData[i]):
                        continue
                    boundaryElement = inputData[row][col]
                    if boundaryElement == '*':
                        coodinates = (row,col)
                        if coodinates in engineGearCombinations.keys():
                            engineGearCombinations[coodinates].append(currentNum)
                        else:
                            temp_li = list()
                            temp_li.append(currentNum)
                            engineGearCombinations[coodinates] = temp_li
            # if isEnginePart:
            #     enginePartSum += int(currentNum)
            #     isEnginePart = False
            currentNum = ""

for combination in engineGearCombinations.values():
    if len(combination) == 2:
        engineGearSum += int(combination[0]) * int(combination[1])

print(engineGearSum)