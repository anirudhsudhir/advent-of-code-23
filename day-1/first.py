with open("first_input.txt", "r") as file:
    lines = file.readlines()

calibrationSum = 0
for line in lines:
    nums = []
    for letter in line:
        if letter.isdigit():
            nums.append(letter)
    calibrationSum += int(nums[0] + nums.pop())

print(calibrationSum)
