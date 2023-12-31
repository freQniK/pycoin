#!/bin/env python3
import json
from pycoingecko import CoinGeckoAPI
import argparse
import sys
from os import path, environ, mkdir
cg = CoinGeckoAPI()

CRED = 'CRED'
CEND = '\033[0m'
CGREEN = 'CGREEN'
SPACE = ' '

USER      = environ['SUDO_USER'] if 'SUDO_USER' in environ else environ['USER']
BASEDIR   = path.join(path.expanduser('~' + USER), '.pycoin')

parser = argparse.ArgumentParser(description="Pycoingecko privacy coin prices - v2.1 freQniK")
parser.add_argument('--dero', action='store_true', default=False)
parser.add_argument('--haven', action='store_true', default=False)
parser.add_argument('--pirate', action='store_true', default=False)
parser.add_argument('--sentinel', action='store_true', default=False)
parser.add_argument('--monero', action='store_true', default=False)
parser.add_argument('--oxen', action='store_true', default=False)
parser.add_argument('--bitcoin', action='store_true', default=False)
parser.add_argument('--secret', action='store_true', default=False)
parser.add_argument('--kadena', action='store_true', default=False)
parser.add_argument('--zcash', action='store_true', default=False)
parser.add_argument('--zephyr', action='store_true', default=False)
parser.add_argument('--litecoin', action='store_true', default=False)
parser.add_argument('--output', action='store_true', default=False)
parser.add_argument('--read', action='store_true', default=False)

args = parser.parse_args()

if not path.isdir(BASEDIR):
    mkdir(BASEDIR)

if args.output:
        crypto = cg.get_price(ids=['dero','haven','pirate-chain', 'sentinel','monero','bitcoin','loki-network', 'secret', 'kadena', 'zcash', 'zephyr-protocol', 'litecoin'],
                              vs_currencies=['usd','btc'],
                              include_market_cap=True,
                              include_24hr_vol=True,
                              include_24hr_change=True,
                              include_last_updated_at=True)

        with open(BASEDIR + "/privacy_coins.json", "w+") as pcoins:
                pcoins.write(json.dumps(crypto))

        sys.exit(0)
        
elif args.read:
        with open(BASEDIR + "/privacy_coins.json", "r") as pcoins:
                crypto = json.loads(pcoins.read())
                
        if args.monero:
            if crypto['monero']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['monero']['usd_24h_change']
            else:
                plusminus = CRED + '%.3f' % crypto['monero']['usd_24h_change'] 
            print("%.3f \t\t  %s%% \n%s %.8f " % (crypto['monero']['usd'], plusminus, SPACE*6, crypto['monero']['btc']))

        elif args.zcash:
            if crypto['zcash']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['zcash']['usd_24h_change']
            else:
                plusminus = CRED + '%.3f' % crypto['zcash']['usd_24h_change'] 
            print("%.3f \t\t  %s%% \n%s %.8f " % (crypto['zcash']['usd'], plusminus, SPACE*6, crypto['zcash']['btc']))

        elif args.oxen:
            if crypto['loki-network']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['loki-network']['usd_24h_change']
            else:
                plusminus = CRED + '%.3f' % crypto['loki-network']['usd_24h_change'] 
            print("%.3f \t\t  %s%% \n%s %.8f " % (crypto['loki-network']['usd'], plusminus, SPACE*6, crypto['loki-network']['btc']))
            
        elif args.kadena:
            if crypto['kadena']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['kadena']['usd_24h_change']
            else:
                plusminus = CRED + '%.3f' % crypto['kadena']['usd_24h_change'] 
            print("%.3f \t\t  %s%% \n%s %.8f " % (crypto['kadena']['usd'], plusminus, SPACE*6, crypto['kadena']['btc']))

        elif args.secret:
            if crypto['secret']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['secret']['usd_24h_change']
            else:
                plusminus = CRED + '%.3f' % crypto['secret']['usd_24h_change'] 
            print("%.3f \t\t  %s%% \n%s %.8f " % (crypto['secret']['usd'], plusminus, SPACE*6, crypto['secret']['btc']))

        elif args.dero:
            if crypto['dero']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['dero']['usd_24h_change']
            else:
                plusminus = CRED + '%.3f' % crypto['dero']['usd_24h_change'] 
            print("%.3f \t\t  %s%% \n%s %.8f " % (crypto['dero']['usd'], plusminus, SPACE*6, crypto['dero']['btc']))
        elif args.haven:
            if crypto['haven']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['haven']['usd_24h_change'] 
            else:
                plusminus = CRED + '%.3f' % crypto['haven']['usd_24h_change'] 
            print("%.3f \t\t  %s%% \n%s %.8f " % (crypto['haven']['usd'], plusminus, SPACE*6, crypto['haven']['btc']))
        elif args.sentinel:
            if crypto['sentinel']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['sentinel']['usd_24h_change'] 
            else:
                plusminus = CRED + '%.4f' % crypto['sentinel']['usd_24h_change'] 
            print("%.6f \t\t  %s%% " % (crypto['sentinel']['usd'], plusminus))
        elif args.pirate:
            if crypto['pirate-chain']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['pirate-chain']['usd_24h_change']
            else:
                plusminus = CRED + '%.3f' % crypto['pirate-chain']['usd_24h_change']
            print("%.3f \t\t  %s%% \n%s %.8f " % (crypto['pirate-chain']['usd'], plusminus, SPACE*6, crypto['pirate-chain']['btc']))
        elif args.litecoin:
            if crypto['litecoin']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['litecoin']['usd_24h_change']
            else:
                plusminus = CRED + '%.3f' % crypto['litecoin']['usd_24h_change']
            print("%.3f \t\t  %s%% \n%s %.8f " % (crypto['litecoin']['usd'], plusminus, SPACE*6, crypto['litecoin']['btc']))
        else:
            if crypto['zephyr-protocol']['usd_24h_change'] >= 0:
                plusminus = CGREEN + '+%.3f' % crypto['zephyr-protocol']['usd_24h_change']
            else:
                plusminus = CRED + '%.3f' % crypto['zephyr-protocol']['usd_24h_change']
            print("%.3f \t\t  %s%% \n%s %.8f " % (crypto['zephyr-protocol']['usd'], plusminus, SPACE*6, crypto['zephyr-protocol']['btc']))

