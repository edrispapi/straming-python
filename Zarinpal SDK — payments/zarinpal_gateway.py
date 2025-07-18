"""Zarinpal helper for payment transactions"""
import requests

def request_payment(amount, description, callback_url, merchant_id):
    url = "https://api.zarinpal.com/pg/v4/payment/request.json"
    data = {
        "merchant_id": merchant_id,
        "amount": amount,
        "callback_url": callback_url,
        "description": description
    }
    response = requests.post(url, json=data)
    return response.json()
