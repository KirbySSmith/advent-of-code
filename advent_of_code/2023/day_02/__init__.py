values_file = open('values.txt', 'r')
values = values_file.readlines()

game_power_sum = 0
for game in values:
    max_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    game_split = str.split(game, ':')
    game_number = game_split[0][5::]
    hand_split = str.split(game_split[1], ';')
    for hand in hand_split:
        cubes_split = str.split(hand, ',')
        for cubes in cubes_split:
            count_color = str.split(str.strip(cubes), " ")
            count = int(count_color[0])
            color = count_color[1]
            if max_cubes[color] < count:
                max_cubes[color] = count
    game_power = max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]
    game_power_sum += game_power

print(f'answer is {game_power_sum}')
