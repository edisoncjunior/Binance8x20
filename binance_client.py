from binance.client import Client
from config import API_KEY, API_SECRET, LEVERAGE, SYMBOL

client = Client(API_KEY, API_SECRET)

def configurar_conta():
    # Ativar Hedge Mode
#    client.futures_change_position_mode(dualSidePosition=True)

    # Definir alavancagem
    client.futures_change_leverage(
        symbol=SYMBOL,
        leverage=LEVERAGE
    )

def obter_preco_atual():
    ticker = client.futures_symbol_ticker(symbol=SYMBOL)
    return float(ticker["price"])

def enviar_ordem_limit_short(price, quantity):
    return client.futures_create_order(
        symbol=SYMBOL,
        side="SELL",
        positionSide="SHORT",  # HEDGE MODE
        type="LIMIT",
        quantity=quantity,
        price=str(price),
        timeInForce="GTC"
    )
