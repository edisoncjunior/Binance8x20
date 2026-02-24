# Binance Futures MM8 x MM20 - Hedge Mode

Bot que:

- Opera XRPUSDT
- Timeframe 5m
- Cruzamento MM8 abaixo da MM20
- Envia ordem LIMIT SHORT no preço da MM20
- Alavancagem 10x
- Valor fixo 1 USD
- Hedge Mode habilitado
- Margem Cross

## Instalação

pip install -r requirements.txt

## Configurar

Copiar .env.example para .env e inserir suas chaves.

## Executar

python main.py
