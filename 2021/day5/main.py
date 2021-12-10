def import_input_file() -> list:
    '''Open input file and reformat input into list'''
    with open('./2021/day5/input.txt') as f:
        lines = f.readlines()
        input_list = [line.strip() for line in lines]

        coords = [pair.split(' -> ') for pair in input_list]
        start = tuple(tuple(int(c) for c in coord[0].split(',')) for coord in coords)
        end = tuple(tuple(int(c) for c in coord[1].split(',')) for coord in coords)
        inp_f = [(start[i], end[i]) for i, coord in enumerate(coords)]
    return inp_f


def deselect_diagonal(input: list) -> list:
    '''Return list of only horizontal and vertical lines'''
    output_list = []
    for i in input:
        if i[0][0] == i[1][0] or i[0][1] == i[1][1]:
            output_list.append(i)
    return output_list


def create_coords_dict() -> dict:
    '''Create empty dictionary of all coordinates in space'''
    d = {}
    for i in range(1000):
        for j in range(1000):
            d[(i, j)] = 0
    return d


def count_coords(dict: dict, input: list) -> dict:
    '''Populate dictionary with counts of coordinates of each line'''
    for i in input:
        if i[0][0] == i[1][0]: #Vertical line as x coords are equal
            for j in range(abs(i[0][1] - i[1][1]) + 1):
                dict[(i[0][0], min(i[0][1], i[1][1]) + j)] += 1
        elif i[0][1] == i[1][1]: #Horizontal line as y coords are equal
            for j in range(abs(i[0][0] - i[1][0]) + 1):
                dict[(min(i[0][0], i[1][0]) + j, i[0][1])] += 1
        else: #Diagonal line as neither x nor y are equal
            for j in range(abs(i[0][0] - i[1][0]) + 1):
                dict[((i[0][0] + (j * (-1 if (i[0][0] > i[1][0]) else 1))), i[0][1] + (j * (-1 if (i[0][1] > i[1][1]) else 1)))] += 1
    return dict 


def count_overlaps(dict: dict, hurdle: int) -> int:
    '''Count values in dictionary which are at least hurdle'''
    count = 0
    for k in dict:
        if dict[k] >= hurdle:
            count += 1
    return count


if __name__ == '__main__':
    input = import_input_file()
    # print(input)

    # Part1 
    no_diagonals = deselect_diagonal(input)
    # print(no_diagonals)
    count_dict = create_coords_dict()
    # print(count_dict)
    count_dict_populated = count_coords(count_dict, no_diagonals)
    # print(count_dict_populated)
    ans = count_overlaps(count_dict_populated, 2)
    # print(ans)

    # Part2
    count_dict = create_coords_dict()
    # print(count_dict)
    count_dict_populated = count_coords(count_dict, input)
    # print(count_dict_populated)
    ans = count_overlaps(count_dict_populated, 2)
    print(ans)