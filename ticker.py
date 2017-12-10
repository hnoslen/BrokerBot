# Program to display market status and buy/sell status

points_to_display = 1000
plotfile_name = 'current_market.png'

import matplotlib.pyplot as plt
import numpy as np
import os

def generateplot(timearray,dataarray,filename_plot):
    fig = plt.figure()
    if (dataarray.size > 2):
        if (dataarray[-1]-dataarray[-2]) > 0:
            c = 'g'
        else:
            c = 'r'
    else:
        c = 'b'
    plt.plot(timearray,dataarray,figure = fig)
    plt.ylabel("Price in USD")
    plt.xlabel("Time Before Present")
    plt.savefig(filename_plot)
    return 1

def displayimage(filename_plot):
    os.system('sudo killall -9 fbi')
    os.system('sudo fbi '+filename_plot)

