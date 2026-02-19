import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_SECRET_KEY")

        self.client = Client(api_key, api_secret)

        # Set Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

