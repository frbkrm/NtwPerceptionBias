import numpy as np 
import matplotlib.pyplot as plt 
import os, sys, inspect
import math

plt.rcParams["font.family"] = "sans-serif"

fminor_list = [0.2]

fig = plt.figure(figsize = (10,6))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)


cmap = [ 'violet','yellowgreen']
for fi in range(len(fminor_list)) : 

    fminor = fminor_list[fi]
    fa = fminor 
    fb = 1.-fminor 

    minor_data = np.loadtxt('0hop_neterr_minor_fa%s.txt' %(fminor))
    major_data = np.loadtxt('0hop_neterr_major_fa%s.txt' %(fminor))

    minorh = minor_data[:,0]
    minor_neterr = minor_data[:,1]
    minor_neterr_std = minor_data[:,2]

    hop_minor_data = np.loadtxt('1.0_hop_neterr_minor_fa%s_avg_sum.txt' %(fminor))
    hop_major_data = np.loadtxt('1.0_hop_neterr_major_fa%s_avg_sum.txt' %(fminor))

    hop_y_min_mean = hop_minor_data[:,1]
    hop_y_min_std = hop_minor_data[:,2]

    '''Fig.5(a) for the minority ''' 
    ax1.axhline(y= 1, color = 'grey', ls = 'dashed')
    ax1.plot(minorh, (minor_neterr)/fminor, marker = 'o', label = 'ego', color = cmap[0] , mec = 'black')
    ax1.errorbar(minorh, (minor_neterr)/fminor, yerr = minor_neterr_std,  color = cmap[0] )
    ax1.plot(minorh, (hop_y_min_mean)/fminor  , marker = '^', label = '1-hop weighted avg.' , color = cmap[1] , mec = 'black')
    ax1.errorbar(minorh, (hop_y_min_mean)/fminor, yerr= hop_y_min_std  ,  color = cmap[1] )
    ax1.xaxis.set_tick_params(labelsize=20)
    ax1.yaxis.set_tick_params(labelsize=20)
    ax1.set_xlabel(r'$h$', fontsize = 24)
    ax1.set_ylabel(r'$P_{indv.}$', fontsize = 24)
    ax1.legend(numpoints = 1, loc = 'best' ,fontsize = 20)

    '''Inset1 in the Fig.5(a)''' 
    in1 = fig.add_axes([0.2, 0.6, 0.2, 0.27])
    in1.axhline(y=1, color = 'grey', ls = 'dashed')
    in1.xaxis.set_tick_params(labelsize=14)
    in1.yaxis.set_tick_params(labelsize=14)
    in1.plot(minorh[1:], (minor_neterr[1:])/fminor, marker = 'o', color = cmap[0])
    in1.plot(minorh[1:], (hop_y_min_mean[1:])/fminor , ls = 'dashed', marker = '^', color = cmap[1])
    in1.set_xlabel(r'$h$',fontsize = 18, labelpad = 0.5)
    in1.set_ylabel(r'$P_{indv.}$',fontsize =18, labelpad = -2)
    in1.set_xticklabels([0.1, '', 0.3, '', 0.5, '', 0.7, '', 0.9, '', 1.0])
    in1.set_xlim([0.1,1.0])
    in1.set_yscale('log')


    '''Fig.5(b) for the majority'''     
    hop_y_maj_mean = hop_major_data[:,1]
    hop_y_maj_std = hop_major_data[:,2]
    majorh = major_data[:,0]
    major_neterr = major_data[:,1]
    major_neterr_std = major_data[:,2]
    ax2.axhline(y= 1, color = 'grey', ls = 'dashed')
    ax2.plot(majorh, (major_neterr)/fminor , marker = 'o', label = 'ego' , color = cmap[0] , mec = 'black')
    ax2.errorbar(minorh, (major_neterr)/fminor, yerr = major_neterr_std,  color = cmap[0] )
    ax2.plot(majorh, (hop_y_maj_mean)/fminor , marker = '^', label = '1-hop weighted avg.' , color = cmap[1] , mec = 'black')
    ax2.errorbar(minorh, (hop_y_maj_mean)/fminor, yerr = hop_y_maj_std,  color = cmap[1] )
    ax2.set_xlabel(r'$h$', fontsize = 24)
    ax2.xaxis.set_tick_params(labelsize=20)
    ax2.yaxis.set_tick_params(labelsize=20)

    '''Inset2''' 
    in2 = fig.add_axes([0.68, 0.6, 0.2, 0.27])
    in2.axhline(y=1, color = 'grey', ls = 'dashed')
    in2.xaxis.set_tick_params(labelsize=14)
    in2.yaxis.set_tick_params(labelsize=14)
    inh = majorh[:10]
    inh_major = major_neterr[:10]
    inh_major_hop = hop_y_maj_mean[:10]
    in2.plot(inh, (inh_major)/fminor, marker = 'o', color = cmap[0])
    in2.plot(inh, (inh_major_hop)/fminor, marker = '^', ls = 'dashed', color = cmap[1])
    in2.set_xlabel(r'$h$',fontsize = 18, labelpad = 0.5)
    in2.set_ylabel(r'$P_{indv.}$',fontsize =18, labelpad = -2)
    in2.set_xlim([0.0, 0.92])
    in2.set_yscale('log')
    

ax1.xaxis.set_ticks(np.arange(0, 1.2, 0.2))
ax2.xaxis.set_ticks(np.arange(0, 1.2, 0.2))

ax1.text(0.28,5.1, '(a) Minority',fontsize = 20)
ax2.text(0.28,5.1, '(b) Majority',fontsize = 20)

ax1.legend(numpoints=1, fontsize =17,bbox_to_anchor=(1.6, 1.2), fancybox=True, ncol=5, handletextpad=0.1,columnspacing=0.3)

plt.savefig('Fig5.pdf', bbox_inches = 'tight')
