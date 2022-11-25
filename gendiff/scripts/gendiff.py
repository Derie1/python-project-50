#!/usr/bin/env python3

import json
from gendiff.cli import parse
from gendiff.build_diff import generate_diff


def main():
    args = parse()
    with open(args.first_file, encoding='utf-8') as f1:
        json1 = json.load(f1)
    with open(args.second_file, encoding='utf-8') as f2:
        json2 = json.load(f2)
    print(generate_diff(json1, json2))


if __name__ == '__main__':
    main()
