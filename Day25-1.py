import networkx as nx
from networkx.algorithms import community
import math

G = nx.Graph()

with open("input.txt") as f:
	for line in f.readlines():
		n, tmp = line.split(':')
		nb = tmp.strip().split()
		for item in nb:
			G.add_edge(n, item)

# Detect communities using the Louvain method
communities = community.greedy_modularity_communities(G)

# Map nodes to their respective communities
community_map = {node: idx for idx, nodes in enumerate(communities) for node in nodes}

# Find edges that connect different clusters (inter-cluster edges)
inter_cluster_edges = [(u, v) for u, v in G.edges() if community_map[u] != community_map[v]]

for item in inter_cluster_edges:
	print(item)
	# cut_value, partition = nx.minimum_cut(G, item[0], item[1])
	cut_edges = nx.minimum_edge_cut(G, s=item[0], t=item[1])
	if len(cut_edges) == 3:
		G.remove_edges_from(cut_edges)
		break
clusters = list(nx.connected_components(G))
result1 = []
for c in clusters:
	result1.append(len(c))
print("Result 1:", math.prod(result1))
