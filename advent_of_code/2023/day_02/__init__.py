values_file = open('values.txt', 'r')
values = values_file.readlines()

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


game_number_sum = 0
for game in values:
    game_split = str.split(game, ':')
    game_number = game_split[0][5::]
    hand_split = str.split(game_split[1], ';')
    valid_game = True
    for hand in hand_split:
        if valid_game is True:
            cubes_split = str.split(hand, ',')
            for cubes in cubes_split:
                count_color = str.split(str.strip(cubes), " ")
                count = count_color[0]
                color = count_color[1]
                if max_cubes[color] < int(count):
                    valid_game = False
                    break
    if valid_game is True:
        game_number_sum += int(game_number)

print(f'answer is {game_number_sum}')
