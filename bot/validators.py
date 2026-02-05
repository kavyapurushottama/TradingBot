def validate_symbol(symbol: str) -> str:
    if not symbol:
        raise ValueError("Symbol cannot be empty")
    if not symbol.isalnum():
        raise ValueError("Symbol must be alphanumeric (e.g., BTCUSDT)")
    return symbol.upper()


def validate_side(side: str) -> str:
    if side not in ("BUY", "SELL"):
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    return quantity
