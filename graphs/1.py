import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# добавление ребер в граф
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(1, 5)
G.add_edge(3, 5)
# визуализация графа
nx.draw(G, with_labels=True)
plt.show()
