from bs4 import BeautifulSoup
import requests
import json
import datetime
import time

def pairsAll():
    page = requests.get('https://coinmarketcap.com/exchanges/binance/')
    soup = BeautifulSoup(page.content, "lxml")
    cryptoName = soup.find_all("td")
    i = 5
    pairs = []
    for crypto in cryptoName:
        if i == 7:
            i = 0
            pair = crypto.contents[0].contents[0]
            pair = pair.replace("/","")
            pairs.append(pair)
        i +=1
    json_in = open('./Backend/pickleData/pairsAll.json', 'w')
    json.dump(pairs, json_in)


def pairsBTC():
    json_in = open('./Backend/pickleData/pairsAll.json', 'r')
    tickers = json.load(json_in)
    BTCpairs =[]
    for pair in tickers:
        if pair[-3:] == "BTC":
            BTCpairs.append(pair)
    json_in = open('./Backend/pickleData/pairsBTC.json', 'w')
    json.dump(BTCpairs, json_in)

def pairsUSDT():
    json_in = open('./Backend/pickleData/pairsAll.json', 'r')
    tickers = json.load(json_in)
    USDTpairs =[]
    for pair in tickers:
        if pair[-4:] == "USDT":
            USDTpairs.append(pair)
    json_in = open('./Backend/pickleData/pairsUSDT.json', 'w')
    json.dump(USDTpairs, json_in)


def pairsETH():
    json_in = open('./Backend/pickleData/pairsAll.json', 'r')
    tickers = json.load(json_in)
    ETHpairs =[]
    for pair in tickers:
        if pair[-3:] == "ETH":
            ETHpairs.append(pair)
    json_in = open('./Backend/pickleData/pairsETH.json', 'w')
    json.dump(ETHpairs, json_in)

def main():
    pairsAll()
    pairsBTC()
    pairsUSDT()
    pairsETH()


main()
