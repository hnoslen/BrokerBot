# Program to display market status and buy/sell status

price_data_file_path = 'pricedata'
npext = '.npy'
points_to_save = 1000
plotfile_name = 'current_market.png'

import matplotlib.pyplot as plt
import numpy as np
import os.path

def save(arr, filename):
    return np.save(filename,arr)

def load(filename):
    if os.path.isfile(filename+npext):
        out = np.load(filename+npext)
    else:
        out = np.array([0])
    return out

def generateplot(timearray,dataarray,filename_plot):
    fig = plt.figure()
    plt.plot(timearray,dataarray,figure = fig) 
    plt.ylabel("Price in USD")
    plt.xlabel("Time Before Present")
    plt.savefig('./Results/evol_conc_v'+str(vinit)+'a_'+str(a)+'.png')

