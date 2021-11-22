import numpy as np
import sys
import os
import itertools
from dataExtract2 import dataExtract
from fitWholeNight2 import fitWholeNight
from multiprocessing import Pool
import itertools


files=[]
iplocations=[]
f=open(sys.argv[1],'r')
for i in f.readlines():
    files.append(i.split(';')[0])
    iplocations.append((i.split(';')[1]).strip())
#print(files)
def filterWholeNight(filename,iploc):
#    print(filename)
        iploc1=iploc.replace('[','').replace(']','')
        iploc2=iploc1.replace('"','').split(',')
        iploc=[]
        for i in iploc2:
            try:
                iploc.append(int(i))
            except ValueError:
                pass
#    print(filename,iploc[0])
#    try:
        data=dataExtract(filename)
#        print(data)
        linfit=fitWholeNight(data,iploc)
#        print(linfit)
#        print(data)
#        if np.abs(linfit[0])<np.abs(linfit[1])/2.0:
#            return(data[0])
#        print(linfit)
        return(linfit)
#    except:
#        pass

if __name__ == '__main__':
    pool=Pool()
    results=pool.starmap(filterWholeNight,zip(files,iplocations))
#    np.save(str(sys.argv[2])+'/allResults_wholeNightSlope.npy',results)
#    np.savetxt(str(sys.argv[2])+'/PossibleTransients_sw'+str(sys.argv[3])+'_ip'+str(sys.argv[4])+'_slopefiltered.txt',results)
    np.save(str(sys.argv[2])+'/possibleTransients_sw'+str(sys.argv[3])+'_ip'+str(sys.argv[4])+'_slopefiltered.npy',results)
