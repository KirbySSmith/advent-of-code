values_file = open('values.txt', 'r')
values = values_file.readlines()

seeds = []
maps = []
seed_to_soil_map = {}

map_load_index = 0
for index, line in enumerate(values):
    if index == 0:
        seeds_split = str.split(line, ':')
        seeds = list(map(int, seeds_split[1].strip().split()))
    elif len(line.strip()) > 0:
        if line[0].isdigit():
            if len(maps) <= map_load_index:
                maps.append([])
            maps[map_load_index].append(list(map(int, line.strip().split())))
        elif len(maps) != 0:
            map_load_index += 1


def source_to_destination(seed_maps, source_value):
    for map_entry in seed_maps:
        destination_range_start = map_entry[0]
        source_range_start = map_entry[1]
        range_length = map_entry[2]
        if source_range_start <= source_value < (source_range_start + range_length):
            offset = source_value - source_range_start
            return destination_range_start + offset
    return source_value


def seed_to_soil(seed):
    current_value = seed
    for seed_maps in maps:
        current_value = source_to_destination(seed_maps, current_value)
    return current_value


for seed in seeds:
    seed_to_soil_map[seed] = seed_to_soil(seed)

min_location = min(seed_to_soil_map.values())

print(f'{min_location}')

