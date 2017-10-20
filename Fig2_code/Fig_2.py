import numpy as np 
import matplotlib.pyplot as plt 

plt.rcParams["font.family"] = "sans-serif"


fminor_list = [0.1, 0.2, 0.3, 0.4, 0.5]
fig = plt.figure(figsize = (10,6))
ha = [i/10. for i in range(11)]
hb = [1.-temp_h for temp_h in ha]
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.axvspan(0.5,1.0,color='lightgrey', edgecolor = 'lightgrey', alpha=0.5)
ax2.axvspan(0.0,0.5, color='lightgrey', edgecolor = 'lightgrey', alpha=0.5)
cmap = ['Goldenrod', 'coral', 'Pink', 'Firebrick', 'Red']
for fi in range(len(fminor_list)) : 
    fminor = fminor_list[fi]
   
    ''' Initial data'''
    Cdata = np.loadtxt('ctest_fa%s.txt' %(fminor))
    # data = np.loadtxt('neterr_fa%s.txt' %(fminor))
    fa = fminor 
    fb = 1.-fminor 
    
    minor_data = np.loadtxt('neterr_minor_fa%s.txt' %(fminor))
    major_data = np.loadtxt('neterr_major_fa%s.txt' %(fminor))
    c = Cdata[:,1]

    ''' Fig1(a) for the minority'''
    minorh = minor_data[:,0]
    minor_neterr = minor_data[:,1]
    minor_analytic_y = [2*((fa*ha[temp_c])/(ha[temp_c]*c[temp_c]+hb[temp_c]*(2.-c[temp_c])) )/fa for temp_c in range(len(c))]
    norm_minor_neterr = [(merr+fminor)/fminor for merr in minor_neterr]
    ax1.axhline(y=1, color = 'grey', ls = 'dashed')
    ax1.scatter(minorh, norm_minor_neterr, marker = 'o', edgecolor = 'black', s= 60,label = '$f_M=%s$' %fminor, facecolor = cmap[fi], zorder = 2)
    ax1.plot(minorh, minor_analytic_y, label = '',color = cmap[fi])
    ax1.set_xlabel(r'$h$', fontsize = 25)
    ax1.set_ylabel(r'$P_{group}$', fontsize = 25,labelpad = -5)
    ax1.xaxis.set_tick_params(labelsize=20)
    ax1.yaxis.set_tick_params(labelsize=20)
    ax1.set_xlim([0.0,1.0])
    ax1.set_ylim([0.0,10.0])
    

    '''Inset1 in Fig1 (a) for the minority''' 
    in1 = fig.add_axes([0.2, 0.55, 0.2, 0.3])
    inset_min_x = minorh[1:]
    inset_min_y = norm_minor_neterr[1:]
    inset_min_y_anal = minor_analytic_y[1:]
    in1.axhline(y=1, color = 'grey', ls = 'dashed')
    in1.xaxis.set_tick_params(labelsize=14)
    in1.yaxis.set_tick_params(labelsize=14)
    in1.scatter(inset_min_x, inset_min_y, edgecolor = 'black',s=30, marker = 'o', color = cmap[fi])
    in1.plot(inset_min_x, inset_min_y_anal, color = cmap[fi])
    in1.set_xlabel(r'$h$',fontsize = 16, labelpad = -1)
    in1.set_ylabel(r'$P_{group}$',fontsize =16, labelpad = -1)
    in1.set_xticklabels([0.1, '', 0.3, '', 0.5, '', 0.7, '', 0.9, '', 1.0])
    in1.set_xlim([0.1,1.0])
    in1.set_ylim([0.1, 10.0])
    in1.set_yscale('log')
    

    ''' Fig1(b) for the majority'''
    majorh = major_data[:,0]
    major_neterr = major_data[:,1]
    major_analytic_y = [((fa*hb[temp_c])/(ha[temp_c]*c[temp_c]+hb[temp_c]*(2.-c[temp_c])) + ((c[temp_c]/(2.-c[temp_c]))*(fb*hb[temp_c])/(hb[temp_c]*c[temp_c]+ha[temp_c]*(2.-c[temp_c]))))/ (fa) for temp_c in range(len(c))]
    norm_major_neterr = [(mjerr+fminor)/fminor for mjerr in major_neterr]
    ax2.axhline(y=1, color = 'grey', ls = 'dashed')
    ax2.scatter(majorh, norm_major_neterr, marker = 'o', s = 60, edgecolor = 'black', label = '$f_M=%s$' %fminor, color = cmap[fi], zorder = 2)
    ax2.plot(majorh, major_analytic_y, label = '',color = cmap[fi])
    ax2.set_xlabel(r'$h$', fontsize = 25)
    ax2.xaxis.set_tick_params(labelsize=20)
    ax2.yaxis.set_tick_params(labelsize=20)
    ax2.set_xlim(0.0,1.0)
    ax2.set_ylim(0.0,10.0)
    

    '''Inset1 in Fig1 (b) for the majority''' 
    in2 = fig.add_axes([0.68, 0.55, 0.2, 0.3])
    inset_maj_x = majorh[:10]
    inset_maj_y = norm_major_neterr[:10]
    inset_maj_y_anal = major_analytic_y[:10]
    in2.axhline(y=1, color = 'grey', ls = 'dashed')
    in2.xaxis.set_tick_params(labelsize=14)
    in2.yaxis.set_tick_params(labelsize=14)
    in2.scatter(inset_maj_x, inset_maj_y, edgecolor = 'black', marker = 'o',s=30, color = cmap[fi], zorder = 2)
    in2.plot(inset_maj_x, inset_maj_y_anal, color = cmap[fi])
    in2.set_xlabel(r'$h$',fontsize = 16, labelpad = -1)
    in2.set_ylabel(r'$P_{group}$',fontsize =16, labelpad = -1)
    in2.set_xticklabels([0.0, '', 0.2, '', 0.4, '', 0.6, '', 0.8, ''])
    in2.set_yscale('log')
    in2.set_xlim([0.0, 0.9])
    in2.set_ylim([0.1, 10.0])
    
''' Set labels ''' 
ax1.text(0.3,10.3, '(a) Minority',fontsize = 20)
ax2.text(0.3,10.3,'(b) Majority', fontsize = 20)

ax1.text(0.57,0.4, 'Filter Bubble',fontsize = 14,style='italic')
ax2.text(0.04,0.4, 'Majority Illusion',fontsize = 14,style='italic')

ax1.legend(scatterpoints=1, fontsize =17,bbox_to_anchor=(2.2, 1.23), fancybox=True, ncol=5, handletextpad=0.1,columnspacing=0.3)


fig.savefig('Fig2.pdf', bbox_inches = 'tight')

