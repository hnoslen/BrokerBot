price_data_file_path = 'pricedata'
points_to_save = 1000
npext = '.npy'
logfilename = "activityLog.txt"
cbase_version='2017-12-01'

import numpy as np
import os.path
import time
from coinbase.wallet.client import Client
import getpass

# Logging functions
def log(action, quantity, price):
	with open(logfilename,"a") as logfile:
		logfile.write(str(time.time())+','+str(action)+','+str(quantity)+','+str(price))

# Functions for interfacing with coinbase
def login(api_key=None,api_secret=None):
	if api_key==None:
		api_key = getpass.getpass('Api key:')
	if api_secret==None:
		api_secret = getpass.getpass('Api secret:')
	return Client(api_key,api_secret)

def get_prices(client,curr='BTC'):
	buy_price  = client.get_buy_price(currency_pair =(curr+'-USD'))
	sell_price = client.get_sell_price(currency_pair =(curr+'-USD'))
	spot_price = client.get_spot_price(currency_pair = (curr+'-USD'))
	return float(spot_price.amount), float(buy_price.amount), float(sell_price.amount)

# Functions for saving/loading data
def save(arr, filename):
    return np.save(filename,arr)

def load(filename):
    if os.path.isfile(filename+npext):
        out = np.load(filename+npext)
    else:
    	print "File not found: "+filename+npext
        out = np.array([0])
    return out

# Functions for trend finding in data
def linearTrend(arr):
	x = np.linspace(-1*(arr.size-1),0,arr.size)
	return np.polyfit(x,arr,1)
