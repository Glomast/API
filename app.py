import json
from flask import Flask, request, jsonify


app = Flask(__name__)
data = json.load(open('stock.json'))

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/api/v1/info', methods=['GET'])
def api_home():
    return jsonify(data)


@app.route('/api/v1/stocks', methods=['GET'])
def api_stocks():
    if 'symbol' in request.args:
        symbol = request.args['symbol']
    else:
        return "Error: No name field provided. Please specify a name."
        
    data_list = data['quotedata']

    for i in data_list:
        # sym = i["symbol"]

        if i['symbol'] == symbol:
            details = {
                "name": i["longname"],
                "datatype": i["datatype"],
                "exchange": i["exchange"],
                "price_data": i["pricedata"]
            }

    return jsonify(details)  


if __name__ == '__main__':
    app.run(debug=True)