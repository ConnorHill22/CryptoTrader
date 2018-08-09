import numpy as np
import pandas as pd


def rsiFunc(prices, n):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)
    return rsi[-1]


def insideBarFunc(prices):
    # prices["High"] = prices.High.astype(float)
    # prices["Low"] = prices.Low.astype(float)
    if prices.iloc[0]["High"] > prices.iloc[1]["High"] and prices.iloc[0]["Low"] < prices.iloc[1]["Low"]:
        return True
    else:
        return False

def SMAcrossFunc(prices, sma1, sma2):
    prices['SMA(1)'] = prices.Close.rolling(sma1).mean()
    prices['SMA(2)'] = prices.Close.rolling(sma2).mean()
    if prices.iloc[-2]['SMA(1)'] < prices.iloc[-2]['SMA(2)'] and prices.iloc[-1]['SMA(1)'] > prices.iloc[-1]['SMA(2)']:
        return "SMA("+str(sma1)+") crossed SMA("+str(sma2)+")"
    elif prices.iloc[-2]['SMA(1)'] > prices.iloc[-2]['SMA(2)'] and prices.iloc[-1]['SMA(1)'] < prices.iloc[-1]['SMA(2)']:
        return "SMA("+str(sma2)+") crossed SMA("+str(sma1)+")"
    else:
        return "None"

def EMAcrossFunc(prices, ema1, ema2):
    prices['EMA(1)'] = prices['Close'].ewm(span = ema1, adjust=False).mean()
    prices['EMA(2)'] = prices['Close'].ewm(span = ema2, adjust=False).mean()
    if prices.iloc[-2]['EMA(1)'] < prices.iloc[-2]['EMA(2)'] and prices.iloc[-1]['EMA(1)'] > prices.iloc[-1]['EMA(2)']:
        return "EMA("+str(ema1)+") crossed EMA("+str(ema2)+")"
    elif prices.iloc[-2]['EMA(1)'] > prices.iloc[-2]['EMA(2)'] and prices.iloc[-1]['EMA(1)'] < prices.iloc[-1]['EMA(2)']:
        return "EMA("+str(ema2)+") crossed EMA("+str(ema1)+")"
    else:
        return "None"
