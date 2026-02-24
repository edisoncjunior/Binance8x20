import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")

SYMBOL = "XRPUSDT"
TIMEFRAME = "5m"
LEVERAGE = 10
USD_VALUE = 1  # valor da operação
