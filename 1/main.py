def get_calibration_sum(data):
    values = []

    for line in data:
        numbers = "".join(filter(str.isdigit, line))
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
