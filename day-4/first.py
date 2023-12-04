total_score = 0
data = []

with open("first_input.txt","r") as file:
    for line in file.readlines():
        data.append(line[:len(line)-1])

for line in data:
    game_data = line.split(":")[1].split("|")
    winning_numbers = game_data[0].split(" ")
    card_numbers = game_data[1].split(" ")
    winning_numbers_list, card_numbers_list = [] , []
    round_score = 0
    for element in winning_numbers:
        if element.isdigit():
            winning_numbers_list.append(element)
    for element in card_numbers:
        if element.isdigit():
            card_numbers_list.append(element)
    for element in winning_numbers_list:
        if element in card_numbers_list:
            if round_score == 0:
                round_score = 1
            else:
                round_score *=2

    total_score += round_score

print(total_score)