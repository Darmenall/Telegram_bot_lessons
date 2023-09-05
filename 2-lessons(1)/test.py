import requests
from pprint import pprint as print
from tokens import API_VALYUTA

url = f"https://v6.exchangerate-api.com/v6/{API_VALYUTA}/pair/USD/UZS"

response = requests.get(url)
print(response.status_code)  # 200-duris, 404,403-naduris
# print(response.text)   #tusiniksiz

print(response.json())   # dic korinisinde keldi
print(response.json()['conversion_rate'])  # kerek cenani aliw

kurs = response.json()['conversion_rate']
print(f"bugingi kurs: 1 AQSh dollari {kurs} so'm")
som = int(input("neshe dollar?: "))
print(f"{som} dollar: {kurs*som} so'm boladi")


