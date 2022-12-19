# //+------------------------------------------------------------------+
# //|                                                                  |
# //|                                   Copyright 2022, Lucas Eduardo. |
# //|                                                                  |
# //+------------------------------------------------------------------+
import MetaTrader5 as mt5
# //+------------------------------------------------------------------+
# //| Script program start                                             |
# //+------------------------------------------------------------------+

# Conecte-se ao servidor MetaTrader5
if not mt5.initialize():
    print("Falha ao inicializar a biblioteca MetaTrader5")
    exit()

# Defina o ticker e o time frame, etc...
ticker = "WDOF23"
time_frame = mt5.TIMEFRAME_M5
input_max_deviation = 0,123
input_min_deviation = -0,234

# Obtenha as informações do ticker
symbol_info = mt5.symbol_info_tick(ticker)

# Obtenha os dados de ticks para o time frame especificado
ticks = mt5.copy_ticks_range(ticker, time_frame, 0, symbol_info.count)

# Calcule a vwap histórica do time frame
vwap = mt5.vwap(ticker, time_frame, 0, symbol_info.count)

# Inicie o loop sem interrupção
while True:
    # Obtenha os últimos ticks
    latest_ticks = mt5.copy_ticks_range(ticker, time_frame, -1, 1)
    if not latest_ticks:
        continue

    # Calcule a frequência do maior e menor desvio dos fechamentos
    max_deviation = max(ticks.close) - latest_ticks[0].close
    min_deviation = latest_ticks[0].close - min(ticks.close)

    if max_deviation >= input_min_deviation:
        # Imprima a mensagem "Bom momento para VENDER"
        print("Bom momento para VENDER !!!")
    elif min_deviation >= input_max_deviation:
        # Imprima a mensagem "Bom momento para COMPRAR"
        print("Bom momento para COMPRAR !!!")
# //+------------------------------------------------------------------+
# //| Script program end                                               |
# //+------------------------------------------------------------------+
