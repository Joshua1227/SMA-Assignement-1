import networkx as nx

Graph1 = nx.read_gml("karate.gml", label = 'id')
print("Number of Nodes", Graph1.number_of_nodes())
print("Number of Edges", Graph1.number_of_edges())
print("Average Path Length",nx.average_shortest_path_length(Graph1))
print("Average Clustering Coefficient",nx.average_clustering(Graph1))


a_file = open("jazz.net", "r")

lines = a_file.readlines()
a_file.close()

new_file = open("jazzz.net", "w")
for line in lines:
    if (line != lines[0] and line != lines[1] and line != lines[2]):
        new_file.write(line)

new_file.close()

Graph2 = nx.read_weighted_edgelist("jazzz.net")
print("Number of Nodes", Graph2.number_of_nodes())
print("Number of Edges", Graph2.number_of_edges())
print("Average Path Length",nx.average_shortest_path_length(Graph2))
print("Average Clustering Coefficient",nx.average_clustering(Graph2))

Graph3 = nx.read_gml("dolphins.gml", label = 'id')
print("Number of Nodes", Graph3.number_of_nodes())
print("Number of Edges", Graph3.number_of_edges())
print("Average Path Length",nx.average_shortest_path_length(Graph3))
print("Average Clustering Coefficient",nx.average_clustering(Graph3))
