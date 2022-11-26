import yaml


yaml1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}

yaml2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}

# with open('data.yml', 'w') as outfile:
#     yaml.dump(data, outfile, default_flow_style=False)

with open('./tests/fixtures/file1.yaml', 'w', encoding='utf8') as f1:
    yaml.dump(yaml1, f1, default_flow_style=False, allow_unicode=True)

with open('./tests/fixtures/file2.yaml', 'w', encoding='utf8') as f2:
    yaml.dump(yaml2, f2, default_flow_style=False, allow_unicode=True)

with open('./tests/fixtures/file1.yaml', 'r') as stream1:
    print(yaml.safe_load(stream1))

with open('./tests/fixtures/file2.yaml', 'r') as stream2:
    print(yaml.safe_load(stream2))

