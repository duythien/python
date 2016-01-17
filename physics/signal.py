import numpy as np 
import pylab as pl 
from scipy import signal

t = np.linspace(0, 5, 100)
x = t + np.random.normal(size = 100)

#print t
#print x
#
pl.plot(t,x, linewidth = 3)
pl.plot(t, signal.detrend(x), linewidth = 3)
pl.show()