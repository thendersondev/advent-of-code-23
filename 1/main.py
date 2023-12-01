def digitise_verbose_digits(value: str):
    digits_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    transformed = value
    for key in digits_map.keys():
        if value.__contains__(key):
            # this key + digits_map[key] + key kinda sucks
            transformed = transformed.replace(key, key + digits_map[key] + key)

    return transformed


def get_calibration_sum(data):
    values = []

    for line in data:
        digitised = digitise_verbose_digits(line)
        numbers = "".join(filter(str.isdigit, digitised))
        length = len(numbers)

        if length == 0:
            continue

        if length == 1:
            values.append(numbers + numbers)
            continue

        if length > 1:
            values.append(numbers[0] + numbers[length - 1])
            continue

    return sum(map(int, values))


print(get_calibration_sum(open('./data_input.txt', "r")))
