import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt, ceil

def visualizar(grafos, titulo = ''):
    """
    Abre uma visualizacao interativa do matplotlib da lista de grafos fornecida.
    """
    # TODO: Colorir os nós de acordo com a opinião
    # TODO: Opção de fornecer um subgrafo para destacar

    # Determina a quantidade de plots necessaria
    qtd_cols_e_lins = ceil(sqrt(len(grafos)))

    # Título mostrado no topo da figura
    plt.suptitle(titulo)

    for i, grafo in enumerate(grafos):
        # Cria axes
        plt.subplot(qtd_cols_e_lins, qtd_cols_e_lins, i+1)


        # Reduz um pouco o zoom para os nomes das pessoas não ficarem
        # de fora quando vários grafos são visualizados
        plt.margins(0.2)

        # Lista de textos dos nós
        labels_dict = { node_name: "{}\n{:.2f}".format(node_name, grafo.nodes[node_name]["opinion"])
                        for node_name in grafo.nodes }

        nx.draw_networkx(
            grafo,
            with_labels = True, labels = labels_dict,
            node_color = [grafo.nodes[node]["opinion"] for node in grafo.nodes],
            cmap = plt.cm.get_cmap('coolwarm_r'), vmin = -1.0, vmax = 1.0,
            node_size = 50,
            edge_color = '#888888',
            font_size = 8, font_weight = "bold",
        )

    plt.show()