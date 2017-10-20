"""
Generators for BA homophilic network with minority and majority 
and clustering similar to Holme-Kim algorithm.


written by: Fariba Karimi
Date: 01-07-2017
"""

import networkx as nx
from collections import defaultdict
import random
import bisect
import copy


def homophilic_barabasi_albert_graph(N, m , minority_fraction, similitude, p_clustering = 0.3 ):
    """Return homophilic random graph using BA preferential attachment model.

    A graph of n nodes is grown by attaching new nodes each with m
    edges that are preferentially attached to existing nodes with high
    degree. The connections are established by linking probability which 
    depends on the connectivity of sites and the similitude (similarities).
    similitude varies ranges from 0 to 1.

    Parameters
    ----------
    N : int
        Number of nodes
    m : int
        Number of edges to attach from a new node to existing nodes
    seed : int, optional
        Seed for random number generator (default=None).

    minority_fraction : float
        fraction of minorities in the network

    similitude: float
        value between 0 to 1. similarity between nodes. if nodes have same attribute
        their similitude (distance) is smaller.

    Returns
    -------
    G : Graph

    Notes
    -----
    The initialization is a graph with with m nodes and no edges.

    References
    ----------
    .. [1] A. L. Barabasi and R. Albert "Emergence of scaling in
       random networks", Science 286, pp 509-512, 1999.
    """
    if m < 1 or N < m:
        raise ("Network must have m>1 and m<n, m=%d,n=%d"%(m,n))


    G = nx.Graph()

    minority = int(minority_fraction * N)

    minority_nodes = random.sample(range(N),minority)
    node_attribute = {}
    for n in range(N):
        if n in minority_nodes:
            G.add_node(n , color = 'red')
            node_attribute[n] = 'minority'
        else:
            G.add_node(n , color = 'blue')
            node_attribute[n] = 'majority'



    #create homophilic distance ### faster to do it outside loop ###
    dist = defaultdict(int) #distance between nodes

    for n1 in range(N):
        n1_attr = node_attribute[n1]
        for n2 in range(N):
            n2_attr = node_attribute[n2]
            if n1_attr == n2_attr:
                dist[(n1,n2)] = 1 - similitude # higher similarity, lower distance
            else:
                dist[(n1,n2)] = similitude



    target_list=list(range(m))
    source = m #start with m nodes

    while source < N:

        targets = _pick_targets(G,source,target_list,dist,m)
        if targets == set([]): #if target list is empty
            continue
        # do one homophilic pref. attachment for new node
        target = targets.pop()
        #if targets != set(): #if the node does  find the neighbor
        G.add_edge(source, target)

        if targets == set([]): #if target list is empty
            continue
        count = 1
        while count < m:
            if random.random() < p_clustering:
                neighborhood=[nbr for nbr in G.neighbors(target) \
                               if not G.has_edge(source,nbr) \
                               and not nbr==source]
                if neighborhood: # if there is a neighbor without a link
                    nbr=random.choice(neighborhood)
                    G.add_edge(source,nbr) # add triangle
                    count=count+1
                    continue # go to top of while loop
            # else do preferential attachment step if above fails
            target=targets.pop()
            G.add_edge(source,target)
            count=count+1
        target_list.append(source)
        source += 1

    return G

def _pick_targets(G,source,target_list,dist,m):
    
    target_prob_dict = {}
    for target in target_list:
        target_prob = (1-dist[(source,target)])* (G.degree(target)+0.00001)
        target_prob_dict[target] = target_prob
        
    prob_sum = sum(target_prob_dict.values())

    targets = set()
    target_list_copy = copy.copy(target_list)
    count_looking = 0
    if prob_sum == 0:
        return targets #it returns an empty set

    while len(targets) < m:
        count_looking += 1
        if count_looking > len(G): # if node fails to find target
            break
        rand_num = random.random()
        cumsum = 0.0
        for k in target_list_copy:
            cumsum += float(target_prob_dict[k]) / prob_sum
            if rand_num < cumsum:
                targets.add(k)
                target_list_copy.remove(k)
                break
    return targets


if __name__ == '__main__':
    graph = homophilic_barabasi_albert_graph(N = 100, m = 2 , minority_fraction = 0.2, similitude= 0.8 , p_clustering = 0.3)
    #nx.write_gexf(graph,'graph_clustering.gexf')






