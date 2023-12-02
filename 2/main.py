import re
import operator
from functools import reduce

data = open('./data_input.txt', "r")


def get_group_numbers_and_colours(group):
    colour = "".join(filter(str.isalpha, group))
    number = "".join(filter(str.isdigit, group))
    return colour, int(number)


def get_game_id_and_sets(game):
    regex = "^Game (?P<id>[0-9]+):(?P<sets>.+)$"
    search = re.search(regex, game)
    game_id = search.group("id")
    sets = re.split(";", search.group("sets"))
    return int(game_id), sets


def get_id_sum(games):
    limits = {"red": 12, "green": 13, "blue": 14}
    id_sum = 0

    for game in games:
        game_id, sets = get_game_id_and_sets(game)

        game_is_valid = True
        for game_set in sets:
            if not game_is_valid:
                continue

            groups = re.split(", ", game_set)

            for group in groups:
                if not game_is_valid:
                    continue

                colour, number = get_group_numbers_and_colours(group)

                if number > limits[colour]:
                    game_is_valid = False

        if game_is_valid:
            id_sum += game_id

    return id_sum


def get_power_sum(games):
    power_sum = 0

    for game in games:
        minimums = {"red": 0, "green": 0, "blue": 0}
        _, sets = get_game_id_and_sets(game)

        for game_set in sets:
            groups = re.split(", ", game_set)

            for group in groups:
                colour, number = get_group_numbers_and_colours(group)

                if minimums[colour] < number:
                    minimums[colour] = number

        power_sum += reduce(operator.mul, minimums.values())

    return power_sum


# part 1
print("part 1:", get_id_sum(data))

# part 2
data.seek(0)
print("part 2:", get_power_sum(data))
