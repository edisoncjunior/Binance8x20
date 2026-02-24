import time
from binance_client import configurar_conta, enviar_ordem_limit_short
from strategy import obter_klines, calcular_medias, cruzamento_baixa, calcular_quantidade
from config import SYMBOL

def main():
    configurar_conta()
    print("Bot iniciado...")

    while True:
        try:
            df = obter_klines()
            df = calcular_medias(df)

            if cruzamento_baixa(df):
                preco_mm20 = df["mm20"].iloc[-1]
                quantidade = calcular_quantidade(preco_mm20)

                print(f"Sinal detectado. Enviando SHORT LIMIT em {preco_mm20}")
                enviar_ordem_limit_short(preco_mm20, quantidade)

            time.sleep(60)

        except Exception as e:
            print("Erro:", e)
            time.sleep(10)

if __name__ == "__main__":
    main()
