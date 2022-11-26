import json


json1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}

json2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}


with open('./tests/fixtures/file1.json', 'w') as js1:
    json.dump(json1, js1)


with open('./tests/fixtures/file2.json', 'w') as js2:
    json.dump(json2, js2)