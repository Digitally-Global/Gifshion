import json

def getRate(country,weight):
  with open('./app/rates.json') as json_file:
    data = json.load(json_file)
  for item in data:
    if country in item["country"]:
      for rate in item['rates']:
        if weight <= rate['weight']:
          return rate['rate']

if __name__ == "__main__":
  print(getRate('22222',39.0))