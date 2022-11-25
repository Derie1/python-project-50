
import json
from gendiff.build_diff import generate_diff

with open('./tests/fixtures/correct_result.txt', encoding='utf-8') as r:
    result = r.read()

with open('./tests/fixtures/file1.json', encoding='utf-8') as f1:
    json1 = json.load(f1)

with open('./tests/fixtures/file2.json', encoding='utf-8') as f2:
    json2 = json.load(f2)


def test_gendiff():
    assert generate_diff(json1, json2) == result
