import json


data = json.load(open('stock.json'))

# print(data)

data_list = data['quotedata']

for i in data_list:
    sym = i["symbol"]

    if "MSFT" in sym:
        details = {
            "name": i["longname"],
            "datatype": i["datatype"],
            "exchange": i["exchange"],
            "price_data": i["pricedata"]
        }

print(details)