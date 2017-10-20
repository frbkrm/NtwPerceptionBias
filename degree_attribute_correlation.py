
# coding: utf-8

# In[34]:

import networkx as nx
from collections import defaultdict,Counter
import matplotlib
import matplotlib.pyplot as plt
import random
import bisect
import numpy as np
import copy
import math

from generate_homophilic_graph_symmetric import homophilic_barabasi_albert_graph


# In[35]:

#get_ipython().magic(u'matplotlib inline')

def analytical_prediction(similitude_param,min_fraction):
    # group a is the minority

    f = min_fraction
    h = similitude_param


    A = -(2*h-1)**2 
    B  = (2*h-1)*(2*f*h + 5*h - 3) 
    C = -2*(4*f*h**2 - 2*f*h + 3*h**2 -4*h + 1) 
    D = -4*f*h*(1-h) 

    p = [A,B,C,D]
    print np.roots(p)
    for r in np.roots(p):
        if r> 0 and r<2:
            ca = r

    h_aa = h_bb = h
    h_ba = h_ab = 1- h
    fb = 1 - f
    b_a = float(f*h_aa)/ (h_aa*ca + h_ab * (2 - ca)) + float(fb*h_ba)/(h_ba*ca + h_bb*(2-ca))

    #b_b = float(fb*h_bb)/ (h_ba*ca + h_bb * (2 - ca)) + float(fa*h_ab)/(h_aa*ca + h_ab*(2-ca))
    print 'ca',ca

    return ca

# In[36]:



def check_correlation(N , m , min_fraction , similitude  , fig_name ):
    
    x_list = [] ; y_list = [] ; z_list = [] ; y_list_prediction = []

    itter_num = 1
    for i in range(itter_num):
        G = homophilic_barabasi_albert_graph(N,m,min_fraction,similitude)
        #degree_sequence_min =sorted([d for n,d in G.degree().iteritems() if G.node[n]['color']=='red' ], reverse=True) # degree sequence
        #degree_sequence_maj =sorted([d for n,d in G.degree().iteritems() if G.node[n]['color']=='blue' ], reverse=True) # degree sequence

        degree_sequence_all =sorted([d for n,d in G.degree().iteritems()  ], reverse=True) # degree sequence

        degree_attr_dict = defaultdict(list)
        degree_correlation_dict = defaultdict(list)
        # let's calculate deg-deg correlation
        #the probability to find nodes of degrees k and k′ at either end of a randomly chosen edge in an undirected network
        for n in G.nodes():
            n_k = G.degree(n)
            degree_attr_dict[n_k].append(G.node[n]['color'])
            for neibor in G.neighbors(n):
                n_n_k = G.degree(neibor)
                degree_correlation_dict[n_k].append(n_n_k)


        for k in degree_correlation_dict.keys():
            if k == 8:
                for k_prime in degree_correlation_dict[k]:
                    p_k_prime = float(degree_correlation_dict[k].count(k_prime)) / len(degree_correlation_dict[k])

                    #x_list.append(k_prime)

                    #y_list.append(p_k_prime)
    ca,beta_a = analytical_prediction(similitude,min_fraction)

    for deg in degree_attr_dict.keys():
        x_list.append(deg)
        prob = float(degree_attr_dict[deg].count('red')) / N
        y_list.append(prob)
        deg_prob = deg**(-(1/beta_a + 1))
        y_list_prediction.append( deg_prob)

    plt.scatter(x_list,y_list)
    plt.scatter(x_list,y_list_prediction,color = 'red')

    print 'ca',ca
    rho_deg_attr = min_fraction*m*(ca - 2)

    degree_deviation = np.std(list(G.degree().values()))
    for kprime in x_list:
        p_xprime_kprime_approximate = min_fraction + rho_deg_attr/(degree_deviation**2) * (kprime - 4)
        z_list.append(p_xprime_kprime_approximate)
    #plt.scatter(x_list,z_list,color = 'r')


    plt.ylim(10**(-4),1)
    plt.xlim(1,10**(2))

    plt.yscale('log')
    plt.xscale('log')
    plt.legend(loc='upper right')
    plt.rc('legend',**{'fontsize':14})
    #plt.show()

    plt.xlabel('degree')
    plt.ylabel('probability of being minority attribute')

    plt.savefig('degree_attr_correlation_min_fract_%s_simil_%s.png'%(min_fraction,similitude))







# In[54]:

#similitude_list = [0.005,0.2,0.5,0.8,0.999,1.0]
similitude_list =[1]
eun_measure = []
Hang_measure = []
sim_list = []

for similitude in np.arange(0,1.05,0.05):
    N = 3000 ; m = 2 ; min_fraction = 0.2
    ca = analytical_prediction( similitude  , min_fraction)
    eun_measure.append((2*min_fraction*similitude)/(similitude*ca + (1 - similitude)*(2-ca)))
    Hang_measure.append((min_fraction*similitude)/(min_fraction*similitude+(1- min_fraction)*(1 - similitude)))
    sim_list.append(similitude)

plt.plot(sim_list,np.array(eun_measure)/min_fraction, label = 'Eun measure')

plt.plot(sim_list,np.array(Hang_measure)/min_fraction, label = 'Hang measure')

plt.title('min fraction = %s'%min_fraction)
plt.legend(loc='upper left')
plt.savefig('compare_calculations.png')


    #print 'plot similitude',similitude




