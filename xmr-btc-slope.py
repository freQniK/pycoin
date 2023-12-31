#!/bin/env python3
import json
from pycoingecko import CoinGeckoAPI
import argparse
import datetime
import time


MINSPREAD = 2.0
MAXSPREAD = 6.0
BUFFER = 0.314


def APR(xmrbtc, slope, b):
    print("y = %.3f * %.8f + %.3f" % (slope, xmrbtc,b))
    return round(float(float(slope*xmrbtc) + float(b)),3)


def main():
    cg = CoinGeckoAPI()
    
    
    today = datetime.datetime.now()
    
    xmrbtc = float(cg.get_coin_history_by_id(id="monero", date=today.strftime("%d-%m-%Y"))["market_data"]["current_price"]["btc"])
    
    xmrbtcdata = [] 
    for k in range(1,14):    
        delta = datetime.timedelta(days=k)
        yesterday = today - delta
        data = cg.get_coin_history_by_id(id="monero", date=yesterday.strftime("%d-%m-%Y"))
        xmrbtcdata.append(data["market_data"]["current_price"]["btc"])
        time.sleep(10)
        
    #for price in xmrbtcdata:
    #    print(price)
        
    max_xmrbtc = max(xmrbtcdata)
    min_xmrbtc = min(xmrbtcdata)
    
    print("Max: %s\nMin: %s" % (max_xmrbtc, min_xmrbtc))
    
    slope = round(float((MINSPREAD - MAXSPREAD)/float(float(max_xmrbtc) - float(min_xmrbtc))),3)
    
    b = round(float(MAXSPREAD) - float(slope*float(min_xmrbtc)),3)

    print("SPREAD: %f" % (APR(xmrbtc,slope,b) + BUFFER))

if __name__ == "__main__":
    main()
