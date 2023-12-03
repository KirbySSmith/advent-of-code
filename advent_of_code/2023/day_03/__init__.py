values_file = open('values.txt', 'r')
values = values_file.readlines()

parts_sum = 0
part_number_positions = set()


def find_number_start_x_y(x, y):
    offset = 0
    while values[y][x-offset].isdigit():
        offset += 1
    return x - (offset - 1), y


for y, line in enumerate(values):
    for x, char in enumerate(line.strip()):
        if not char.isdigit() and char != '.':
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

for x, y in part_number_positions:
    offset = 0
    while values[y][x + offset].isdigit():
        offset += 1
    parts_sum += int(values[y][x:x+offset:])
print(parts_sum)
