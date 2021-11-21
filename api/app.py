#!/usr/bin/env python
# encoding: utf-8
import requests
from flask import Flask, make_response, jsonify, abort
app = Flask(__name__)

supported_currencies = ['USD', 'EUR', 'UAH', 'CAD',  'GBP', 'HRK', 'JPY', 'THB', 'CHF', 'SGD', 'PLN', 'AUD', 'RON', 'SEK', 'IDR', 'INR']


@app.route('/')
def index():
    return jsonify({'Description': 'Demo Coinbase Cryptocurrency Simple API'})


# get list of all supported currencies
@app.route('/currency', methods=['GET'])
def get_currency_list():
    currency_list = []
    r = requests.get("https://api.coinbase.com/v2/exchange-rates")
    data = dict(r.json()["data"]["rates"])
    for key in data.keys():
        currency_list.append(key)
    return jsonify({"supported currencies": currency_list})


# Get price for a particular currency
@app.route('/currency/<string:currency_id>', methods=['GET'])
def get_currency(currency_id):
    if currency_id not in supported_currencies:
        abort(404)  # 404 Not Found
    r = requests.get(
        f"https://api.coinbase.com/v2/prices/spot?currency={currency_id}"
    )
    data = r.json()
    return data


# Health endpoint
@app.route('/health', methods=['GET'])
def get_app_state():
    return {"status": "I'm healthy and wealthy"}


# Error handling function
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Invalid currency ID, please find the correct in  "/currency" endpoint'}), 404)


if __name__ == '__main__':
    app.run(debug=True)