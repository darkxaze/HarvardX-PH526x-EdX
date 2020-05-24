# import speciified statements
import numpy as np
import pandas as pd
import networkx as nx 
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

# create graph
G = nx.Graph()

# add nodes in dif ways
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u","v"])
print("nodes in Graph G", G.nodes())

# add edges in dif ways
G.add_edge(1,2)
G.add_edge("u","v")
G.add_edges_from([(1,3),(1,4),(1,5),(1,6)])
# can even add edge if node doesn't exist
G.add_edge("u","w")
print("edges in Graph G", G.edges())

# divider
print("")

# remove nodes from graph
G.remove_node(2)
print("nodes in Graph G after deleting node #2", G.nodes())
G.remove_nodes_from([4,5])
print("deleted nodes #4 and #5", G.nodes())

# remove edges from graph
G.remove_edge(1,3)
print("edges in Graph G after deleting one between #1 and #3", G.edges())
G.remove_edges_from([(1,2),("u","w")])
print("edges in Graph G after deleting #1:#2and #u:#w", G.edges())

# divider
print("")

# print number of nodes and edges
print("number of nodes", G.number_of_nodes())
print("number of edges", G.number_of_edges())

# divider
print("")

G = nx.karate_club_graph()
print("grid", nx.draw(G, with_labels = True, node_color = "lightblue", edge_color = "gray"))
# commented code as to not save twice
#  plt.savefig("karate_graph.pdf")

print("degrees for each node", G.degree())
# same things
print("degree of 33:", G.degree()[33])
print("degree of 33:", G.degree(33))

# print number of nodes and edges
print("number of nodes", G.number_of_nodes())
print("number of edges", G.number_of_edges())

# check if two are exactly same
print(G.degree(0) is G.degree()[0])

#divider
print("")

print("bernoull dist with prob 0.2:", bernoulli.rvs(p=0.2))

N = 20
p = 0.2 

def er_graph(N,p):
    """Generate and er_graph"""
    # create empty graph
    # add all N nodes
    # loop over all pairs of nodes
        # add an edge with prob p
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1<node2 and bernoulli.rvs(p=p):
                G.add_edge(node1,node2)
    # print number of nodes and edges
    print("number of nodes", G.number_of_nodes())
    print("number of edges", G.number_of_edges()) 

    # draw graph
    # nx.draw(G)
    return G
# commented code as to not save twice
# plt.savefig("Erdos_Renyl_graph*updated.pdf")
# nx.draw(er_graph(50,0.08), node_size = 40, node_color = "lightgreen")
# plt.savefig("FinalErdosRenylGraph.pdf")
def plot_deg_dist(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree Dist")
G = er_graph(500,0.08)
plot_deg_dist(G)
# commented code as to not save twice
# plt.savefig("hist1.pdf")
# plt.savefig("hist1*.pdf")

G1 = er_graph(500,0.08)
plot_deg_dist(G1)
G2 = er_graph(500,0.08)
plot_deg_dist(G2)
G3 = er_graph(500,0.08)
plot_deg_dist(G3)
# commented code as to not save twice
# plt.savefig("hist_3graphs.pdf")

A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("number of nodes", G.number_of_nodes())
    print("number of edges", G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))
#divider
# print("")
# print("basic net stats G1:", basic_net_stats(G1))
# print("")
# print("basic net stats G2:", basic_net_stats(G2))

# plot_deg_dist(G1)
# plot_deg_dist(G2)

# commented code as to not save twice
# plt.savefig("village_hist.pdf")

# gen = nx.connected_component_subgraphs(G1)
# g = gen.__next__()
# # print(type(g))
# print("number of nodes in g:", nx.number_of_nodes(g))
# print(len(g))