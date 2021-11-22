import numpy as np
import sys

def slidingWindow(l,step):
    x=0
    masterindexlist=[]
    while x+int(step)<int(l):
#        print(str(x)+' '+str(x+3))
        tempindexlist=[]
        tempindexlist.append(x)
        tempindexlist.append(int(x)+int(step))
        masterindexlist.append(tempindexlist)
        x+=1
#    print(masterindexlist)
    return(masterindexlist)

if __name__=='__main__':
    slidingWindow(sys.argv[1],sys.argv[2])
