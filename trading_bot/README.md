# Binance Futures Testnet Trading Bot

A small Python application to place orders on Binance Futures Testnet (USDT-M) with proper logging and structured code.

## Setup

1. **Clone the repository** 
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure API Keys**:
   - Add your Binance Futures Testnet API Key and Secret to the `.env` file.

## Usage

Run the bot via the CLI:

### Place a MARKET Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a LIMIT Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000
```

## Project Structure
- `bot/client.py`: Binance API client wrapper.
- `bot/orders.py`: Order placement logic and response formatting.
- `bot/validators.py`: Input validation logic.
- `bot/logging_config.py`: Centralized logging configuration.
- `cli.py`: Command-line interface entry point.

## Error Handling
- Validates all user inputs before making API requests.
- Catches Binance API errors and network failures.
- Logs all requests, responses, and errors to `trading_bot.log`.

