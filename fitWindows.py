import numpy as np
import sys

def fitWindows(windows):

#    windowt=np.load('windowt.npy')
#    windowm=np.load('windowm.npy')
#    windowdm=np.load('windowdm.npy')
#    windowt=(np.load(tfile,allow_pickle=True))
#    windowm=np.load(mfile,allow_pickle=True)
#    windowdm=np.load(dmfile,allow_pickle=True)

    windowt=windows[0]
    windowm=windows[1]
    windowdm=windows[2]

#    windowt_copy=[]
#    windowm_copy=[]
#    windowdm_copy=[]
#    for i in range(len(windowt)):
#        try:
#            t_0=windowt[i][0]
#            windowt_temp=[]
#            windowm_temp=[]
#            windowdm_temp=[]
#            for j in range(len(windowt[i])):
#                windowt_temp.append((windowt[i][j]-t_0)*24*60.)
#                windowm_temp.append(windowm[i][j])
#                windowdm_temp.append(windowdm[i][j])
#            windowt_copy.append(np.array(windowt_temp))
#            windowm_copy.append(np.array(windowm_temp))
#            windowdm_copy.append(np.array(windowdm_temp))
#        except:
#            pass
#    windowt=np.array(windowt_copy)
#    windowm=np.array(windowm_copy)
#    windowdm=np.array(windowdm_copy)


    slopelist=[]
#    masterslopelist=[]
#    for i in range(len(windowt)):
#        tmpslopelist=[]
    for i in range(len(windowt)):
        for j in range(len(windowt[i])):
            try:
                p, residuals, _, _, _ =np.polyfit(windowt[i][j],windowm[i][j],deg=1,full=True)
                red_chi_squared=residuals/(len(windowt[i][j])-2)
#                p=np.polyfit(windowt[i][j],windowm[i][j],deg=1)
#                red_chi_squared=np.sum((np.polyval(p,windowt[i][j])-windowm[i][j])**2)/(len(windowt[i][j])-2)
#                fitparams=np.sqrt(np.diag(cov))

#            popt,pcov=curve_fit(linfunc,windowt[i][j],windowm[i][j],sigma=windowdm[i][j])
#            slope=popt[0]
#            print(popt)
#            print('made it past slope')
            #tmpslopelist.append(slope)
        #masterslopelist.append(slope)
#            print('made it past appending slope value')
#                print(p[0],fitparams[0])

#                slopelist.append([p[0],fitparams[0])
                slopelist.append([p[0],red_chi_squared[0]])
            except np.linalg.LinAlgError:
                pass

    return(slopelist)

#    np.save('slopes_'+str(sw)+'.npy',slopelist)
#    np.save('masterSlopes_'+str(sw)+'.npy',masterslopelist)

if __name__ == '__main__':
    fitWindows(sys.argv[1])
