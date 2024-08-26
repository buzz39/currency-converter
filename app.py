import requests 
from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
@app.route('/currency/<currency_id>', methods=['GET'])
def get_currency(currency_id):
    try:
        response = requests.get('https://api.coinbase.com/v2/currencies', verify=False)
        data = response.json()
 
        for currency in data['data']:
            if currency['id'] == currency_id:
                return jsonify(currency)
 
        return jsonify({"error": "Currency not found"}), 404
 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
if __name__ == '__main__':
    app.run(debug=True)
