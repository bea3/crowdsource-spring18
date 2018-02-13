import networkx as nx
import community
import networkx.algorithms as nx_alg
import matplotlib.pyplot as plt
import csv
import random

# Read in CSV and turn into dictionary
tweets = []
with open('prochoice.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    reader.next()
    for row in reader:
        tweet = {}
        tweet["from"] = row[0]
        tweet["to"] = row[1]
        tweet["text"] = row[2]
        tweets.append(tweet)

# Create graph
G = nx.Graph()
G.add_node("N/A")
users = []
for entry in tweets:
    from_user = entry["from"]
    to_user = entry["to"]
    if from_user not in users:
        G.add_node(from_user)
        users.append(from_user)
    if to_user != "N/A" and to_user not in users:
        G.add_node(to_user)
        users.append(to_user)
        G.add_edge(from_user, to_user)
    # else:
    #     G.add_edge(from_user, "N/A")
# nx.draw(G, pos=nx.spring_layout(G), k=0.15, iterations=20, with_labels=True)
# plt.show(G)

# uses Louvain method
# http://python-louvain.readthedocs.io/en/latest/api.html
partition = community.best_partition(G)
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0
used_colors = []
for com in set(partition.values()) :
    count += 1
    list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
    r = lambda: random.randint(0, 255)
    node_color = '#%02X%02X%02X' % (r(),r(),r())
    while node_color in used_colors:
        r = lambda: random.randint(0, 255)
        node_color = '#%02X%02X%02X' % (r(), r(), r())
    used_colors.append(node_color)
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20, node_color=node_color)
nx.draw_networkx_edges(G, pos, alpha=0.5)
# nx.draw_networkx_labels(G, pos, font_size=8)

# Calculate degree
degree_scores = nx_alg.degree_centrality(G)
sorted_degrees = sorted(degree_scores.iteritems(), key=lambda (k,v): (v,k), reverse=True)
print("Users with the Top 10 degree scores")
i = 1
for score in sorted_degrees:
    if i <= 10:
        print(score[0] + " with score " + str(score[1]))
        i += 1
    else:
        break
print

# Calculate betweenness
scores = nx_alg.betweenness_centrality(G)
sorted_scores = sorted(scores.iteritems(), key=lambda (k,v): (v,k), reverse=True)
print("Users with the Top 10 Betweenness scores")
i = 1
for score in sorted_scores:
    if i <= 10:
        print(score[0] + " with score " + str(score[1]))
        i += 1
    else:
        break
print

# Calculate closeness
scores = nx_alg.closeness_centrality(G)
sorted_scores = sorted(scores.iteritems(), key=lambda (k,v): (v,k), reverse=True)
print("Users with the Top 10 Closeness scores")
i = 1
for score in sorted_scores:
    if i <= 10:
        print(score[0] + " with score " + str(score[1]))
        i += 1
    else:
        break
print

# Calculate closeness
scores = nx_alg.eigenvector_centrality_numpy(G)
sorted_scores = sorted(scores.iteritems(), key=lambda (k,v): (v,k), reverse=True)
print("Users with the Top 10 Eigenvector scores")
i = 1
for score in sorted_scores:
    if i <= 10:
        print(score[0] + " with score " + str(score[1]))
        i += 1
    else:
        break
print

# Get diameter
if not nx_alg.is_connected(G):
    gc = max(nx.connected_component_subgraphs(G), key=len)
    print ("Diameter: " + str(nx_alg.diameter(gc)))
else:
    print ("Diameter: " + str(nx_alg.diameter(G)))

plt.show()
