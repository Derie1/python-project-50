#!/usr/bin/env python3

import json
from gendiff.cli import parse


def build_diff(data1: dict, data2: dict) -> str:
    """Function that compares two configuration 
    files and shows a difference."""
    brackets = '{}'
    prefix_1 = '  - '
    prefix_2 = '  + '
    prefix_12 = '    '
    result = f'gendiff {json1} {json2}\n{brackets[0]}\n'
    keys = sorted(list(set(data1.keys()) | set(data2.keys())))
    for item in keys:
        if item in data1 and item in data2:
            if data1[item] == data2[item]:
                result += prefix_12 + f"{item}: {data1[item]}\n"
            else:
                result += prefix_1 + f"{item}: {data1[item]}\n"
                result += prefix_2 + f"{item}: {data2[item]}\n"
        elif item in data1 and item not in data2:
            result += prefix_1 + f"{item}: {data1[item]}\n"
        elif item not in data1 and item in data2:
            result += prefix_2 + f"{item}: {data2[item]}\n"
    result += brackets[1]
    return result


if __name__ == '__main__':
    args = parse()
    json1 = args.first_file
    json2 = args.second_file

    with open(json1) as js1:
        json_data1 = json.load(js1)

    with open(json2) as js2:
        json_data2 = json.load(js2)
        
    print(build_diff(json_data1, json_data2))