import re

data = open('./data_input.txt', "r")
limits = {"red": 12, "green": 13, "blue": 14}
id_sum = 0

for line in data:
    regex = "^Game (?P<game>[0-9]+):(?P<sets>.+)$"
    search = re.search(regex, line)
    game = search.group("game")
    sets = re.split(";", search.group("sets"))

    game_is_valid = True
    for game_set in sets:
        if not game_is_valid:
            continue

        colours = re.split(", ", game_set)

        for colour in colours:
            if not game_is_valid:
                continue

            number = "".join(filter(str.isdigit, colour))
            colour = "".join(filter(str.isalpha, colour))

            if int(number) > limits[colour]:
                game_is_valid = False

    if game_is_valid:
        id_sum += int(game)


print(id_sum)
