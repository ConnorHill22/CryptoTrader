import pickle
import json

def EMAcrossFunc(prices, ema1, ema2):
    prices['EMA(1)'] = prices['Close'].ewm(span = ema1, adjust=False).mean()
    prices['EMA(2)'] = prices['Close'].ewm(span = ema2, adjust=False).mean()
    if prices.iloc[-2]['EMA(1)'] < prices.iloc[-2]['EMA(2)'] and prices.iloc[-1]['EMA(1)'] > prices.iloc[-1]['EMA(2)']:
        return "EMA("+str(ema1)+") crossed EMA("+str(ema2)+")"
    elif prices.iloc[-2]['EMA(1)'] > prices.iloc[-2]['EMA(2)'] and prices.iloc[-1]['EMA(1)'] < prices.iloc[-1]['EMA(2)']:
        return "EMA("+str(ema2)+") crossed EMA("+str(ema1)+")"
    else:
        return "None"

def RSI(tickers, interval, periods):
    for coin in tickers:
        pickle_in = open('Backend/pickleData/'+ interval +'/' + coin + '.pickle', 'rb')
        data = pickle.load(pickle_in)
        data = data.iloc[-periods:]["Close"]
        rsi = rsiFunc(data,periods)
        if rsi > 70 :
            print(coin + ' is overbought at ' + str(rsi))
        elif rsi < 30 and rsi > 0:
            print(coin + ' is oversold at ' + str(rsi))

def insideBar(tickers, interval):
    for coin in tickers:
        pickle_in = open('Backend/pickleData/'+ interval +'/' + coin + '.pickle', 'rb')
        data = pickle.load(pickle_in)
        data = data.iloc[-3:]
        iB = insideBarFunc(data)
        if iB == True :
            print(coin + ' has an inside bar formed')

def SMAcross(tickers, sma1, sma2, interval):
    if sma1 > sma2:
        placeholder = sma2
        sma2 = sma1
        sma1 = placeholder
    for coin in tickers:
        pickle_in = open('Backend/pickleData/'+ interval +'/' + coin + '.pickle', 'rb')
        data = pickle.load(pickle_in)
        data = data.iloc[-sma2:]
        SMA = SMAcrossFunc(data,sma1,sma2)
        if SMA != "None":
            print(coin + ": " + SMA)

def EMAcross(tickers, ema1, ema2, interval):
    if ema1 > ema2:
        placeholder = ema2
        ema2 = ema1
        ema1 = placeholder
    for coin in tickers:
        pickle_in = open('Backend/pickleData/'+ interval +'/' + coin + '.pickle', 'rb')
        data = pickle.load(pickle_in)
        data = data.iloc[-ema2:]
        EMA = EMAcrossFunc(data,ema1,ema2)
        if EMA != "None":
            print(coin + ": " + EMA)

#interval_posibilities = ['1m', '5m', '15m', '30m', '1h', '4h', '1d', '1w']


RSI_periods = 14
RSI_interval ='fifteenMin'

insideBar_interval = 'fifteenMin'

sma_interval = 'fifteenMin'
sma1 = 9
sma2 = 20

ema_interval = 'fifteenMin'
ema1 = 7
ema2 = 25

json_in = open('Backend/pickleData/pairsETH.json', 'r')
tickers = json.load(json_in)

RSI(tickers,RSI_interval,RSI_periods)
insideBar(tickers,insideBar_interval)
SMAcross(tickers,sma1, sma2, sma_interval)
EMAcross(tickers, ema1, ema2, ema_interval)
