with open('./2021/day2/input.txt') as f:
    inputs = f.readlines()
    input_list = [input.strip() for input in inputs]

x = 0
y = 0

for inp in input_list:
    inp_spl = inp.split()
    match inp_spl[0]:
        case 'forward':
            x += int(inp_spl[1])
        case 'up':
            y -= int(inp_spl[1])
        case 'down':
            y += int(inp_spl[1])

print(x * y)