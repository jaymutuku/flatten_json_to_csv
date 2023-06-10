import json
import logging


import pandas as pd
import requests

from flatten_json import flatten

import pprint 
pp = pprint.PrettyPrinter(indent=4)

from mytoken import token


# dataframe from csv
df = pd.read_csv("delivery_codes.csv")

# store results of import
rows_list = []

# logging to a file in append mode
# logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

headers = {
"Authorization": "Bearer " + token,
"programId": "c0d4651a-5d9a-11e7-846e-06f77de3a7f0"
}

url = "http://api.xxxxx.xx/order/deliverynotes/search/code/"

json_file = 'delivery_code_data2.json'

# iterate and get data
for index, row in df.iterrows():

    searchTerm = str(row['delivery_code'])      
        
# NOTE:searchTerm is path variable

    response = requests.get(url+searchTerm,  headers=headers)
    # dict_list = response.json()['data']
    dict_list = response.json()
    print(type(dict_list))
    if response.status_code == 200:        
        rows_list.append(dict_list)
        pp.pprint(rows_list)
        with open(json_file,'w+') as outfile:
            json.dump(rows_list,outfile)
            outfile.close()
    elif response.status_code == 404:
        with open('file2.log','a') as f:
            # print("deliverycode - {} headers{} - response - {}".format(searchTerm, headers, response.text))
            print("deliverycode - {} response - {}".format(searchTerm, response.text),file=f)
        continue

    else:
        response.raise_for_status()

with open(json_file,'r') as inputfile:
    data = json.load(inputfile)
    print(type(data))

flattened = (flatten(d) for d in data)     
inputfile.close()

print(type(flattened))

dataset = pd.DataFrame(flattened)
    
print(dataset)    
    # export to csv
dataset.to_csv('delivery_code_data2.csv',index=False)
