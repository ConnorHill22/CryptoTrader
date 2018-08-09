import json
import time
from datetime import datetime
import pandas as pd
from indicators import rsiFunc
import talib

def getData(ticker, interval, startTime):
    try:
        link = 'https://api.binance.com/api/v1/klines?symbol='+ticker+'&interval='+interval+'&startTime='+startTime 
        crypto = pd.read_json(link)
        crypto.columns = ["Date", "Open", "High", "Low", "Close", "Volume", "CloseTime", "QuoteAssestVolume","NumberOfTrades", "TakerBuy", "TakerBuy2", "Ignore"]
        crypto.drop(["CloseTime", "QuoteAssestVolume","NumberOfTrades", "TakerBuy", "TakerBuy2", "Ignore"], axis=1, inplace=True)
        crypto['Date'] = pd.to_datetime(crypto['Date'], unit='ms')
        crypto.set_index('Date', inplace=True)
        crypto["Close"].apply(pd.to_numeric)
        return crypto
    except:
        e = 'NA'
        return str(e)

def startTime(periods, interval):
    interval_choices = [['1m', 60000],['5m', 300000],['15m', 900000], ['30m', 1800000], ['1h', 3600000], ['4h', 14400000], ['1d', 86400000], ['1w', 604800000]]
    for i in interval_choices:
        if interval == i[0]:
            n = i[1]
    period = n * periods
    startTime = str(round(time.time() * 1000) - period)
    return startTime

def RSIlevel(tickers, periods, interval):
    print("Started")
    currentTime = datetime.fromtimestamp(time.time()).strftime('%c')
    tempList = []
    for coin in tickers: 
        try:
            data = getData(coin, interval, startTime(periods*2, interval))
        except:
            print(coin + " data fetch isn't working")
        try:
            RSInumber= rsiFunc(data["Close"],periods)
        except:
            print(coin + " RSI Fun not working!")
        if RSInumber > 70 and RSInumber < 100:
            tempList.append({'coin':str(coin),'status':'Over Bought','RSI_Level':str(RSInumber)})
        elif RSInumber < 30 and RSInumber > 0:
            tempList.append({'coin':str(coin),'status':'Over Sold','RSI_Level':str(RSInumber)})
    solution = [{'time': str(currentTime), 'RSI_Triggers': tempList}]
    json_in = open('data/' + interval + '/RSIstore.json', 'w')
    json.dump(solution, json_in)

def fiveMin():
    while True:
        s = datetime.fromtimestamp(time.time()).strftime('%c')
        if int(s[14:16])%5 == 0:
            interval = '5m'
            periods = 14
            json_in = open('pairs/pairsBTC.json', 'r')
            tickers = json.load(json_in)
            RSIlevel(tickers, periods, interval)
        t = datetime.now()
        sleeptime = 60 - (t.second + t.microsecond/1000000.0)
        time.sleep(sleeptime)

def fifteenMin():
    while True:
        s = datetime.fromtimestamp(time.time()).strftime('%c')
        if int(s[14:16])%15 == 0:
            interval = '15m'
            periods = 14
            json_in = open('pairs/pairsBTC.json', 'r')
            tickers = json.load(json_in)
            RSIlevel(tickers, periods, interval)
        t = datetime.now()
        sleeptime = 60 - (t.second + t.microsecond/1000000.0)
        time.sleep(sleeptime)

def oneHour():
    while True:
        s = datetime.fromtimestamp(time.time()).strftime('%c')
        if s[14:16] == "00":
            interval = '1h'
            periods = 14
            json_in = open('pairs/pairsBTC.json', 'r')
            tickers = json.load(json_in)
            RSIlevel(tickers, periods, interval)
        t = datetime.now()
        sleeptime = 60 - (t.second + t.microsecond/1000000.0)
        time.sleep(sleeptime)

def fourHour():
    while True:
        s = datetime.fromtimestamp(time.time()).strftime('%c')
        if int(s[11:13])%4 == 0:
            interval = '4h'
            periods = 14
            json_in = open('pairs/pairsBTC.json', 'r')
            tickers = json.load(json_in)
            RSIlevel(tickers, periods, interval)
        t = datetime.now()
        sleeptime = 60 - (t.second + t.microsecond/1000000.0)
        time.sleep(sleeptime)

def oneDay():
    while True:
        s = datetime.fromtimestamp(time.time()).strftime('%c')
        if s[11:13] == "00":
            interval = '1d'
            periods = 14
            json_in = open('pairs/pairsBTC.json', 'r')
            tickers = json.load(json_in)
            RSIlevel(tickers, periods, interval)
        t = datetime.now()
        sleeptime = 60 - (t.second + t.microsecond/1000000.0)
        time.sleep(sleeptime)
