from .logging_config import logger

def validate_symbol(symbol: str):
    if not symbol or not symbol.endswith('USDT'):
        raise ValueError(f"Invalid symbol: {symbol}. Must be a USDT-M futures symbol (e.g. BTCUSDT)")
    return symbol.upper()

def validate_side(side: str):
    side = side.upper()
    if side not in ['BUY', 'SELL']:
        raise ValueError(f"Invalid side: {side}. Must be BUY or SELL")
    return side

def validate_order_type(order_type: str):
    order_type = order_type.upper()
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError(f"Invalid order type: {order_type}. Must be MARKET or LIMIT")
    return order_type

def validate_quantity(quantity: str):
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be greater than zero")
        return qty
    except ValueError:
        raise ValueError(f"Invalid quantity: {quantity}. Must be a number")

def validate_price(price: str, order_type: str):
    if order_type == 'LIMIT':
        if not price:
            raise ValueError("Price is required for LIMIT orders")
        try:
            p = float(price)
            if p <= 0:
                raise ValueError("Price must be greater than zero")
            return p
        except ValueError:
            raise ValueError(f"Invalid price: {price}. Must be a number")
    return None
