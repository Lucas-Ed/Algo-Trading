# //+------------------------------------------------------------------+
# //|                                                                  |
# //|                                   Copyright 2022, Lucas Eduardo. |
# //|                                                                  |
# //+------------------------------------------------------------------+
# 1. Instale a biblioteca MetaTrader5
!pip install MetaTrader5
# 2. Importe a biblioteca MetaTrader5 e as funções necessárias
import MetaTrader5 as mt5
# //+------------------------------------------------------------------+
# //| Script program start                                             |
# //+------------------------------------------------------------------+

# 3. Defina o ticker e o time frame
ticker = "WDOF23"
time_frame = mt5.TIMEFRAME_M1

# 4. Obtenha os fechamentos do time frame
rates = mt5.copy_rates_from_pos(ticker, time_frame, 0, 30)

# 5. Crie um dataframe pandas com os fechamentos
df = pd.DataFrame(rates)

# 6.Adicione uma coluna de volume ao dataframe
df["volume"] = df["tick_volume"]

# 7. Calcule o preço VWAP do momento a partir dos dados do time frame
vwap = (df['close'] * df['volume']).sum() / df['volume'].sum()
print("O preço da vwap do momento é: {:.2f}".format(vwap))

# 8. Calcule a frequência média do volume dos últimos 30 dias
mean_volume = df["volume"].rolling(30).mean()

# 9. Calcule o preço futuro do ticker com base na vwap atual
future_price = vwap * mean_volume# ou vwap +  mean_volume * 0.01

# 10. Imprima o preço futuro do ticker
print("O preço futuro do ticker: {future_price:.4f}")


# No entanto, é importante lembrar que essa previsão de preço
#  futuro é uma estimativa baseada em dados históricos e nas suposições feitas sobre o volume futuro.
