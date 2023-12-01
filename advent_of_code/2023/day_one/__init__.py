import re

number_as_string_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def get_regex(reverse: bool):
    # Part 1 regex
    # return r"(\d)"
    regex_str = r"(\d"
    for str_key in number_as_string_map.keys():
        if reverse:
            regex_str += "|" + str_key[::-1]
        else:
            regex_str += "|" + str_key
    return regex_str + ")"


def convert_to_number(str_input: str, reverse: bool):
    for str_key, str_value in number_as_string_map.items():
        if reverse and str_input == str_key[::-1]:
            return number_as_string_map.get(str_key)
        if str_input == str_key:
            return number_as_string_map.get(str_key)
    return str_input


values_file = open('values.txt', 'r')
values = values_file.readlines()

value_sum = 0
for value in values:
    match = re.search(get_regex(False), value)
    first_digit = convert_to_number(match.group(1), False)

    last_match = re.search(get_regex(True), value[::-1])
    last_digit = convert_to_number(last_match.group(1), True)

    value_sum += int(first_digit + last_digit)
print(value_sum)
