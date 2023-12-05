inputData = []
enginePartSum = 0

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
    isEnginePart = False
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
                    if (not boundaryElement.isalnum()) and boundaryElement!='.':
                        isEnginePart = True
            if isEnginePart:
                enginePartSum += int(currentNum)
                isEnginePart = False
            currentNum = ""

print(enginePartSum)