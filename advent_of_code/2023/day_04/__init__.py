values_file = open('values.txt', 'r')
values = values_file.readlines()

card_score_sum = 0
for card in values:
    card_split = str.split(card, ':')
    numbers_split = str.split(card_split[1], '|')
    your_numbers = set(map(int, numbers_split[0].strip().split()))
    winning_numbers = set(map(int, numbers_split[1].strip().split()))

    matching_numbers = your_numbers.intersection(winning_numbers)
    matching_count = len(matching_numbers)
    if matching_count != 0:
        card_score = 1 if matching_count == 1 else 2 ** (matching_count - 1)
        card_score_sum += card_score

print(f'answer is {card_score_sum}')
