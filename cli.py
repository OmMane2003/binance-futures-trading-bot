import argparse
import logging

from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="Order side (BUY or SELL)")
    parser.add_argument("--type", required=True, help="Order type (MARKET or LIMIT)")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    # ✅ Defensive uppercasing (professional touch)
    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    quantity = args.quantity
    price = args.price

    try:
        # ----------------------------
        # Validation
        # ----------------------------
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        logging.info(f"Order summary: {symbol} {side} {order_type} {quantity} {price}")

        # ----------------------------
        # Create Client
        # ----------------------------
        client = BinanceFuturesClient()

        # ----------------------------
        # Place Order
        # ----------------------------
        response = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price,
        )

        # ----------------------------
        # Output
        # ----------------------------
        print("\nOrder Summary")
        print("---------------------------")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        print("\nResponse:")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
