# index.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from .electrum_client import ElectrumClient

app = Flask(__name__)

cors = CORS(app, resources={'/*': {'origins': ['http://localhost:3000',
            'https://tokenstork.com', 'https://tokenstork-git-002-panmoni.vercel.app']}})

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def home():
    return 'Hello, World! (vercel)'


@app.route('/token_price', methods=['GET'])
def token_price():
    category = request.args.get('category')
    decimals = request.args.get('decimals', type=int)
    if not category or decimals is None:
        return jsonify({'error': 'Category and decimals are required parameters'}), 400
    try:
        client = ElectrumClient()
        amount = 1 if decimals == 0 else 10 ** decimals
        response = client.call(
            "cauldron.contract.token_price", 2, category, amount)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/token_liquidity', methods=['GET'])
def token_liquidity():
    category = request.args.get('category')
    if not category:
        return jsonify({'error': 'Category is required'}), 400
    client = ElectrumClient()
    response = client.call("cauldron.contract.token_value_locked", 2, category)
    if not response:
        return jsonify({'error': 'Failed to fetch data from Electrum server'}), 500
    return jsonify(response)
# if __name__ == '__main__':
#     app.run(debug=True)
