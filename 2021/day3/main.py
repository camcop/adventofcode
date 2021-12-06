# Import input list
with open('./2021/day3/input.txt') as f:
    inputs = f.readlines()
    input_list = [input.strip() for input in inputs]


## Part 1
# Create dictionary to contain counts of 0s and 1s at each digit position
d = {}
for i in range(len(input_list[0])):
    d[f'{i}'] = 0

for num in input_list:
    for i, bit in enumerate(num):
        d[str(i)] += int(bit)


# Calculate gamma and epsilon in binary
hurdle = int(len(input_list) / 2)
gamma = [(d[dig] > hurdle) * 1 for dig in d]
epsilon = [1 - i for i in gamma]


# Convert gamma and epsilon to decimal
def bin_to_dec(bin: list):
    dec = 0
    for i, d in enumerate(reversed(bin)):
        dec += (2 ** i) * d
    return dec

# Calculate answer to part 1
part1 = bin_to_dec(gamma) * bin_to_dec(epsilon)
print(part1)


## Part 2
# Collapse list to one element based on conditions in question
def select_winner(in_list: list, priority: int) -> list:
    d = 0
    while len(in_list) > 1:
        zeroes_list = [n for n in in_list if n[d] == '0']
        ones_list = [n for n in in_list if n[d] == '1']
        if priority == 1:
            out_list = ones_list if len(ones_list) >= len(zeroes_list) else zeroes_list
        elif priority == 0:
            out_list = zeroes_list if len(zeroes_list) <= len(ones_list) else ones_list
        in_list = out_list
        d += 1
    return in_list

# Calculate oxygen and c02
oxygen = select_winner(input_list, 1)[0]
c02 = select_winner(input_list, 0)[0]

# Convert oxygen and c02 to decimal and calculate answer to part 2
part2 = bin_to_dec([int(i) for i in oxygen]) * bin_to_dec([int(i) for i in c02])
print(part2)