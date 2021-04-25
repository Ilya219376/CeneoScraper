import requests

respons = requests.get("https://www.ceneo.pl/88072703#tab=reviews")

print(respons.status_code)