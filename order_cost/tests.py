import json


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
    def write(self, data):
        if data:
            with open(self.file_json, 'w') as file:
                result = json.dump(data, file)

                
