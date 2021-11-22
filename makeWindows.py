import numpy as np
import sys
from slidingWindow import slidingWindow

def makeWindows(data,sw):
#    filenamelist=[]
#    mastertlist=[]
#    mastermlist=[]
#    masterdmlist=[]

#    data=np.load(filename,allow_pickle=True)

    filename=data[0]
    t=data[1]
    m=data[2]
    dm=data[3]

#    for i in data:
#        try:
#            filenamelist.append(i[0])
#            mastertlist.append(i[1])
#            mastermlist.append(i[2])
#            masterdmlist.append(i[3])
#        except TypeError:
#            pass
#    data=0
    windowt=[]
    windowm=[]
    windowdm=[]
#    for i in range(len(mastermlist)):
    # try:
    l=len(m)
    slidingwindowindices=slidingWindow(l,int(sw))
    #    tmp_slopelist=[]
    tmp_windowt=[]
    tmp_windowm=[]
    tmp_windowdm=[]
    for j in slidingwindowindices:
        tmp_t=t[j[0]:j[1]]
        tmp_m=m[j[0]:j[1]]
        tmp_dm=dm[j[0]:j[1]]
    #        popt,pcov=np.polyfit(tmp_t,tmp_m,1,cov=True)
    #        tmp_slopelist.append(popt[1])
        tmp_windowt.append(tmp_t)
        tmp_windowm.append(tmp_m)
        tmp_windowdm.append(tmp_dm)
    #    windowslopes.append(tmp_slopelist)
    windowt.append(tmp_windowt)
    windowm.append(tmp_windowm)
    windowdm.append(tmp_windowdm)

    allWindow=[windowt,windowm,windowdm]

    return(allWindow)

    #tFileName='windowt_'+str(sw)+'.npy'
    #mFileName='windowm_'+str(sw)+'.npy'
    #dmFileName='windowdm_'+str(sw)+'.npy'
    #fileNames='filenames_'+str(sw)+'.npy'

    #np.save(tFileName,np.array(windowt))
    #np.save(mFileName,np.array(windowm))
    #np.save(dmFileName,np.array(windowdm))
    #np.save(fileNames,np.array(filenamelist))

#    np.save('windowt.npy',np.array(windowt))
#    np.save('windowm.npy',np.array(windowm))
#    np.save('windowdm.npy',np.array(windowdm))
#    np.save('filenames.npy',np.array(filenamelist))

if __name__ == '__main__':
    makeWindows(sys.argv[1],sys.argv[2])
