
import numpy as np
import pandas as pd
def RSI(pastPriceVec, window):
    price_diff = np.diff(pastPriceVec[-window:])
    gain = np.sum(price_diff[price_diff > 0])
    loss = -np.sum(price_diff[price_diff < 0])
    if loss == 0:
        return 100
    rs = gain / loss
    return 100 - (100 / (1+rs))
                
def MA(pastPriceVec, window):
    return np.mean(pastPriceVec[-window:])

def ADX(pastPriceVec, window):
    return np.mean([abs(pastPriceVec[i] - pastPriceVec[i-1]) for i in range(1, len(pastPriceVec))])

def myStrategy(pastPriceVec, currentPrice):
    MA_w = 20
    RSI_w = 14
    ADX_w = 14
    ADX_threshold = 10
    a_len = len(pastPriceVec)
    MA_w = min(a_len, MA_w)
    RSI_w = min(a_len, RSI_w)
    ADX_w = min(a_len, ADX_w)

    ma = MA(pastPriceVec, MA_w)
    rsi = RSI(pastPriceVec, RSI_w)
    adx = ADX(pastPriceVec, ADX_w)
    if adx > ADX_threshold:
        if currentPrice > ma:
            return 1
        elif currentPrice < ma:
            return -1
    else:
        if rsi < 14:
            return 1
        elif rsi > 90:
            return -1
    return 0