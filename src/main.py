import networkx as nx
import matplotlib.pyplot as plt
from gerar_grafo_social import gerar_grafo_social
from achar_cliques_relevantes import achar_cliques_relevantes

def processar_grafo_social(grafo):
    """
    Dado um grafo social, retorna uma estrutura no seguinte formato:

    [(Componente, [CliqueRel, ...]), ...]

    CliqueRel = Clique maximal com pelo menos N nós (N é um inteiro
                maior que ou igual a 3, ainda a ser decidido)
    """

    # Gerar uma lista de grafos onde cada um é um componente conexo
    comps = [grafo.subgraph(c).copy() for c in nx.connected_components(grafo)]

    # TODO: O resto

    return []

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


# Teste:
visualizar(gerar_grafo_social(20, 18))