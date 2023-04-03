import json

import jsonschema


def validate(json_path: str, schema_path: str):
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)

    with open(schema_path, 'r') as path_file:
        schema_data = json.load(path_file)

    jsonschema.validate(json_data, schema_data)


if __name__ == '__main__':
    try:
        validate('file.json', 'schema.json')
        print("Valid JSON")

    except Exception as e:
        print("Invalid JSON")
        print(e)
