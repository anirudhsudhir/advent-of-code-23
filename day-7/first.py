import re

inputData = {}
cardSplit = {}
handTypeSorted = {}
completeSort = {}
rank = 0
totalBet = 0

cardStrength = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}

with open("input.txt") as file:
    for line in file.readlines():
        words = re.findall(r"(\w+)", line)
        inputData[words[0]] = int(words[1])

for card in inputData.keys():
    tempStore = {}
    for char in card:
        if char in tempStore:
            tempStore[char] += 1
        else:
            tempStore[char] = 1
    cardSplit[card] = sorted(tempStore.values())

for card in cardSplit:
    cardValues = cardSplit[card]
    cardType = 0
    if cardValues == [5]:
        cardType = 7
    elif cardValues == [1, 4]:
        cardType = 6
    elif cardValues == [2, 3]:
        cardType = 5
    elif cardValues == [1, 1, 3]:
        cardType = 4
    elif cardValues == [1, 2, 2]:
        cardType = 3
    elif cardValues == [1, 1, 1, 2]:
        cardType = 2
    elif cardValues == [1, 1, 1, 1, 1]:
        cardType = 1
    if cardType not in handTypeSorted:
        handTypeSorted[cardType] = []
    handTypeSorted[cardType].append(card)

for hand in handTypeSorted:
    cards = handTypeSorted[hand]
    sortedList = []
    for i in range(len(cards) - 1):
        for j in range(len(cards) - i - 1):
            for k in range(len(cards[j])):
                cardVal1 = cardStrength[cards[j][k]]
                cardVal2 = cardStrength[cards[j + 1][k]]
                if cardVal1 > cardVal2:
                    tempCard = cards[j]
                    cards[j] = cards[j + 1]
                    cards[j + 1] = tempCard
                    break
                elif cardVal1 < cardVal2:
                    break
                elif cardVal1 == cardVal2:
                    continue
    handTypeSorted[hand] = cards

for i in range(1, 8):
    if i not in handTypeSorted:
        continue
    cards = handTypeSorted[i]
    for card in cards:
        rank += 1
        totalBet += rank * inputData[card]

print(totalBet)
