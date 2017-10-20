import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import copy 
import math 

plt.rcParams["font.family"] = "sans-serif"
cmap = ['#d7191c', 'hotpink', '#ffffbf','#fdae61', '#a6d96a', '#1a9641']
num_data = 2
fig = plt.figure(figsize = (12,8))

data_types = ['brazil','pok','USF51','dblp','github','aps']
data_legend = ['Brazilian','POK','Facebook-USF51','DBLP','Github','APS']

hlist = [0.0,0.15, 0.4625, 0.56, 0.6, 0.74]
falist = [0.4,0.44,0.4166, 0.23, 0.05, 0.38]

for fi in range(num_data): 
    ax1 = fig.add_subplot(1,num_data,fi+1)
    for ti in range(len(data_types)): 
        
        tp = data_types[ti]
        if fi == 0 : # Fig3(a) for the minority's view  
            data = np.loadtxt('%snet_minor.txt' %(tp))
            ax1.set_ylabel(r'$P_{group}$', fontsize = 34, labelpad = 1.5)
            ax1.yaxis.set_tick_params(labelsize=28)
            ax1.yaxis.set_label_coords(-0.2,0.6)
            
            fa = falist[ti]
            y = (data[3])
            
            brzdata = np.loadtxt('brz_minor_fa0.4.txt')
            pokdata = np.loadtxt('pok_minor_fa0.44.txt')
            fbdata = np.loadtxt('usf51_minor_fa0.419.txt')
            dblpdata = np.loadtxt('dblp_minor_fa0.226.txt')
            gitdata = np.loadtxt('github_minor_fa0.05.txt')
            apsdata = np.loadtxt('aps_minor_fa0.38.txt')
            
            ''' perception bias from empirical data ''' 
            fbrz = brzdata[1]
            fpok = pokdata[1]
            ffb = fbdata[1]
            fdblp = dblpdata[1]
            fgit = gitdata[1]
            faps = apsdata[1]
            ''' STD erception bias from empirical data ''' 
            stdbrz = brzdata[2]
            stdpok = pokdata[2]
            stdfb = fbdata[2]
            stddblp = dblpdata[2]
            stdgit = gitdata[2]
            stdaps = apsdata[2]
            
            datafitlist=[fbrz, fpok, ffb, fdblp, fgit, faps ]
            datalist_minor = copy.copy(datafitlist)
            stdlist = [stdbrz, stdpok, stdfb, stddblp, stdgit, stdaps]
            
            '''asym. prediction of brazil'''
            brz_asym_minor = np.loadtxt('brazil_minor_fa0.4_asym.txt')
            brz_asym = brz_asym_minor[2]
            brz_asym_std = brz_asym_minor[3]
            
            '''asym. prediction of pok'''
            pok_asym_minor = np.loadtxt('pok_minor_fa0.44_asym.txt')
            pok_asym = pok_asym_minor[2]
            pok_asym_std = pok_asym_minor[3]
            
            '''asym. prediction of usf51'''
            usf_asym_minor = np.loadtxt('usf51_minor_fa0.42_asym.txt')
            usf_asym = usf_asym_minor[2]
            usf_asym_std = usf_asym_minor[3]
            
            '''asym. prediction of dblp'''
            dblp_asym_minor = np.loadtxt('dblp_minor_fa0.22_asym.txt')
            dblp_asym = dblp_asym_minor[2]
            dblp_asym_std = dblp_asym_minor[3]
            
            '''asym. prediction of Github'''
            github_asym_minor = np.loadtxt('github_minor_fa0.06_asym.txt')
            github_asym = github_asym_minor[2]
            github_asym_std = github_asym_minor[3]
            
            '''asym. prediction of aps'''
            aps_asym_minor = np.loadtxt('aps_minor_fa0.37_asym.txt')
            aps_asym = aps_asym_minor[2]
            aps_asym_std = aps_asym_minor[3]
            
            
            
        elif fi == 1 : # Fig3(b) for the majority's view  
            data = np.loadtxt('%snet_major.txt' %(tp))
            ax1.yaxis.set_tick_params(labelsize=28)
            ax1.yaxis.set_label_coords(-0.08,0.6)
            
            fa = falist[ti]
            y = (data[3])

            brzdata = np.loadtxt('brz_major_fa0.4.txt')
            pokdata = np.loadtxt('pok_major_fa0.44.txt')
            fbdata = np.loadtxt('usf51_major_fa0.419.txt')
            dblpdata = np.loadtxt('dblp_major_fa0.226.txt')
            gitdata = np.loadtxt('github_major_fa0.05.txt')
            apsdata = np.loadtxt('aps_major_fa0.38.txt')

            fbrz = brzdata[1]
            fpok = pokdata[1]
            ffb = fbdata[1]
            fdblp = dblpdata[1]
            fgit = gitdata[1]
            faps = apsdata[1]
            
            stdbrz = brzdata[2]
            stdpok = pokdata[2]
            stdfb = fbdata[2]
            stddblp = dblpdata[2]
            stdgit = gitdata[2]
            stdaps = apsdata[2]
            
            datafitlist=[fbrz, fpok, ffb,fdblp,fgit, faps ]
            datalist_major = copy.copy(datafitlist)
            stdlist = [stdbrz, stdpok, stdfb, stddblp, stdgit, stdaps]
            
            '''asym. prediction of brazil'''
            brz_asym_major = np.loadtxt('brazil_major_fa0.4_asym.txt')
            brz_asym = brz_asym_major[2]
            brz_asym_std = brz_asym_major[3]
            '''asym. prediction of pok'''
            pok_asym_major = np.loadtxt('pok_major_fa0.44_asym.txt')
            pok_asym = pok_asym_major[2]
            pok_asym_std = pok_asym_major[3]
            '''asym. prediction of usf51'''
            usf_asym_major = np.loadtxt('usf51_major_fa0.42_asym.txt')
            usf_asym = usf_asym_major[2]
            usf_asym_std = usf_asym_major[3]
            '''asym. prediction of dblp'''
            dblp_asym_major = np.loadtxt('dblp_major_fa0.22_asym.txt')
            dblp_asym = dblp_asym_major[2]
            dblp_asym_std = dblp_asym_major[3]
            '''asym. prediction of Github'''
            github_asym_major = np.loadtxt('github_major_fa0.06_asym.txt')
            github_asym = github_asym_major[2]
            github_asym_std = github_asym_major[3]
            '''asym. prediction of aps'''
            aps_asym_major = np.loadtxt('aps_major_fa0.37_asym.txt')
            aps_asym = aps_asym_major[2]
            aps_asym_std = aps_asym_major[3]
            
        ax1.set_ylim([-0.05, 3])
        ax1.set_xlim([-0.05,1.0])        
        ax1.axhline(y=1, color = 'grey', ls = 'dashed')        
        ax1.plot(hlist[ti],datafitlist[ti],marker = '^',markersize = 18, mew = 2, linestyle = '-',color = cmap[ti],mfc = 'none', markeredgecolor = cmap[ti], label = '%s-model' %(data_legend[ti]))
        
        ax1.plot(0.0, brz_asym,  markersize = 18, marker = 's', mfc = 'none', markeredgecolor ='#d7191c', color = '#d7191c')
        ax1.plot(0.15, pok_asym,  markersize = 18, marker = 's',mfc = 'none',  mec = 'hotpink', color = 'hotpink' )
        ax1.plot(0.47, usf_asym,  markersize = 18, marker = 's', mfc = 'none',  mec ='#ffffbf', color = '#ffffbf')
        ax1.plot(0.56, dblp_asym,  markersize = 18, marker = 's', mfc = 'none',  mec = '#fdae61')
        ax1.plot(0.6, github_asym,  markersize = 18, marker = 's', mfc = 'none',  mec = '#a6d96a', color = '#a6d96a')
        ax1.plot(0.74, aps_asym,  markersize = 18, marker = 's', mfc = 'none',  mec = '#1a9641', color = '#1a9641')
        
        ax1.errorbar(0.0, brz_asym, yerr = brz_asym_std, markersize = 18, marker = 's', mfc = 'none',  mec ='#d7191c',mew = 2, color ='#d7191c' )
        ax1.errorbar(0.15, pok_asym, yerr = pok_asym_std, markersize = 18, marker = 's', mfc = 'none', mec = 'hotpink',mew = 2, color = 'hotpink')
        ax1.errorbar(0.47, usf_asym, yerr = usf_asym_std, markersize = 18, marker = 's', mfc = 'none',  mec = '#ffffbf', mew = 2,color = '#ffffbf')
        ax1.errorbar(0.56, dblp_asym, yerr = dblp_asym_std, markersize = 18, marker = 's', mfc = 'none', mec = '#fdae61', mew = 2, color = '#fdae61')
        ax1.errorbar(0.6, github_asym, yerr = github_asym_std, markersize = 18, marker = 's', mfc = 'none',  mec = '#a6d96a', mew = 2, color = '#a6d96a')
        ax1.errorbar(0.74, aps_asym, yerr = aps_asym_std, markersize = 18, marker = 's', mfc = 'none',  mec = '#1a9641',mew = 2, color = '#1a9641')
        ax1.xaxis.set_tick_params(labelsize=28)
        ax1.set_xlabel(r'$h$',fontsize = 34)
        ax1.plot(hlist[ti],y,marker = 'x',markersize = 15, mfc = cmap[ti], mec ='black', mew = 2, label = '%s' %(data_legend[ti]))
        
        brazil_color = mpatches.Patch(color='#d7191c', label='Brazil')
        pok_color = mpatches.Patch(color='hotpink', label='POK')
        USF51_color = mpatches.Patch(color='#ffffbf', label='USF51')
        dblp_color = mpatches.Patch(color='#fdae61', label='DBLP')
        github_color = mpatches.Patch(color='#a6d96a', label='Github')
        aps_color = mpatches.Patch(color='#1a9641', label='APS')
        circle = mlines.Line2D([], [], mfc = 'none', mec = 'black', marker='x', markersize=15, ls = 'none', label='empirical')
        triangle = mlines.Line2D([], [], mfc = 'none', mec = 'black', marker='^', markersize=15, ls = 'none', label=r'Symmetric $h$')
        square = mlines.Line2D([], [], mfc = 'none', mec = 'black', marker='s', markersize=15, ls = 'none', label=r'Asymmetric $h$')

        if fi == 1 : 
            ax1.legend(handles=[brazil_color, pok_color, USF51_color, dblp_color, github_color, aps_color, circle, triangle, square], loc = (1.01, 0.52),fontsize = 20,frameon = False, numpoints = 1,labelspacing = 0.2, handletextpad=0.2)
            '''Inset1''' 
            in1 = fig.add_axes([0.7, 0.62, 0.18, 0.25])
            inset_x = [0.0, 0.15, 0.47, 0.56, 0.6, 0.74]
            inset_y = [abs(datalist_minor[i]-datalist_major[i]) for i in range(6)]
            in1.xaxis.set_tick_params(labelsize=15)
            in1.yaxis.set_tick_params(labelsize=15)
            in1.plot(inset_x[ti], inset_y[ti], marker = 'o', color = cmap[ti])
            in1.set_xlabel(r'$h$',fontsize = 20, labelpad = 1)
            in1.set_ylabel('Perception gap',fontsize =18, labelpad = 2)
            in1.set_ylim([0.0,2.6])
            in1.set_xlim([-0.05,1.0])
        x = ti+1
fig.text(0.22, 0.92,'(a) Minority', fontsize = 25)
fig.text(0.63, 0.92, '(b) Majority', fontsize = 25)
plt.savefig('Fig3.pdf', bbox_inches = 'tight')
