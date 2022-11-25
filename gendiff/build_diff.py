from typing import Any, Union


def generate_diff(data1: dict, data2: dict) -> str:
    """Function that compares two configuration
    files and shows a difference."""
    brackets = '{}'
    prefix_1 = '  - '
    prefix_2 = '  + '
    prefix_12 = '    '
    result = f'{brackets[0]}\n'
    keys = sorted(list(set(data1.keys()) | set(data2.keys())))
    for item in keys:
        if item in data1 and item in data2:
            if data1[item] == data2[item]:
                result += prefix_12 + f"{item}: {to_str(data1[item])}\n"
            else:
                result += prefix_1 + f"{item}: {to_str(data1[item])}\n"
                result += prefix_2 + f"{item}: {to_str(data2[item])}\n"
        elif item in data1 and item not in data2:
            result += prefix_1 + f"{item}: {to_str(data1[item])}\n"
        elif item not in data1 and item in data2:
            result += prefix_2 + f"{item}: {to_str(data2[item])}\n"
    result += brackets[1]
    return result


def to_str(value: Any) -> [Union[str, int]]:
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int):
        return value
    return f"{value}"
