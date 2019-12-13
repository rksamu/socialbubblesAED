import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt, ceil

def visualizar(grafos):
    """
    Abre uma visualizacao interativa da lista de grafos fornecida, com o matplotlib
    """
    # TODO: Colorir os nós de acordo com a opinião
    # TODO: Opção de fornecer um subgrafo para destacar

    # Determinar a quantidade de plots necessaria
    qtd_plots = ceil(sqrt(len(grafos)))

    for i in range(len(grafos)):
        grafo = grafos[i]
        # Lista de textos dos nós
        labels_dict = { node_name: "{}\n{:.2f}".format(node_name, grafo.nodes[node_name]["opinion"])
                        for node_name in grafo.nodes }
        
        plt.subplot(qtd_plots, qtd_plots, i+1)

        nx.draw(grafo, with_labels = True, labels=labels_dict,
                node_color= '#aaaaff',
                font_size = 9, font_weight="bold")

    plt.show()