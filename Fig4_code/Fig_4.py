
import numpy as np 
import matplotlib.pyplot as plt 

plt.rcParams["font.family"] = "sans-serif"
cmap = ['#d7191c', '#fdae61', '#ffffbf', '#a6d96a', 'mediumseagreen', 'turquoise', 'teal','olive']
data_types = ['brz', 'pok','usf','dblp','github','aps']

N = [16730, 29341, 6253, 1853, 280200, 120338]
Ns = [1000, 1000, 1000, 400, 100, 1000]
fminor_list = [0.4, 0.44, 0.419, 0.23, 0.05, 0.38]
fig = plt.figure(figsize = (13,8))
num_types = len(data_types)
fig_ind = 0 

# common_path = '/Users/leeeun/Dropbox/project2017/Homophily/New_after0510/empirical/data_hk/data_hk_results/datahk_logresults'
# predict_path = '/Users/leeeun/Dropbox/project2017/Homophily/New_after0510/empirical/data_predict_hk/asym_hk/hk_asymresults/datahkpredict_log'
for ti in range(num_types) : 
    
    tp = data_types[ti]
    fig_col = ti/4+1 #hang
    fig_row = ti%4+1 #yeol     
    ax1 = fig.add_subplot(2,3, ti+1)
       
    '''h(k) of dataset'''
    
    minor_data = np.loadtxt('%s_minorhk_Log.txt' %(tp)) 
    major_data = np.loadtxt('%s_majorhk_Log.txt' %(tp))
    
    minor_cval = 'orange'
    major_cval = 'deepskyblue'
    
    minor_x = minor_data[:,0]
    minor_y = minor_data[:,1]
    
    major_x = major_data[:,0]
    major_y = major_data[:,1]
    
    ax1.plot(minor_x,minor_y, marker = 'o', color = minor_cval, label = 'Minority')
    ax1.plot(major_x,major_y, marker = 'o', color = major_cval, label = 'Majority')
    
    '''predicted h(k) of dataset'''
    
    minor_pre_data = np.loadtxt('%s_minor_asymhk_pre_Log.txt' %(tp)) # we need to do the logbinning 
    major_pre_data = np.loadtxt('%s_major_asymhk_pre_Log.txt' %(tp))
    
    minor_cval = 'orange'
    major_cval = 'deepskyblue'
    
    minor_pre_x = minor_pre_data[:,0]
    minor_pre_y = minor_pre_data[:,1]
    
    major_pre_x = major_pre_data[:,0]
    major_pre_y = major_pre_data[:,1]

    ax1.plot(minor_pre_x,minor_pre_y, color = minor_cval, ls = 'dashed', label = 'Minority-model')
    ax1.plot(major_pre_x,major_pre_y, color = major_cval, ls = 'dashed', label = 'Majority-model')
    ax1.yaxis.set_tick_params(labelsize=23)
    ax1.xaxis.set_tick_params(labelsize=23)
    ax1.set_xscale('log')
    ax1.set_xlim([2,max(max(major_x), max(minor_x))])
    ax1.set_ylim([-0.1,3.0])
    
    '''y-label'''
    if ti == 0:
        ax1.set_ylabel(r'$P_{indv.}$', fontsize = 34)
    elif ti == 3 : 
        ax1.set_ylabel(r'$P_{indv.}$', fontsize = 34)
    ''' legend ''' 
    if ti == 2: 
        ax1.legend(frameon = False, fontsize = 15, loc = (0.1,0.6), numpoints = 1,labelspacing = 0.3,handletextpad=0.1)
    '''x-label'''
    if ti == 4:
        ax1.set_xlabel(r'$k$', fontsize = 34,labelpad = -2)
    '''plots'''
    if ti == 0 : 
        ax1.text(7.0,3.3,r'(a) Brazil', fontsize = 20)
        ax1.set_title('(High heterophily)',fontsize = 15)
        ax1.axhline(y=1, color = 'grey', ls = 'dashed')
        ax1.set_xlabel(r'$k$', fontsize = 34,labelpad = -5)
    elif ti == 1 : 
        ax1.text(10.0,3.3,r'(b) POK', fontsize = 20)
        ax1.set_title('(Medium heterophily)',fontsize = 14)
        ax1.axhline(y=1, color = 'grey', ls = 'dashed')
        ax1.set_xlabel(r'$k$', fontsize = 34,labelpad = -5)
    elif ti == 2 : 
        ax1.text(8,3.3,r'(c) USF51', fontsize = 20)
        ax1.set_title('(Low heterophily)',fontsize = 14)
        ax1.axhline(y=1, color = 'grey', ls = 'dashed')
        ax1.set_xlabel(r'$k$', fontsize = 34,labelpad = -5)
    elif ti == 3 : 
        ax1.text(7.0,3.3,r'(d) DBLP',fontsize = 20)
        ax1.set_title('(Low homophily)',fontsize = 14)
        ax1.axhline(y=1, color = 'grey', ls = 'dashed')
        ax1.set_xlabel(r'$k$', fontsize = 34,labelpad = -4)
    elif ti == 4 : 
        ax1.text(6.0,3.3,r'(e) Github',fontsize = 20)
        ax1.set_title('(Medium homophily)',fontsize = 14)
        ax1.axhline(y=1, color = 'grey', ls = 'dashed')
        ax1.set_xlabel(r'$k$', fontsize = 34,labelpad = -2)
    elif ti == 5 : 
        ax1.set_title('(High homophily)',fontsize = 14)
        ax1.text(5.0,3.3,'(f) APS',fontsize = 20)
        ax1.axhline(y=1, color = 'grey', ls = 'dashed')
        ax1.set_xlabel(r'$k$', fontsize = 34,labelpad = -2)
        
plt.subplots_adjust(top = 0.99, bottom=0.01, hspace=0.4, wspace=0.3)   
plt.savefig('Fig4.pdf', bbox_inches = 'tight')
        
   