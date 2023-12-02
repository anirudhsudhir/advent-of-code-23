data = []
gameid_sum = 0

with open("first_input.txt", "r") as file:
    for line in file.readlines():
        data.append(line[: len(line) - 1])

for game in data:
    split_data = game.split(":")
    game_id = int(split_data[0].split(" ")[1])
    game_data = split_data[1]
    subset_colours = {"red": 0, "green": 0, "blue": 0}
    game_status = True
    for subset in game_data.split(";"):
        for words in subset.split(","):
            # Ignoring the empty character emiited by split
            colours = words.split(" ")[1:]
            subset_colours[colours[1]] = int(colours[0])
            if (
                subset_colours["red"] > 12
                or subset_colours["green"] > 13
                or subset_colours["blue"] > 14
            ):
                game_status = False
    if game_status:
        gameid_sum += game_id

print(gameid_sum)
