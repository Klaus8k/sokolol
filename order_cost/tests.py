# Create your tests here.
import requests
import json


with open('preference.json', 'r') as file:
    print(json.loads(file.read()), sep='4')

