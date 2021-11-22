import numpy as np
import sys

def extractFileNameForPlotting(filename):

    data=np.load(filename,allow_pickle=True)
#    print('Doing the extractFileNameForPlotting code for' + filename)
#    filenames=[]
#    filename_name=filename.split('.')[0]
#    print(filename.split('.')[0])
#    f=open(str(filename.split('.')[0])+'.txt','w')
    for i in data:
        try:
#            f.write(i+'\n')
            print(i)
#            filenames.append(i[0])
        except:
            pass
#    f.close()
if __name__ == '__main__':
    extractFileNameForPlotting(sys.argv[1])
