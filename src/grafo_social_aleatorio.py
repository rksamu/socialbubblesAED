import networkx as nx
import random as random
from nomes import lista_de_nomes

def grafo_social_aleatorio(tamanho = 12, qtd_conexoes = 10):
    """
    Gera um grafo social aleatoriamente.
    O grafo tem quantidade de nós e arestas determinadas pelos argumentos.
    """

    # Criar grafo
    G = nx.Graph()

    # Add vertices
    G.add_nodes_from(random.choices(lista_de_nomes, k=tamanho))

    # Add opinioes
    for node in G.nodes:
        G.nodes[node]['opinion'] = random.uniform(-1.0, 1.0)

    # Add arestas
    for i in range(qtd_conexoes):
        # Escolher um par aleatorio de vertices:
        par = random.choices(list(G.nodes), k=2)
        G.add_edge(par[0], par[1])
    
    return G