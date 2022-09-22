# Create your tests here.
from asyncore import write
from textwrap import indent
import requests #type: ignore
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
            self.j_str = json.load(file)


    def read(self):
        return self.j_str


a = Json_obj('order_cost/preference.json')
print(a.read())