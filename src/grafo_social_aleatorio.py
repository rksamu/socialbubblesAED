import networkx as nx
import random as random
from nomes import lista_de_nomes

def _add_opinioes_basico(G):
    """
    Adiciona opinioes aleatórias a um grafo, uniformemente e sem relação alguma
    com a sua topologia. Modifica o grafo passado como argumento.
    """
    
    for node in G.nodes:
        G.nodes[node]['opinion'] = random.uniform(-1.0, 1.0)

    return G

def _basico(tamanho = 12, qtd_conexoes = 10):
    """
    As arestas são aleatoriamente escolhidas dentre todas as arestas possíveis.
    As opiniões são uniformemente aleatórias sem relação alguma com a topologia.
    """
    # Criar grafo
    G = nx.Graph()

    # Add vertices
    G.add_nodes_from(random.sample(lista_de_nomes, k=tamanho))

    # Add opinioes
    _add_opinioes_basico(G)

    # Add arestas
    for i in range(qtd_conexoes):
        # Adicionar um par aleatório de vertices dentre as que ainda não existem:
        G.add_edge(*random.choice(list(nx.complement(G).edges)))
    
    return G

def grafo_social_aleatorio():
    #return _basico()

    return _add_opinioes_basico(nx.planted_partition_graph(2, 15, 0.3, 0.0))
