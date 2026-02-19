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
def get_open_positions(client, symbol=None):
    """
    Fetch open futures positions.
    If symbol is provided, filter by symbol.
    """
    try:
        positions = client.client.futures_position_information()

        open_positions = []

        for position in positions:
            position_amt = float(position["positionAmt"])

            if position_amt != 0:
                if symbol is None or position["symbol"] == symbol:
                    open_positions.append(position)

        return open_positions

    except Exception as e:
        raise Exception(f"Error fetching positions: {e}")
    

def get_account_balance(client):
    account_info = client.client.futures_account()
    
    balances = account_info.get("assets", [])
    
    usdt_balance = next(
        (asset for asset in balances if asset["asset"] == "USDT"),
        None
    )

    if not usdt_balance:
        print("USDT balance not found.")
        return

    print("\nAccount Balance")
    print("----------------------------")
    print(f"Wallet Balance: {float(usdt_balance['walletBalance']):.4f}")
    print(f"Unrealized PnL: {float(usdt_balance['unrealizedProfit']):.4f}")
    print("----------------------------")


def close_position(client, symbol):
    positions = client.client.futures_position_information(symbol=symbol)

    position = next(
        (p for p in positions if float(p["positionAmt"]) != 0),
        None
    )

    if not position:
        print(f"No open position found for {symbol}")
        return

    position_amt = float(position["positionAmt"])

    side = "SELL" if position_amt > 0 else "BUY"
    quantity = abs(position_amt)

    print("\nClosing Position")
    print("----------------------------")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Quantity: {quantity}")
    print("----------------------------")

    order = client.client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity,
        reduceOnly=True
    )

    print("Position closed successfully.")
    return order


