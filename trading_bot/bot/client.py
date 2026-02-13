import os
from binance.client import Client
from dotenv import load_dotenv
from .logging_config import logger

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv('BINANCE_API_KEY')
        api_secret = os.getenv('BINANCE_API_SECRET')
        
        if not api_key or not api_secret:
            logger.error("API Key or Secret missing in .env file")
            raise ValueError("API Key and Secret must be provided in .env")
            
        # Initialize client for Testnet
        self.client = Client(api_key, api_secret, testnet=True)
        logger.info("Binance Futures Testnet Client initialized")

    def get_client(self):
        return self.client
