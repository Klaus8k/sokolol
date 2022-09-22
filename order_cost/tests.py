# Create your tests here.
# import requests  # type: ignore
from http import server
import json
import os

print(os.getcwd())


def read_json():
    with open('order_cost/preference.json', 'r') as file:
        fileStr = file.read()
        jsonString = json.loads(fileStr)
    return jsonString


def write_json():
    with open('order_cost/preference.json', 'r') as file:
        filestr = read_json()
        for i in filestr.values():
            if 'GlossDiv' in i.keys():
                print(i['GlossDiv'])

# write_json()


# JSON class work

class Json_obj():
    def __init__(self, file_json) -> None:
        self.file_json = file_json
        with open(self.file_json, 'r') as file:
            self.j_str = json.load(file)  # type: dict

    def read(self):
        return self.j_str

    def search(self, search_key):

        if search_key in self.j_str.keys():
            return [search_key, self.j_str[search_key]]
        else:
            return 'Неверный ключ'

    # check and update json file object
    def write(data):
        pass


a = Json_obj('order_cost/preference.json')
print(a.read())
print(a.search('banner'))
