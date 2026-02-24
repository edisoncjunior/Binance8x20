import pandas as pd
from binance_client import client
from config import SYMBOL, TIMEFRAME, USD_VALUE

def obter_klines(limit=100):
    klines = client.futures_klines(
        symbol=SYMBOL,
        interval=TIMEFRAME,
        limit=limit
    )
    df = pd.DataFrame(klines, columns=[
        "open_time","open","high","low","close","volume",
        "close_time","qav","num_trades",
        "taker_base","taker_quote","ignore"
    ])
    df["close"] = df["close"].astype(float)
    return df

def calcular_medias(df):
    df["mm8"] = df["close"].rolling(8).mean()
    df["mm20"] = df["close"].rolling(20).mean()
    return df

def cruzamento_baixa(df):
    if len(df) < 21:
        return False
    
    mm8_anterior = df["mm8"].iloc[-2]
    mm20_anterior = df["mm20"].iloc[-2]
    mm8_atual = df["mm8"].iloc[-1]
    mm20_atual = df["mm20"].iloc[-1]

    # cruzamento para baixo
    if mm8_anterior > mm20_anterior and mm8_atual < mm20_atual:
        return True
    
    return False

def calcular_quantidade(preco):
    return round(USD_VALUE / preco, 1)
