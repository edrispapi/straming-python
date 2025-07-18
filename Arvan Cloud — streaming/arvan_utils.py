"""Arvan Cloud helper functions for VOD/live streaming"""
import requests

def generate_stream_url(channel_id, token):
    """دریافت URL پخش زنده از Arvan Cloud API"""
    url = f"https://napi.arvancloud.com/live/{channel_id}/stream"
    headers = {"Authorization": f"Apikey {token}"}
    resp = requests.get(url, headers=headers)
    return resp.json().get("stream_url")
