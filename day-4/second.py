total_cards = 0
card_data = {}
data = []
current_card = 1 

with open("first_input.txt","r") as file:
    for line in file.readlines():
        data.append(line[:len(line)-1])

for i in range(1,len(data)+1):
    card_data[i] = 1

for line in data:
    for i in range(card_data[current_card]): 
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
                round_score+=1
        for i in range(1,round_score+1):
            if current_card+i > len(data):
                break
            if card_data[current_card+i] == 0:
                card_data[current_card+i] = 1
            else:
                card_data[current_card+i] += 1

    print(current_card)
    current_card += 1

total_cards = sum(card_data.values())
print("Total Cards: ",total_cards)