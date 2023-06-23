# import pandas as pd
 
# data = pd.read_excel('rates.xlsx')
# data = data.values.tolist()
# # print(pd.isna(data[1][0]))
# dataset = []
# dictionry = {}
# countries = []
# rates=[]
# for country in data:
#   if pd.isna(country[1]) == False:
#     countries.append(country[1])
#   if pd.isna(country[-2]) == False:
#     rates.append({
#       "weight":country[-2],
#       "rate":country[-1],
#     })
#   if country[-2] == 70.5:
#     dictionry["country"] = countries
#     dictionry["rates"] = rates
#     dataset.append(dictionry)
#     dictionry = {}
#     countries = []
#     rates = []
   
   
import json 
# with open('rates.json', 'w') as outfile:
#   json.dump(dataset, outfile)

with open("rates.json", "r") as read_file:
  with open('countries.json',"w") as json_file:
    data = json.load(read_file)
    for country in data:
      for county in country["country"]:
        json_file.write(county+",")