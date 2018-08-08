import pickle
import json
import time
import datetime
from five_minUpdate import fiveMinUpdate
from indicators import EMAcrossFunc


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

def fiveMin():
    while True:
        fiveMinUpdate()
        ema_interval = 'fifteenMin'
        ema1 = 7
        ema2 = 25
        json_in = open('pickleData/pairsETH.json', 'r')
        tickers = json.load(json_in)
        EMAcross(tickers, ema1, ema2, ema_interval)
    t = datetime.datetime.now()
    sleeptime = 60 - (t.second + t.microsecond/1000000.0)
    time.sleep(sleeptime)

