#!/usr/bin/env python3

import json
from gendiff.cli import parse


args = parse()
json1 = args.first_file
json2 = args.second_file


with open(json1) as js1:
    json_data1 = json.load(js1)

with open(json2) as js2:
    json_data2 = json.load(js2)

def build_diff(json_data1: dict, json_data2: dict):
    sorted_keys_1 = sorted([*json_data1])
    sorted_keys_2 = sorted([*json_data2])

    return sorted_keys_1, sorted_keys_2

print(build_diff(json_data1, json_data2))