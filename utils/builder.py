import csv
import json
from collections import OrderedDict

input_file_path = "../data/input.csv"
output_file_path = "../docs/data.json"


def parse_tags():
    """ parse tag field from input csv"""
    pass

def serialize_data(file_path: str) -> str:
    """ read in csv, return as json"""

    data = {}
    with open(file_path, mode="r") as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            brand = row['brand']
            data[brand] = {
                'brand_url': row['brand_url'],
                'gi_url': row['gi_url'],
                'rashguard_url': row['rashguard_url'],
                'shorts_url': row['shorts_url'],
                'belt_url': row['belt_url']
            }
    ordered_data = OrderedDict(sorted(data.items()))
    return json.dumps(ordered_data)

def write_data(file_path: str, data: str) -> None:
    """ read in json, write to file"""

    with open(file_path, mode='w') as output_file:
        output_file.write(data)
    return

data = serialize_data(input_file_path)
write_data(output_file_path, data)