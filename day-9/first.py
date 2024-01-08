import re

inputData = {}
count = 0
totalLineCounts = 0
totalExtrapolation = 0

with open("sampleinput.txt") as file:
    for line in file.readlines():
        nums = re.findall(r"(-?\w+)", line)
        count += 1
        inputData[count] = [[int(num) for num in nums]]

# print(inputData)
for key in inputData:
    count = 0
    nums = inputData[key][count]
    while sum(nums) != 0:
        count += 1
        tempLi = list(map(lambda i: nums[i + 1] - nums[i], range(len(nums) - 1)))
        inputData[key].append(tempLi)
        nums = inputData[key][count]
    # Start
    # print(inputData)
    inputData[key][count].append(0)
    count -= 1
    while count >= 0:
        inputData[key][count].append(
            inputData[key][count + 1][len(inputData[key][count + 1]) - 1]
            + inputData[key][count][len(inputData[key][count]) - 1]
        )
        count -= 1
    extraElement = inputData[key][0][len(inputData[key][0]) - 1]
    print(extraElement)
    totalExtrapolation += extraElement
    print("total extra", totalExtrapolation)
    totalLineCounts += 1


print(inputData)
print(totalExtrapolation)
print(totalLineCounts)
