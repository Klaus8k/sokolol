import requests

url = "http://79.133.181.123/"
host = 'www.sokolol.ru'
r = requests.get(url, headers={'host': host})

print(r.status_code)
print(r.text)