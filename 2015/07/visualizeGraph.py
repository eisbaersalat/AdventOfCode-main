import networkx as nx
import matplotlib.pyplot as plt

outputs = []
inputs = []

with open("2015/07/input.txt", encoding="utf-8") as file:
    for line in file:
        s, t = line.rstrip().split(" -> ")
        outputs.append(t)
        inputs.append(s.split(" "))


G = nx.Graph()

for idx in range(len(outputs)):

    if len(inputs[idx]) == 1:
        G.add_edge(inputs[idx][0], outputs[idx])

    elif len(inputs[idx]) == 2:
        G.add_edge(inputs[idx][1], outputs[idx])

    elif len(inputs[idx]) == 2:
        G.add_edge(inputs[idx][0], outputs[idx])
        G.add_edge(inputs[idx][2], outputs[idx])

nx.draw(G, with_labels=True)
plt.show()