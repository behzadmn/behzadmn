import numpy as np

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
high = [...]  # List or array of high prices
low = [...]  # List or array of low prices

signal = chaikin_volatility_strategy(high, low, length=10, roc_length=12, trigger=0, reverse=False)
print(signal)
