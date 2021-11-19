import networkx as nx
import itertools
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community import greedy_modularity_communities
from sklearn.cluster import SpectralClustering
import warnings
warnings.filterwarnings("ignore")

def find(lists, key):
    for i, list in enumerate(lists):
        if(key in list):
            return i

Graph1 = nx.read_gml("karate.gml", label = 'id')
adj_list = nx.to_numpy_array(Graph1)
k = 3
comp = girvan_newman(Graph1)
cluster = []
for communities in itertools.islice(comp, k):
    cluster = list(sorted(c) for c in communities)

num_clusters = len(cluster)
node_cluster_dict = {}
for x in Graph1.nodes():
    node_cluster_dict[x] = find(cluster, x)
rep1 = nx.Graph()
rep1.add_nodes_from(range(num_clusters))
rep1.add_edges_from(itertools.combinations(range(num_clusters), 2))

nx.set_edge_attributes(rep1, values = 0, name = 'weight')
for i, node in enumerate(Graph1.nodes()):
    for j, val in enumerate(adj_list[i]):
        if(node_cluster_dict[node] != node_cluster_dict[j+1]):

            rep1[node_cluster_dict[node]][node_cluster_dict[j+1]]["weight"] += val*0.5

print(rep1.edges(data = True))
nx.write_gml(rep1, "rep1.gml")

Graph2 = nx.read_weighted_edgelist("jazzz.net")
adj_list = nx.to_numpy_array(Graph2)
cluster = list(greedy_modularity_communities(Graph2))
num_clusters = len(cluster)

node_cluster_dict = {}
for x in Graph2.nodes():
    node_cluster_dict[x] = find(cluster, x)

rep2 = nx.Graph()
rep2.add_nodes_from(range(num_clusters))
rep2.add_edges_from(itertools.combinations(range(num_clusters), 2))
nx.set_edge_attributes(rep2, values = 0, name = 'weight')

for i, node in enumerate(Graph2.nodes()):
    for j, val in enumerate(adj_list[i]):
        if(node_cluster_dict[node] != node_cluster_dict[str(j+1)]):
            rep2[node_cluster_dict[node]][node_cluster_dict[str(j+1)]]["weight"] += val*0.5
print(rep2.edges(data = True))
nx.write_gml(rep2, "rep2.gml")

Graph3 = nx.read_gml("dolphins.gml", label = 'id')
adj_list = nx.to_numpy_matrix(Graph3)
sc = SpectralClustering(4, affinity='precomputed', n_init=100)
sc.fit(adj_list)
lg = list(Graph3)
num_clusters = len(set(sc.labels_))
cluster = []
for i in range(num_clusters):
    cluster.append([])
for i , val in enumerate(sc.labels_):
    cluster[val].append(lg[i])

node_cluster_dict = {}
for x in Graph3.nodes():
    node_cluster_dict[x] = find(cluster, x)

rep3 = nx.Graph()
rep3.add_nodes_from(range(num_clusters))
rep3.add_edges_from(itertools.combinations(range(num_clusters), 2))
nx.set_edge_attributes(rep3, values = 0, name = 'weight')
adj_list = adj_list.tolist()

for i, node in enumerate(Graph3.nodes()):
    for j, val in enumerate(adj_list[i]):
        if(node_cluster_dict[node] != node_cluster_dict[j]):

            rep3[node_cluster_dict[node]][node_cluster_dict[j]]["weight"] += val*0.5
print(rep3.edges(data = True))
nx.write_gml(rep3, "rep3.gml")
