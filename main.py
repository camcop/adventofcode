def import_input_file():
    with open('input.txt') as f:
        lines = f.readlines()
        input_list = [int(line.strip()) for line in lines]
    return input_list


def count_increases(input: list):
    inc_count = 0
    for i, num in enumerate(input):
        if num > input[i - 1]:
            inc_count += 1
    return inc_count


def count_rolling_threes_increases(input: list):
    inc_count = 0
    for i, num in enumerate(input):
        if num > input[i - 3]:
            inc_count += 1
    return inc_count


if __name__ == '__main__':
    input = import_input_file()
    print(count_increases(input))
    print(count_rolling_threes_increases(input))