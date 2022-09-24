import json


class Json_obj():
    def __init__(self, file_json) -> None:
        self.file_json = file_json
        

    def read(self):
        with open(self.file_json, 'r') as file:
            return json.load(file)  # type: dict

    def search(self, search_key):
        if search_key in self.j_str.keys():
            return [search_key, self.j_str[search_key]]
        else:
            return 'Неверный ключ'

    # Здесь проверку содержания и запись обновленных значений
    def write(self, data):
        if data:
            with open(self.file_json, 'w') as file:
                result = json.dump(data, file)

            

                
