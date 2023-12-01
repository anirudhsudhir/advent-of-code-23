with open("first_input.txt", "r") as file:
    lines = file.readlines()

ones = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
totalSum = 0

all_combinations = {}
line_count = 0

for line in lines:
    temp_li = []
    for i in range(len(line)):
        for j in range(len(line)):
            if line[i:j] != "":
                temp_li.append(line[i:j])
    all_combinations[line_count] = temp_li
    line_count += 1

line_nums = {}
line_count2 = 0

for line in all_combinations:
    temp_li = []
    for element in all_combinations[line]:
        if element.isdigit() and int(element) <= 9:
            temp_li.append(element)
        elif element in ones:
            temp_li.append(ones[element])
    line_nums[line_count2] = temp_li
    totalSum += int(str(temp_li[0]) + str(temp_li.pop()))
    line_count2 += 1

print(totalSum)
