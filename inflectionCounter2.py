import numpy as np
import sys
#from slopeHist import slopeHist
from datetime import datetime
from matplotlib import pyplot

def inflectionCounter(filename,slopes,sw,ip):  #ip is number of inflection points to count

#    slopelist=np.load(slopesFile,allow_pickle=True)
#    filelist=np.load(fileList,allow_pickle=True)
    #masterSlopes=np.load(masterSlopesFile,allow_pickle=True)

#    mu_fit,sigma_fit=slopeHist(masterSlopesFile,sw,ip,sig)
    errRange=0.25
    slopelist=[]
    slopeerror=[]
    for i in slopes:
        slopelist.append(i[0])
        slopeerror.append(i[1])

    inflectioncounter=0
#    inflectionlist=[]
#    gtlt1sigmalist=[]
    up=0
    down=0
    flat=0
#    print(slopelist)
    inflectionpositiontracker=[]
    x=0
    for j in slopelist:
#        inflectioncounter=0
#        gtlt1sigmacounter=0
#        up=0
#        down=0
#        flat=0
        #for j in i:
#       print(x) 
#      if((slopeerror[x]<1.5) and (slopeerror[x]>0.5)):
#        print(slopeerror[x])
        if j>0.01: #and (slopeerror[x]<1.0+errRange) and (slopeerror[x]>1.0-errRange):
                #gtlt1sigmacounter+=1
#            print('Found positive slope')
#            print(up,down)
#            print('positive slope with good fit')
            if up==1 and down==0 and flat==0:
                None
            elif up==0 and down==1 and flat==0:
#                if((slopeerror[x]<1.5) and (slopeerror[x]>0.5)):
                inflectioncounter+=1
                inflectionpositiontracker.append(x)
            elif up==0 and down==0 and flat==1:
#                if((slopeerror[x]<1.5) and (slopeerror[x]>0.5)):
                inflectioncounter+=1
                inflectionpositiontracker.append(x)
            else:
                None
            up=1
            down=0
            flat=0
#        elif j>0.01 and (slopeerror[x]>1.0+errRange):
#            print('positive slope with bad fit')
#            up=0
#            down=0
#            flat=0
#            None
#        elif j>0.01 and (slopeerror[x]<0.5):
#            print('positive slope with bad fit')
#            up=0
#            down=0
#            flat=0
#            None
        elif j<-0.01:# and (slopeerror[x]<1.0+errRange) and (slopeerror[x]>1.0-errRange):
#            gtlt1sigmacounter+=1
#            print('Found negative slope')
#            print(up,down)
#            print('negative slope with good fit')
            if down==1 and up==0 and flat==0:
                None
            elif down==0 and up==1 and flat==0:
#                if((slopeerror[x]<1.5) and (slopeerror[x]>0.5)):
                inflectioncounter+=1
                inflectionpositiontracker.append(x)
            elif down==0 and up==0 and flat==1:
#                if((slopeerror[x]<1.5) and (slopeerror[x]>0.5)):
                inflectioncounter+=1
                inflectionpositiontracker.append(x)
            else:
                None
            down=1
            up=0
            flat=0
#        elif j<-0.01 and (slopeerror[x]>1.0+errRange):
#            print('negative slope with bad fit')
#            up=0
#            down=0
#            flat=0
#            None
#        elif j<-0.01 and (slopeerror[x]<1.0-errRange):
#            print('negative slope with bad fit')
#            up=0
#            down=0
#            flat=0
#            None
        elif j>=-0.01 and j<=0.01:# and (slopeerror[x]<1.0+errRange) and (slopeerror[x]>1.0-errRange):
#            print('flat slope with good fit')
            if flat==1 and up==0 and down==0:
                None
            elif flat==0 and up==1 and down==0:
#                if((slopeerror[x]<1.5) and (slopeerror[x]>0.5)):
                inflectioncounter+=1
                inflectionpositiontracker.append(x)
            elif flat==0 and up==0 and down==1:
#                if((slopeerror[x]<1.5) and (slopeerror[x]>0.5)):
                inflectioncounter+=1
                inflectionpositiontracker.append(x)
            else:
                None
            flat==1
            up==0
            down==0
#        elif j>=-0.01 and j<=0.01 and (slopeerror[x]>1.0+errRange):
#            print('flat slope with bad fit')
#            up=0
#            down=0
#            flat=0
#            None
#        elif j>=-0.01 and j<=0.01 and (slopeerror[x]<1.0-errRange):
#            print('flat slope with bad fit')
#            up=0
#            down=0
#            flat=0
#            None
        else:
            None
        x+=1
#    badfitcounter=100
#    if int(inflectioncounter)<=int(ip):
#        print('Inflection counter is less than ip')
#        badfitcounter=0
#        for i in slopeerror:
#            if i>0.1:
#                badfitcounter+=1
#    else:
#        print('Inflection counter is NOT less than ip')
#        None
#    print(badfitcounter)
#    if badfitcounter!=0:
#        inflectioncounter=100
#    else:
#        None

    return([filename,inflectioncounter,inflectionpositiontracker])
if __name__ == '__main__':
    inflectionCounter(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

