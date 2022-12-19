# //+------------------------------------------------------------------+
# //|                                                                  |
# //|                                   Copyright 2022, Lucas Eduardo. |
# //|                                                                  |
# //+------------------------------------------------------------------+
import MetaTrader5 as mt5
import numpy as np
from sklearn.linear_model import ARIMA

# //+------------------------------------------------------------------+
# //| Script program start                                             |
# //+------------------------------------------------------------------+

# Inicializa a conexão MT5
mt5.initialize()

while True:
    
    # definir o ticker e o time frame
    ticker = 'WDOF23'
    time_frame = mt5.TIMEFRAME_M5

    # obter os fechamentos históricos do time frame escolhido
    closes = mt5.copy_rates_range(ticker, time_frame, 0, 1000)

    #converter os fechamentos em um array NumPy
    closes = np.array([close.close for close in closes])

    #dividir os fechamentos em treino e teste
    train_size = int(len(closes) * 0.8)
    train, test = closes[0:train_size], closes[train_size:]

    #treinar o modelo de autoregressão
    model = ARIMA(train, order=(5,1,0))
    model_fit = model.fit(disp=0)

    #fazer previsões para os dados de teste
    predictions = model_fit.forecast(len(test))[0]

    #calcular a frequência média do desvio dos fechamentos
    mean_deviation = np.mean(np.abs(predictions - test))

    #calcular a VWAP histórica do time frame escolhido
    vwap = np.mean(closes)

    #comparar o valor estimado pelo modelo com a VWAP histórica e a frequência média do desvio dos fechamentos
    if predictions[-1] > vwap > mean_deviation:
        print("Bom momento pra VENDER !!!")
    elif predictions[-1] < vwap < mean_deviation:
        print("Bom momento pra COMPRAR !!!")
    else:
        print("O preço está neutro")
# Adicione aqui qualquer lógica que deseje usar para interromper o loop
        # Por exemplo, você pode adicionar uma condição para verificar se o usuário deseja continuar o loop
        # e, se não desejar, usar o comando "break" para sair do loop
    #     break
    # finally:
    #     mt5.shutdown()
    
# //+------------------------------------------------------------------+
# //| Script program end                                               |
# //+------------------------------------------------------------------+


# o algoritimo usando a lib metatrader5 e python que
# define um ticker e a partir do ticker, defina um time frame, e a partir dos fechamentos históricos do time frame, 
# do ticker faz uma autoregressão levando em conta á série histórica do time frame, os fechamentos históricos do time 
# frame e estima se o preço do ticker está barato ou caro, ou neutro baseado na autoregressão
# e no calculo da frequência média do desvio dos fechamentos da série histórica toda com os fechamentos de time frame
# com a vwap histórica do time frame faz o print("O preço está caro") se estiver caro, faça o print("O preço está
# barato") se estiver barato,e faça o print("O preço está neutro") se estiver neutro.