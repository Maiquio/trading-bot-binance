import time
import numpy as np
from binance.client import Client
from binance.enums import *
import os

# Configurações do bot
API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')
SYMBOL = 'BTCUSDT'  # Par de trading
LEVERAGE = 20  # Alavancagem máxima
RISK_PER_TRADE = 0.25  # 25% do capital disponível

# Inicializa cliente da Binance
client = Client(API_KEY, API_SECRET)
client.futures_change_leverage(symbol=SYMBOL, leverage=LEVERAGE)

def get_balance():
    balance_info = client.futures_account_balance()
    for asset in balance_info:
        if asset['asset'] == 'USDT':
            return float(asset['balance'])
    return 0

def calculate_position_size():
    balance = get_balance()
    position_size = balance * RISK_PER_TRADE * LEVERAGE  # Ajustado para alavancagem
    return position_size

def get_market_data():
    ticker = client.futures_symbol_ticker(symbol=SYMBOL)
    return float(ticker['price'])

def trading_logic():
    while True:
        try:
            price = get_market_data()
            position_size = calculate_position_size()
            print(f"Preço atual: {price}, Tamanho da posição: {position_size}")
            time.sleep(10)  # Espera 10 segundos entre verificações
        except Exception as e:
            print(f'Erro: {e}')

# Configuração para rodar em VPS
if __name__ == "__main__":
    print("Iniciando bot de trading na VPS...")
    trading_logic()
 
