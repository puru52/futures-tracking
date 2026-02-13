from .logging_config import logger
from binance.exceptions import BinanceAPIException, BinanceRequestException

class OrderManager:
    def __init__(self, binance_client):
        self.client = binance_client

    def place_futures_order(self, symbol, side, order_type, quantity, price=None):
        """Places a futures order on Binance Testnet."""
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
            }

            if order_type == 'LIMIT':
                params['price'] = price
                params['timeInForce'] = 'GTC'  # Good Til Cancelled is standard for limit orders

            logger.info(f"Placing {order_type} {side} order for {quantity} {symbol}")
            
            # Use futures_create_order from python-binance
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order placed successfully. Response: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message} (Code: {e.code})")
            raise Exception(f"API Error: {e.message}")
        except BinanceRequestException as e:
            logger.error(f"Binance Request Error: {e}")
            raise Exception(f"Network/Request Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise e

    def format_order_response(self, response):
        """Formats the API response for clear printing."""
        summary = {
            "orderId": response.get('orderId'),
            "status": response.get('status'),
            "executedQty": response.get('executedQty'),
            "avgPrice": response.get('avgPrice', 'N/A'),
            "symbol": response.get('symbol'),
            "side": response.get('side'),
            "type": response.get('type')
        }
        return summary
