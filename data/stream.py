import requests

def get_market_data():
    # Mock data for now — replace with Birdeye/Jupiter
    return {
        "token": "BONK", 
        "price_usd": 0.000028,
        "change_5m": 1.8,  # 180%
        "volume_5m": 1200000
    }
