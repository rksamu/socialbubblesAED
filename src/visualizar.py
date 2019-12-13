import networkx as nx
import matplotlib.pyplot as plt

def visualizar(grafo):
    """
    Abre uma visualizacao interativa do grafo com o matplotlib
    """
    # TODO: Se for fornecido uma lista de grafos, visualizar todos
    # TODO: Colorir os nós de acordo com a opinião
    # TODO: Opção de fornecer um subgrafo para destacar

    # Lista de textos dos nós
    labels_dict = { node_name: "{}\n{:.2f}".format(node_name, grafo.nodes[node_name]["opinion"])
                    for node_name in grafo.nodes }
    
    nx.draw(grafo, with_labels = True, labels=labels_dict,
            node_color= '#aaaaff',
            font_size = 9, font_weight="bold")
    plt.show()