import numpy as np
import os
import sys

def dataExtract(filename):
#mastertlist=[]
#mastermlist=[]
#masterdmlist=[]
#for i in os.listdir('/home/strausbaugh/DWF/Data/fourhour2/files'):
#f=open('/home/strausbaugh/DWF/Data/fourhour2/files/goodlc_clean_10.txt','r')
#filelist=[]
#mastertlist=[]
#mastermlist=[]
#masterdmlist=[]

#for i in f.readlines():
#    filelist.append(i)
#f.close()
#for i in filelist:
#    if 'DWF' in i:
    t,m,dm,ul=np.loadtxt(str(filename.strip()),unpack=True,skiprows=1)
    keep=np.where(m!=0.0)[0]
    if len(keep)<10:
        pass
    else:
        m_temp=m[keep]
        t_temp=t[keep]
        dm_temp=dm[keep]
        keep2=np.where(m_temp<25.0)[0]
        #print(keep)
        tkeep=t_temp[keep2]
        mkeep=m_temp[keep2]
        dmkeep=dm_temp[keep2]
        #    print('Line below this is the error')
        mmed=np.abs(mkeep-np.median(mkeep))
        #    print('Error is somewhere else later')
        keeptest=np.where(mmed>2.5)[0]
        if len(keeptest)==1:
        #        print('keeptest=1')
        #        print(i)
            keep3=np.where(mmed<2.5)[0]
            mkeep3=mkeep[keep3]
            dmkeep3=dmkeep[keep3]
            tkeep3=tkeep[keep3]
        else:
    #        print('keeptest!=1')
            mkeep3=mkeep
            tkeep3=tkeep
            dmkeep3=dmkeep
    #        print(len(tkeep3),len(mkeep3))
#    mastertlist.append(tkeep3)
             #sys.stdout.write(str(tkeep3)+','+str(mkeep3)+','+str(dmkeep3))
        datatofile=[filename.strip()]
        datatofile.append(tkeep3*24.0*60.0)
        datatofile.append(mkeep3)
        datatofile.append(dmkeep3)
        return(datatofile)
#        np.save('alldata.npy',np.array(datatofile))
#        print('Extracted '+str(filename))
#    mastermlist.append(mkeep3)
#sys.stdout.write(mkeep3)
#    masterdmlist.append(dmkeep3)
#sys.stdout.write(dmkeep3)
#f.close()

#print(len(mastermlist))
#if __name__ == '__main__':
#    dataExtract(sys.argv[1])

