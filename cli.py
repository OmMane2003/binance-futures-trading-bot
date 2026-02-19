import argparse
from bot.client import BinanceFuturesClient
from bot.orders import place_order, get_open_positions, get_account_balance, close_position




def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", type=str, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", type=str, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", type=str, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit price (required for LIMIT orders)")

    parser.add_argument(
        "--positions",
        action="store_true",
        help="Check open positions"
    )

    parser.add_argument(
    "--balance",
    action="store_true",
    help="View account balance"
    )

    parser.add_argument(
    "--close",
    type=str,
    help="Close position for given symbol (e.g. BTCUSDT)"
)



    args = parser.parse_args()

    client = BinanceFuturesClient()

    try:
        # ------------------------------------
        # CHECKS OPEN POSITIONS
        # ------------------------------------


        if args.balance:
             get_account_balance(client)
             return
        
        if args.close:
            close_position(client, args.close)
            return


        if args.positions:
            positions = get_open_positions(client, args.symbol)

            if not positions:
                print("\nNo open positions.")
                return

            print("\nOpen Positions")
            print("-" * 40)

            for pos in positions:
                print(f"Symbol: {pos['symbol']}")
                print(f"Position Amt: {pos['positionAmt']}")
                print(f"Entry Price: {float(pos['entryPrice']):.2f}")
                print(f"Unrealized PnL: {float(pos['unRealizedProfit']):.4f}")
                print("-" * 40)

            return

        # ------------------------------------
        # PLACE ORDER
        # ------------------------------------
        if not all([args.symbol, args.side, args.type, args.quantity]):
            print("Error: Missing required order arguments.")
            return

        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\nOrder Summary")
        print("-" * 40)
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

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
