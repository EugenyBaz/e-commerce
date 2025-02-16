import json


def read_data_json():
    prod_list_json = "data/products.json"
    with open(prod_list_json, "r", encoding="UTF-8") as file:
        data = json.load(file)

    return data
