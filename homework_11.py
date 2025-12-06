import requests

country_name = input("Введіть назву країни англійською: ")

url = f"https://restcountries.com/v3.1/name/{country_name}"

response = requests.get(url)

data = response.json()

country = data[0]

official_name = country["name"]["official"]
capital = country.get("capital")[0]
flag = country.get("flag", "")
population = country.get("population")
population_formatted = f"{population:,}".replace(",", " ")
lat, lng = country["latlng"]

print("\n*** ІНФОРМАЦІЯ ПРО КРАЇНУ ***")
print(f"Офіційна назва: [{official_name}]")
print(f"Столиця: [{capital}]")
print(f"Прапор: {flag}")
print(f"Населення: [{population_formatted}]")
print(f"Географічне положення: [{official_name}] розташована приблизно на широті [{lat}] та довготі [{lng}].")


fact1 = requests.get("https://catfact.ninja/fact").json()["fact"]

fact2 = requests.get("https://zenquotes.io/api/random").json()[0]["q"]

print("\n ВИПАДКОВИЙ ФАКТ ДЛЯ РОЗВАГИ ")
print(fact1)
print(fact2)