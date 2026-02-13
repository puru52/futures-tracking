import argparse
import sys
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol, validate_side, validate_order_type, 
    validate_quantity, validate_price
)
from bot.logging_config import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, help="Quantity to trade")
    parser.add_argument("--price", help="Price for LIMIT orders")

    args = parser.parse_args()

    try:
        # Validate inputs
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print(f"\n--- Order Request Summary ---")
        print(f"Symbol:   {symbol}")
        print(f"Side:     {side}")
        print(f"Type:     {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price:    {price}")
        print("-----------------------------\n")

        # Initialize client and manager
        client_wrapper = BinanceFuturesClient()
        order_manager = OrderManager(client_wrapper.get_client())

        # Place order
        response = order_manager.place_futures_order(symbol, side, order_type, quantity, price)

        # Print result
        formatted_res = order_manager.format_order_response(response)
        print("SUCCESS: Order placed successfully!")
        print(f"Order ID:     {formatted_res['orderId']}")
        print(f"Status:       {formatted_res['status']}")
        print(f"Executed Qty: {formatted_res['executedQty']}")
        print(f"Avg Price:    {formatted_res['avgPrice']}")
        print("Check 'trading_bot.log' for full details.\n")

    except ValueError as e:
        print(f"INPUT ERROR: {e}")
        logger.error(f"Input validation failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"FAILURE: {e}")
        # Error is already logged in orders.py
        sys.exit(1)

if __name__ == "__main__":
    main()
