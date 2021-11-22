import numpy as np
import os
import sys
import itertools
from dataExtract2 import dataExtract
from makeWindows import makeWindows
from fitWindows import fitWindows
from slidingWindow import slidingWindow
from inflectionCounter2 import inflectionCounter
from helpplotting2 import helpplot
from multiprocessing import Pool


filesnopath=os.listdir(sys.argv[1])
files=[]
for i in filesnopath:
    files.append(str(sys.argv[1]+str(i)))

def analysis(filename,sw,ip):
#    print('Working on '+str(filename))
    try:
        data=dataExtract(filename)
        windows=makeWindows(data,sw)
        slopes=fitWindows(windows)
        result=inflectionCounter(filename,slopes,sw,ip)
        return(result)
#        return(slopes)
    except:
        pass

if __name__ == '__main__':
#    analysis(sys.argv[1],sys.argv[2],sys.argv[3])
    pool=Pool()
    results=pool.starmap(analysis,zip(files,itertools.repeat(sys.argv[3]),itertools.repeat(sys.argv[4])))
#    Slopes=pool.starmap(analysis,zip(files,itertools.repeat(sys.argv[3]),itertools.repeat(sys.argv[4])))
    print('Saving data to '+str(sys.argv[2])+'/allResults.npy')
    np.save(str(sys.argv[2])+'/allResults.npy',results)
#    np.save(str(sys.argv[2])+'/allSlopes.npy',Slopes)
