import json
from .models import Solvent_model, Solvent_orders

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
    cost_per_m2 = Solvent_model.objects.get(type=order_info['type']).cost
    square = order_info['width'] * order_info['higth']


    # check in db have order_info in db
    # if have return cost newest
    # if no calc_solvent and save all in db and return cost
    return square * cost_per_m2

def check_order_params_db(order_info: dict):
    pass

# def save_to_db(order_info): -------------> Здесь сохраняем заказы в базу
#     new_cost = Solvent_orders(type=order_info['type'],
#                                 width = order_info['width'],
#                                 higth = order_info['higth'],
#                                 cost_this = solvent_check_and_save_or_return(order_info))
#     new_cost.save()
#     return new_cost

def save_to_db(set_new_cost):
    new_cost = Solvent_model(type=set_new_cost['type'],
                                cost=set_new_cost['cost'])
    new_cost.save()
    return 0