import networkx as nx
import matplotlib.pyplot as plt

print("test")

# Criar grafo
G = nx.Graph()

# Add vertices
G.add_nodes_from(['Lucas', 'Maria', 'Pedro', 'Pedro', 'Ana', 'Renato'])
# Note que o pedro so eh adicionado uma vez.

# Add arestas
G.add_edges_from([('Lucas', 'Maria'), ('Pedro', 'Maria'), ('Lucas', 'Pedro'), ('Maria', 'Renato')])

# Abrir visualizacao interativa com o matplotlib
nx.draw(G, with_labels=True)
plt.show()