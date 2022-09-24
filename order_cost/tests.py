import json


class Json_obj():
    def __init__(self, file_json) -> None:
        self.file_json = file_json
        
    def read(self):
        with open(self.file_json, 'r') as file:
            cost = json.load(file)
            return cost  # type: dict

    def write(self, data, order_type):
        cost = self.read()
        if order_type in cost.keys():
            cost[order_type].update(data)
        
        with open(self.file_json, 'w') as file:
            json.dump(cost, file, indent=4)

            

                
