import json

import pandas as pd
import requests

from flatten_json import flatten
from pandas.io.json import json_normalize

import pprint 
pp = pprint.PrettyPrinter(indent=4)

from mytoken import token

# dataframe from csv
df = pd.read_csv("test_ids.csv")

# store results of import
rows_list = []

headers = {"Authorization": "Bearer " + token}
url = "https://test-gateway.tulaa.io/cogency-service/credit-info/"

json_file = 'metropol_test_data.json'

# iterate and get data
for index, row in df.iterrows():

    payload = {
        "identityNumber": str(row['identity_number']),
        "loanAmount": 6000,
        "reason": 1,
    }

    response = requests.get(url, params=payload, headers=headers)
    dict_list = response.json()['data']
    print(type(dict_list))
    if response.status_code == 200:        
        rows_list.append(dict_list)
        pp.pprint(rows_list)
        with open(json_file,'w+') as outfile:
            json.dump(rows_list,outfile)
            outfile.close()
    else:
        response.raise_for_status()

inputFile = open(json_file)
print(type(inputFile))

data = json.load(inputFile)
print(type(data))

flattened = (flatten(d) for d in data)     
inputFile.close()

print(type(flattened))

dataset = pd.DataFrame(flattened)
    
print(dataset)    
    # export to csv
dataset.to_csv('metropol_test_data.csv',index=False)
