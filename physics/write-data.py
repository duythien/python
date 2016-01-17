import numpy as np 
import pylab as pl 
from scipy import signal

t = np.linspace(0, 5, 100)
f = open('somefile.txt', 'wt')
for tt in t:
	f.write("%s %s \n" %(tt, 2*tt))