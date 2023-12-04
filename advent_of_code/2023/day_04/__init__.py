values_file = open('values.txt', 'r')
values = values_file.readlines()

card_count = 0
card_scores = []
tree_results = [None] * len(values)

for card in values:
    card_split = str.split(card, ':')
    numbers_split = str.split(card_split[1], '|')
    your_numbers = set(map(int, numbers_split[0].strip().split()))
    winning_numbers = set(map(int, numbers_split[1].strip().split()))

    matching_numbers = your_numbers.intersection(winning_numbers)
    matching_count = len(matching_numbers)
    card_scores.append(matching_count)


def process_card_tree(current_index: int):
    offset = 0
    result_card_count = 1
    while offset < card_scores[current_index]:
        offset += 1
        next_index = current_index + offset
        tree_result = tree_results[next_index]
        if tree_result is None:
            tree_result = process_card_tree(next_index)
            tree_results[next_index] = tree_result
        result_card_count += tree_result

    return result_card_count


index = 0
while index < len(card_scores):
    card_count += process_card_tree(index)
    index += 1

print(f'answer is {card_count}')
