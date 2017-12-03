import numpy as np
import matplotlib.pyplot as plt

#number of past points to use
n = 100

#weights for fit
w = np.ones(n)

# Open price datafile
list_of_prices = []

x = np.linspace(-99,0,100)
next = np.array(1.0)
i = n
l = len(list_of_prices)-1
uncerts = []
while (i < l):
    y = np.array(list_of_prices[(i-n):i])
    fit = np.polyfit(x,y,1)
    prediction = np.polyval(fit,next)
    uncerts.append(list_of_prices[i]-prediction[0])

outfile = open('uncerts'+str(n)'.txt', 'w')
for item in uncerts:
    outfile.write("%s\n" % item)
outfile.close()
  
