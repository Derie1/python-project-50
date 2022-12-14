import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    # Positional args
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # Optional args
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()
