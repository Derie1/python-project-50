
import json
import yaml
from gendiff.build_diff import generate_diff




def test_gendiff_json():
    with open('./tests/fixtures/correct_result.txt', encoding='utf-8') as r:
        result = r.read()
    with open('./tests/fixtures/file1.json', encoding='utf-8') as f1:
        json1 = json.load(f1)
    with open('./tests/fixtures/file2.json', encoding='utf-8') as f2:
        json2 = json.load(f2)

    assert generate_diff(json1, json2) == result


def test_gendiff_yaml():
    with open('./tests/fixtures/correct_result.txt', encoding='utf-8') as r:
        result = r.read()
    with open('./tests/fixtures/file1.yaml', 'r') as stream1:
        yaml1 = yaml.safe_load(stream1)
    with open('./tests/fixtures/file2.yaml', 'r') as stream2:
        yaml2 = yaml.safe_load(stream2)

    assert generate_diff(yaml1, yaml2) == result