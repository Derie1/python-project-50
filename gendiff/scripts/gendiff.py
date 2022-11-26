#!/usr/bin/env python3

import json
import yaml
import os
from gendiff.cli import parse
from gendiff.build_diff import generate_diff


def main():
    args = parse()
    data1 = get_data(args.first_file)
    data2 = get_data(args.second_file)
    print(generate_diff(data1, data2))


def get_data(path) -> dict:
    if os.path.splitext(path)[-1] == '.json':
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    elif os.path.splitext(path)[-1] in ('.yml', '.yaml'):
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
    else:
        data = {}
    return data


if __name__ == '__main__':
    main()
