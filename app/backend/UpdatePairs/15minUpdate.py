import time
import datetime
import pickle
import pandas as pd
import json

def getData(ticker, interval, startTime):
    try:
        link = 'https://api.binance.com/api/v1/klines?symbol='+ticker+'&interval='+interval+'&startTime='+startTime  
        crypto = pd.read_json(link)
        crypto.columns = ["Date", "Open", "High", "Low", "Close", "Volume", "CloseTime", "QuoteAssestVolume","NumberOfTrades", "TakerBuy", "TakerBuy2", "Ignore"]
        crypto.drop(["CloseTime", "QuoteAssestVolume","NumberOfTrades", "TakerBuy", "TakerBuy2", "Ignore"], axis=1, inplace=True)
        crypto['Date'] = pd.to_datetime(crypto['Date'], unit='ms')
        crypto.set_index('Date', inplace=True)
        return crypto
    except:
        e = 'NA'
        return str(e)

def fiveMinUpdate():
    while True:
        if datetime.datetime.now().minute % 15 == 0:
            a = datetime.datetime.now()
            print(a)
            json_in = open('./Backend/pickleData/pairsETH.json', 'r')
            tickers = json.load(json_in)
            for pair in tickers:
                ticker = str(pair)
                cryptoTime = str(round(time.time() * 1000) - 180000000)
                interval = '15m'
                data = getData(ticker, interval, cryptoTime)
                if data is 'NA':
                    print(ticker + ': is no longer active')
                else:
                    pickle_out = open('./Backend/pickleData/fifteenMin/' + pair + '.pickle', 'wb')
                    pickle.dump(data, pickle_out)
                    pickle_out.close()
            b = datetime.datetime.now()
            print(b)
            print("Done updating 15 min data.")
        t = datetime.datetime.now()
        sleeptime = 60 - (t.second + t.microsecond/1000000.0)
        time.sleep(sleeptime)

fiveMinUpdate()