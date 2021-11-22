#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:00:11 2020

@author: strausbaugh
"""
import numpy as np
from matplotlib import pyplot

def helpplot(filename):
#    t,m,dm,ul=np.loadtxt('/home/strausbaugh/DWF/Data/files/'+str(filename),unpack=True,skiprows=1)
    t,m,dm,ul=np.loadtxt(str(filename),unpack=True,skiprows=1)
    keep=np.where(m!=0.0)[0]
    tstart=t
    t=[]
    for i in tstart:
        t.append((i-tstart[0])*24*60)
    t=np.array(t)
    m_temp=m[keep]
    t_temp=t[keep]
    dm_temp=dm[keep]

    mkeep=[]
    tkeep=[]
    dmkeep=[]
    try:
        keep2=np.where(m_temp<25.0)[0]
        tkeep=t_temp[keep2]
        mkeep=m_temp[keep2]
        dmkeep=dm_temp[keep2]
    except:
        pass

    upkeep=np.where(m==0.0)[0]
    tup=t[upkeep]
    ulup=ul[upkeep]
    ulplot=[]
    for i in ulup:
        if len(mkeep)==0:
            ulplot.append(i)
        else:
            if i>np.max(mkeep):
                ulplot.append(np.max(mkeep)+0.1)
            else:
                ulplot.append(i)
#    pyplot.xlabel('MJD')
    pyplot.xlabel('Time from first observation (min)')
    pyplot.ylabel('g')
#    pyplot.plot(tkeep,mkeep,'k.')   
    try:
        pyplot.errorbar(tkeep,mkeep,yerr=dmkeep,linestyle='',marker='.')
        pyplot.ylim(np.max(mkeep)+0.2,np.min(mkeep)-0.2)

    except:
        pass
    if len(mkeep)==0:
        pyplot.ylim(np.max(ulplot)+0.2,np.min(ulplot)-0.2)
    pyplot.plot(tup,ulplot,'rv')
    return(tkeep,mkeep,dmkeep)
