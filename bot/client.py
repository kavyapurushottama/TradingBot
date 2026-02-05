import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()


class BinanceClient:
    def __init__(self):
        self.client = Client(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET"),
            testnet=True
        )

        # Futures Testnet endpoint
        # self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        self.client.API_URL = "https://testnet.binance.vision"

    def place_order(self, **kwargs):
        return self.client.create_order(**kwargs) # return self.client.futures_create_order(**kwargs)

