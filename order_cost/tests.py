# Create your tests here.
import requests #type: ignore
import json
import os

print(os.getcwd())


with open('order_cost/preference.json', 'r') as file:
    jsonString = json.load(file)
    
    print(jsonString)
