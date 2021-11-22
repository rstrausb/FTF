import numpy as np
from matplotlib import pyplot
import pathlib
import os
from helpplotting2 import helpplot
import sys
from multiprocessing import Pool
import itertools

f=open('possibleTransients'+'_sw'+str(sys.argv[4])+'_ip'+str(sys.argv[5])+'_slopefiltered.txt','r')
files=[]
for i in f.readlines():
    if 'None' in i:
        None
    else:
        files.append(i.strip())


#files=np.load(possibleTransient.npy

#folderForSaving='Potential_Transients'

#dataDirectory='home/strausbaugh/DWF/'

def plotOnePossibleTransient(possibleTransientFileName,folderForSaving,dataDirectory):

    path=pathlib.PurePath(possibleTransientFileName)
    fileName=path.name
#    print(path)
#    obj=filename.split('_')[0]
    obj=fileName
#    print(obj)
#    try:
#        os.mkdir(folderForSaving+'/'+obj)
#    except:
#        print("Folder "+obj+" probably already exists")
#    for j in os.listdir(dataDirectory):
#        if obj.split('_')[0] in j:
#            print(j)
#            print(obj)
    try:
        helpplot(dataDirectory+obj)
        print("Plotting "+obj)
        pyplot.savefig(folderForSaving+'/'+obj+'.png')
        pyplot.clf()
    except:
        print('Something wrong with file '+str(dataDirectory+obj)+'. Could not plot data')

if __name__=='__main__':
#    plotOnePossibleTransient(sys.argv[1],sys.argv[2],sys.argv[3])
    pool=Pool()
    pool.starmap(plotOnePossibleTransient,zip(files,itertools.repeat(sys.argv[2]),itertools.repeat(sys.argv[3])))
