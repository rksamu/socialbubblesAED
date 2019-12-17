import networkx as nx
import random as random
from nomes import lista_de_nomes

def _basico(tamanho = 12, qtd_conexoes = 10):
    """
    As arestas são aleatoriamente escolhidas dentre todas as arestas possíveis.
    As opiniões são uniformemente aleatórias sem relação alguma com a topologia.
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

def grafo_social_aleatorio(tamanho = 12, qtd_conexoes = 10):
    return _basico(tamanho, qtd_conexoes)
