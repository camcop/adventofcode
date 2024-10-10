# Import input list
def import_input_file():
    with open('./2021/day4/input.txt') as f:
        lines = f.readlines()
        input_list = [line.strip() for line in lines]
    return input_list


# Create bingo cards structured as card, line, number (list of list of lists)
def separate_input(input: list):
    callouts = [int(i) for i in input[0].split(',')]
    # print(callouts)
    
    bingo_cards = []
    input = input[1:]
    for i in range(len(input) // 6):
        card = input[6 * i + 1: 6 * i + 6]
        # print(card)
        card_clean = []
        for line in card:
            card_clean.append([int(i) for i in line.split()])
            # print(line)        
        bingo_cards.append(card_clean)
    return callouts, bingo_cards


# Play bingo one number at a time
def play_bingo(number_called: int, cards: list) -> list:
  
    # Call number
    print(f'{number_called=}')
    
    # Remove matches from each card
    for card in cards:
        for row in card:
            for i, num in enumerate(row):
                if num == number_called:
                    row[i] = -1
            # print(row)
    
    return cards


def check_for_bingo(cards: list) -> int:   
    # Check for bingo on row
    for i, card in enumerate(cards):
        bingo_on_card = i
        for row in card:
            for num in row:
                if num != -1:
                    bingo_on_card = -1
            if bingo_on_card != -1:
                print("Bingo on row!")
                return bingo_on_card

    # Check for bingo on column
        for j in range(5):
            bingo_on_card = i
            for row in card:
                if row[j] != -1:
                    bingo_on_card = -1
            if bingo_on_card != -1:
                print("Bingo on column!")
                return bingo_on_card

    return bingo_on_card


def calculate_score(cards: list, winning_card: int):
    print(cards[winning_card])
    sumtotal = 0
    for row in cards[winning_card]:
        for num in row:
            if num != -1:
                sumtotal += num
    return sumtotal



if __name__ == '__main__':
    input = import_input_file()
    # print(input)
    callouts, bingo_cards = separate_input(input)

    bingo_on_card = -1
    k = 0
    while bingo_on_card == -1:
        print(f'{k=}')
        if len(callouts) < 1:
            print("No numbers left to call")
            bingo_on_card = -2
        bingo_cards = play_bingo(callouts[k], bingo_cards)
        # for card in bingo_cards:
        #     print(card)
        bingo_on_card = check_for_bingo(bingo_cards)
        if bingo_on_card == -1:
            k += 1
    print(f'{bingo_on_card=}')
    
    sumtotal = calculate_score(bingo_cards, bingo_on_card)
    print(sumtotal)

    winning_score = calculate_score(bingo_cards, bingo_on_card) * callouts[k]
    print(winning_score)
