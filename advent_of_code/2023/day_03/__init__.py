values_file = open('values.txt', 'r')
values = values_file.readlines()

parts_sum = 0


def find_number_start_x_y(x, y):
    offset = 0
    while values[y][x-offset].isdigit():
        offset += 1
    return x - (offset - 1), y


def get_number(position):
    x = position[0]
    y = position[1]
    offset = 0
    while values[y][x + offset].isdigit():
        offset += 1
    return int(values[y][x:x+offset:])


for y, line in enumerate(values):
    for x, char in enumerate(line.strip()):
        if char == '*':
            part_number_positions = set()
            if y > 0:
                if x > 0 and values[y-1][x-1].isdigit():
                    part_number_positions.add(find_number_start_x_y(x-1, y-1))
                if values[y-1][x].isdigit():
                    part_number_positions.add(find_number_start_x_y(x, y-1))
                if x != len(line) - 1 and values[y-1][x+1].isdigit():
                    part_number_positions.add(find_number_start_x_y(x+1, y-1))

            if x > 0 and values[y][x-1].isdigit():
                part_number_positions.add(find_number_start_x_y(x-1, y))
            if x != len(line) - 1 and values[y][x+1].isdigit():
                part_number_positions.add(find_number_start_x_y(x+1, y))

            if y != len(values) - 1:
                if x > 0 and values[y+1][x-1].isdigit():
                    part_number_positions.add(find_number_start_x_y(x-1, y+1))
                if values[y+1][x].isdigit():
                    part_number_positions.add(find_number_start_x_y(x, y+1))
                if x != len(line) - 1 and values[y+1][x+1].isdigit():
                    part_number_positions.add(find_number_start_x_y(x+1, y+1))

            if len(part_number_positions) == 2:
                parts_sum += (get_number(part_number_positions.pop()) * get_number(part_number_positions.pop()))

print(parts_sum)
