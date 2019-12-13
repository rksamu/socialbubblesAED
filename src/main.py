import networkx as nx
import matplotlib.pyplot as plt
from gerar_grafo_social import gerar_grafo_social






# Abrir visualizacao interativa com o matplotlib
G = gerar_grafo_social(12, 10)
nx.draw(G, with_labels = True, font_weight='bold')
plt.show()