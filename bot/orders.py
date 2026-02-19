import logging
from binance.exceptions import BinanceAPIException


def place_order(client, symbol, side, order_type, quantity, price=None):
    """
    Places a MARKET or LIMIT order on Binance Futures Testnet.
    Returns the updated order response.
    """

    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        # --------------------
        # MARKET ORDER
        # --------------------
        if order_type == "MARKET":
            response = client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        # --------------------
        # LIMIT ORDER
        # --------------------
        elif order_type == "LIMIT":
            response = client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Unsupported order type")

        logging.info(f"Initial order response: {response}")

        # --------------------
        # Fetch Updated Order (Important for MARKET orders)
        # --------------------
        order_id = response.get("orderId")

        updated_order = client.client.futures_get_order(
            symbol=symbol,
            orderId=order_id
        )

        logging.info(f"Updated order response: {updated_order}")

        return updated_order

    except BinanceAPIException as e:
        logging.error(f"API error: {e}")
        raise

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise
