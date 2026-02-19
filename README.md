# Binance Futures Testnet CLI Trading Bot
Backend-focused CLI trading system built in Python with modular architecture and lifecycle position management for Binance Futures Testnet.

This project demonstrates clean backend architecture, API integration, lifecycle management of trading positions, and secure environment configuration.

---

## 🚀 Features

- Place MARKET and LIMIT futures orders
- View open positions
- View account balance (wallet + unrealized PnL)
- Close positions safely using `reduceOnly`
- Environment-based API key management
- Clean modular architecture with separation of concerns

---

## 🧰 Tech Stack

- Python
- python-binance
- python-dotenv
- argparse
- Logging module

---

## 🧱 Project Structure

```
trading-bot/
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── cli.py
├── requirements.txt
└── README.md
```



The project separates:

- API connection layer  
- Business logic (orders & account operations)  
- CLI interaction layer  

This mirrors real-world backend system design principles.

---

## ⚙️ Setup

### 1. Clone the repository

git clone https://github.com/OmMane2003/binance-futures-trading-bot.git
cd binance-futures-trading-bot

### 2. Install dependencies

pip install -r requirements.txt


### 3. Create `.env` file

BINANCE_API_KEY=your_testnet_key
BINANCE_SECRET_KEY=your_testnet_secret



This project uses Binance Futures **Testnet** for safe experimentation.

---

## 🖥 Usage

### Place Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Place Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000

### View Open Positions

python cli.py --positions

### View Account Balance

python cli.py --balance

### Close Position

python cli.py --close BTCUSDT


---

## 🛡 Why Testnet?

All operations are executed on Binance Futures Testnet to:

- Avoid real capital risk
- Safely test trading lifecycle logic
- Simulate real derivatives trading behavior

---

## 🧠 Engineering Focus

This project was built to demonstrate:

- Clean modular backend design
- Secure environment configuration
- REST API interaction
- Futures trading lifecycle management
- Structured CLI design
- Clear output formatting and error handling

---

## 🔮 Future Improvements

- Enhanced logging & monitoring
- Docker containerization
- Cloud deployment
- Strategy module integration


