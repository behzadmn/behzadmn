import numpy as np
import pandas as pd
import requests
import json


def get_bars_panda_ichi(symbol, interval,limit):
    url = root_url + '?symbol=' + symbol + '&interval=' + interval + '&limit=' + limit
    response = session.get(url)
    data = json.loads(response.text)
    # df = pd.DataFrame(data)
    df = pd.DataFrame(data, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume','a','b','c','d','e','f'])
    df['Open'] = df['Open'].astype(np.float64)
    df['High'] = df['High'].astype(np.float64)
    df['Low'] = df['Low'].astype(np.float64)
    df['Close'] = df['Close'].astype(np.float64)
    df['Volume'] = df['Volume'].astype(np.float64)
    # print(df['Close'])
    # print(type(df))
    # print(df)
    return df
    
def chaikin_volatility_strategy(high, low, length=10, roc_length=12, trigger=0, reverse=False):
    x_price = high - low
    xroc_ema = np.zeros_like(x_price)
    pos = np.zeros_like(x_price)
    possig = np.zeros_like(x_price)
    signal = np.zeros_like(x_price)

    for i in range(len(high)):
        if i >= length:
            xroc_ema[i] = (xroc_ema[i-1] * (roc_length - 1) + (x_price[i] - x_price[i-length])) / roc_length

            if xroc_ema[i] < trigger:
                pos[i] = 1
            elif xroc_ema[i] > trigger:
                pos[i] = -1
            else:
                pos[i] = pos[i-1]

            if reverse:
                if pos[i] == 1:
                    possig[i] = -1
                elif pos[i] == -1:
                    possig[i] = 1
                else:
                    possig[i] = pos[i]
            else:
                possig[i] = pos[i]

            if possig[i] == 1:
                signal[i] = 1
            elif possig[i] == -1:
                signal[i] = -1

    return signal

# Example usage
try:
    root_url = 'https://api.binance.com/api/v1/klines'
    cryptos = {
        "cryptos": ["BTCUSDT" , "ETHUSDT", "BNBUSDT" , "SHIBUSDT", "SOLUSDT" , "LINKUSDT" , "LINAUSDT" , "LUNAUSDT" , "LUNCUSDT" , "AVAXUSDT" , "KAVAUSDT" , "ADAUSDT" , "DOTUSDT"]
    }
    df1 = pd.DataFrame(cryptos)
    crypt = df1[df1.columns[0]]
    for i in range(len(crypt)):  
        crypto = crypt[i]
        steemeth = get_bars_panda_ichi(crypto, '1d', '200')
        steemeth = steemeth.dropna()

        o = steemeth[steemeth.columns[1]]
        h = steemeth[steemeth.columns[2]]
        l = steemeth[steemeth.columns[3]]
        c = steemeth[steemeth.columns[4]]
        v = steemeth[steemeth.columns[5]]
    
    signal = chaikin_volatility_strategy(high, low, length=10, roc_length=12, trigger=0, reverse=False)
    print(signal)
except Exception as error:
    print(Exception)
