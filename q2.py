#girvan newman clustering
import itertools
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community import greedy_modularity_communities
import numpy as np
from sklearn.cluster import SpectralClustering
import networkx.algorithms.community as nx_comm
import time
import warnings
warnings.filterwarnings("ignore")

max_count = 5

#Read graph information frim files and load graphs
Graph1 = nx.read_gml("karate.gml", label = 'id')
Graph2 = nx.read_weighted_edgelist("jazzz.net")
Graph3 = nx.read_gml("dolphins.gml", label = 'id')
#initialize time values
times = [[0,0,0],[0,0,0],[0,0,0]]
for t in range(max_count):                      #run algorithm 5 times to get average time data
    print("_________GRAPH1 = KARATE_____________")
    print("___________GIRVAN_NEWMAN_____________")
    k = 3
    start_time = time.time()
    comp = girvan_newman(Graph1)
    times[0][0] +=  time.time()-start_time
    print("Girvan Newman Time",times[0][0]/max_count)
    cluster = []
    for communities in itertools.islice(comp, k):
        #print(tuple(sorted(c) for c in communities))
        cluster = list(sorted(c) for c in communities)
        #print(cluster)
    print(len(cluster))
    print(nx_comm.modularity(Graph1, cluster))

    print("______________MOD_MAX________________")
    start_time = time.time()
    cluster = list(greedy_modularity_communities(Graph1))
    times[0][1] += time.time()-start_time
    print("Modularity Maximization Time",times[0][1]/max_count)
    print(len(cluster))
    print(nx_comm.modularity(Graph1, cluster))

    print("____________SPECTRAL_________________")
    start_time = time.time()
    adj_mat = nx.to_numpy_matrix(Graph1)
    sc = SpectralClustering(3, affinity='precomputed', n_init=100)
    sc.fit(adj_mat)
    times[0][2] += time.time()-start_time
    print("Spectral Clustering Time",times[0][2]/max_count)

    num = len(set(sc.labels_))
    print(num)
    cluster = []
    for i in range(num):
        cluster.append([])
    for i , val in enumerate(sc.labels_):
        cluster[val].append(i+1)

    print(nx_comm.modularity(Graph1, cluster))
    print("___________GRAPH2 = JAZZ_____________")
    print("___________GIRVAN_NEWMAN_____________")
    k=5
    start_time = time.time()
    comp = girvan_newman(Graph2)
    times[1][0] += time.time()-start_time
    print("Girvan Newman Time",times[1][0]/max_count)
    for communities in itertools.islice(comp, k):
        cluster = list(sorted(c) for c in communities)

    print(len(cluster))
    print(nx_comm.modularity(Graph2, cluster))

    print("______________MOD_MAX________________")
    start_time = time.time()
    cluster = list(greedy_modularity_communities(Graph2))
    times[1][1] += time.time()-start_time
    print("Modularity Maximization Time",times[1][1]/max_count)
    print(len(cluster))
    print(nx_comm.modularity(Graph2, cluster))

    print("____________SPECTRAL_________________")
    start_time = time.time()
    adj_mat = nx.to_numpy_matrix(Graph2)
    sc = SpectralClustering(4, affinity='precomputed', n_init=100)
    sc.fit(adj_mat)
    times[1][2] += time.time()-start_time
    print("Spectral Clustering Time",times[1][2]/max_count)
    lg = list(Graph2)
    num = len(set(sc.labels_))
    print(num)
    cluster = []
    for i in range(num):
        cluster.append([])
    for i , val in enumerate(sc.labels_):
        cluster[val].append(lg[i])

    print(nx_comm.modularity(Graph2, cluster))

    print("__________GRAPH3 = DOLPHINS___________")
    print("___________GIRVAN_NEWMAN_____________")
    k=4
    start_time = time.time()
    comp = girvan_newman(Graph3)
    times[2][0] += time.time()-start_time
    print("Girvan Newman Time",times[2][0]/max_count)
    for communities in itertools.islice(comp, k):
        cluster = list(sorted(c) for c in communities)

    print(len(cluster))
    print(nx_comm.modularity(Graph3, cluster))

    print("______________MOD_MAX________________")
    start_time = time.time()
    cluster = list(greedy_modularity_communities(Graph3))
    times[2][1] += time.time()-start_time
    print("Modularity Maximization Time",times[2][1]/max_count)
    print(len(cluster))
    print(nx_comm.modularity(Graph3, cluster))

    print("____________SPECTRAL_________________")
    start_time = time.time()
    adj_mat = nx.to_numpy_matrix(Graph3)
    sc = SpectralClustering(4, affinity='precomputed', n_init=100)
    sc.fit(adj_mat)
    times[2][2] += time.time()-start_time
    print("Spectral Clustering Time",times[2][2]/max_count)
    lg = list(Graph3)
    num = len(set(sc.labels_))
    print(num)
    cluster = []
    for i in range(num):
        cluster.append([])
    for i , val in enumerate(sc.labels_):
        cluster[val].append(lg[i])
    print(nx_comm.modularity(Graph3, cluster))
