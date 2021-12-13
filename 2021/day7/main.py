def import_input_file() -> list:
    '''Open input file'''
    with open('./2021/day7/input.txt') as f:
        lines = f.readlines()
        input_list = [int(l.strip()) for l in lines[0].split(',')]
    return input_list

   
def fuel_spent_part1(input: list, point: int) -> int:
    return sum(abs(i - point) for i in input)

   
def fuel_spent_part2(input: list, point: int) -> int:
    total = 0
    for i in input:
        total += (abs(i - point) ** 2 + abs(i - point)) // 2
    return total
        

def iterate_to_ans(func, input: list, point: int) -> int:
    min = func(input, point)
    
    i = 1
    while func(input, point + i) < min:
        min = func(input, point + i)
        i += 1

    i = -1
    while func(input, point + i) < min:
        min = func(input, point + i)
        i -= 1
 
    return min

   
if __name__ == '__main__':
    input = import_input_file()
    mid = max(i for i in input) // 2

    part1 = iterate_to_ans(fuel_spent_part1, input, mid)
    print(part1)

    part2 = iterate_to_ans(fuel_spent_part2, input, mid)
    print(part2)
