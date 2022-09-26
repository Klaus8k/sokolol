import json


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
    return result


            

                
