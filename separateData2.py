import numpy as np
import sys

def separateData(allResultsfile,dataSaveDirectory,sw,ip):

    allResults=np.load(allResultsfile,allow_pickle=True)

    ip_file=open(str(dataSaveDirectory)+'/possibleTransients_sw'+str(sw)+'_ip'+str(ip)+'.txt','w')
#    ip1=open(str(dataSaveDirectory)+'/possibleTransients_sw'+str(sw)+'_ip1.txt','w')
#    ip2=open(str(dataSaveDirectory)+'/possibleTransients_sw'+str(sw)+'_ip2.txt','w')
#    ip3=open(str(dataSaveDirectory)+'/possibleTransients_sw'+str(sw)+'_ip3.txt','w')

    for i in allResults:
        try:
            if int(i[1])==int(ip):
                ip_file.write(str(i[0])+';'+str(i[2])+'\n')
        except TypeError:
            pass

    ip_file.close()

if __name__ == '__main__':
    separateData(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
