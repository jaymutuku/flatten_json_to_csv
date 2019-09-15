import json
import time

import pandas as pd
import requests

# from flatsplode import flatsplode
from flatten_json import flatten

from mytoken import token

# dataframe from csv
df = pd.read_csv('test_ids.csv',dtype=str)

# store results of import
rows_list = []

headers = {"Authorization": "Bearer " + token}
url = "https://test-gateway.tulaa.io/cogency-service/credit-info"

# iterate and get data
for index, row in df.iterrows():
    userdata = {
        "identityNumber": row["identity_number"],
        "loanAmount": 6000,
        "reason": 1,
    }

    response = requests.get(url, data=json.dumps(userdata), headers=headers)

    if response.status_code == 200:
        json_data = rows_list.append(rows_list)
    else:
        response.raise_for_status()

    print(type(json_data))

    # flatten response
    flattened = (flatten(d) for d in json_data)
    # flattened = pd.DataFrame(list(flatsplode(json_data)))

    user_df = pd.DataFrame(flattened)
    print(user_df)

    # export to csv
    user_df.to_csv(str(time.time()) + "metropol_test_data.csv")
