data = []
game_power_sum = 0

with open("first_input.txt", "r") as file:
    for line in file.readlines():
        data.append(line[: len(line) - 1])

for game in data:
    split_data = game.split(":")
    game_data = split_data[1]
    set_colours = {"red": 0, "green": 0, "blue": 0}
    subset_colours = {"red": 0, "green": 0, "blue": 0}
    set_power = 1
    for subset in game_data.split(";"):
        for words in subset.split(","):
            # Ignoring the empty character emiited by split
            colours = words.split(" ")[1:]
            subset_colours[colours[1]] = int(colours[0])
        for colour in set_colours:
            set_colours[colour] = max(set_colours[colour], subset_colours[colour])
    for colour in set_colours:
        set_power *= set_colours[colour]
    game_power_sum += set_power

print(game_power_sum)
