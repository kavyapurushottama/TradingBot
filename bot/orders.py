from bot.client import BinanceClient
from bot.logger_config import get_logger
from binance.exceptions import BinanceAPIException

logger = get_logger("TRADING_BOT")
client = BinanceClient()


def place_trade(symbol, side, order_type, quantity, price=None):
    try:
        order_params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            order_params["price"] = price
            order_params["timeInForce"] = "GTC"

        logger.info(f"Placing order: {order_params}")

        response = client.place_order(**order_params)

        logger.info(
            f"Order placed | ID={response.get('orderId')} "
            f"Status={response.get('status')}"
        )

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error | {e.message}")
        raise

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise
