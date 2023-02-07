import json
from .models import Solvent_model
import datetime


class Json_obj():
    """Class for work with order settings"""

    def __init__(self, file_json) -> None:
        self.file_json = file_json

    def read(self):
        with open(self.file_json, 'r') as file:
            cost = json.load(file)
            return cost  # type: dict

    def write(self, data, order_type):
        cost = self.read()
        if None not in data.values():
            cost[order_type].update(data)

        with open(self.file_json, 'w') as file:
            json.dump(cost, file, indent=4)


# Calculation order solvent print
def calc_solvent(order_info: dict, cost):
    square = order_info['width'] * order_info['higth']
    result = square * cost.read()['solvent'][order_info['material']]
    return round(result, 2)


def solvent_check_and_save_or_return(order_info):

    cost_per_m2 = Solvent_model.objects.filter(type=order_info['type']).order_by('-date')[0].cost 
    # x = cost_per_m2.order_by('-date')[0].cost # order by latest (-reverse order)
    return cost_per_m2 * order_info['width'] * order_info['higth']

# https://django.fun/ru/docs/django/4.1/topics/db/queries/ - !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def save_to_db(set_new_cost):
    new_cost = Solvent_model(type=set_new_cost['type'],
                             cost=set_new_cost['cost'])
    new_cost.save()
