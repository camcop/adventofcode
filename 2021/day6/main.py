def import_input_file() -> list:
    '''Open input file'''
    with open('./2021/day6/sample_input.txt') as f:
        lines = f.readlines()
        input_list = [int(l.strip()) for l in lines[0].split(',')]
    return input_list



## Formula for number of fish if one fish and doubles every day
# 2 ^ day
# 0: 1
# 1: 2
# 2: 4
# 3: 8
## Formula for number of fish if one fish and doubles every 7 days
# 2 ^ (day // 7)
## Formula for number of fish if multiple fish and doubles every 7 days
# for i in fish sum(2 ^ ((day - offset[i]) // 7))

# def count_exponential(fish: list, day: int) -> int:
#     count = 0
#     for f in fish:
#         count += 2 ** ((day - f) // 7)
#     return count

def count_exponential(fish: list, day: int) -> int:
    count = 0
    for f in fish:
        # unit_mature = 7
        # unit_immature = 9
        power1 = max(((day - f + 7 - 1) // 7), 0)
        count += 2 ** power1
        
        power2 = max(((day - f + 9 - 1) // 9), 0)
        count += 2 ** power2
        
        count -= 1
    return count


'''
Should be able reduce to a formula for the number of fish on day n from each fish
However, as there is an extra 2 day gestation period on first generation, does not simplify cleanly

For each fish:
Simple case:
First generation: 1 splits to 2, 2 mature (7 days)
Second generation: 2 split to 4, 4 mature (7 days)
Third generation: 4 split to 8, 8 mature (7 days)
Number of fish for each fish = 2 ^ (day // 7)
With offset: 2 ^ ((day - offset) // 7)
For all fish: for i in fish sum(2 ^ ((day - offset[i]) // 7))

Complex case:
First generation: 1 splits to 2, 1 mature (7 days), 1 immature (9 days)
Second generation: 2 split to 4, 2 mature (7 days), 2 immature (9 days)
Third generation: 4 split to 8, 4 mature (7 days), 4 immature (9 days)

Number of mature fish per OG fish: 2 ^ ((day // 7) - 1)
Number of immature fish per OG fish: 2 ^ ((day // 9) - 1)

With offset:
Mature fish = 2 ^ (((day - offset) // 7) - 1)
Immature fish = 2 ^ (((day - offset) // 9 - 1)


'''

   
if __name__ == '__main__':
    input = import_input_file()
    print(input)

    ans = count_exponential(input, 25)
    print(ans)
