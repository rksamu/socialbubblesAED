import networkx as nx

def achar_cliques_relevantes(grafo, n):
    """
    Dado um grafo conexo, retorna uma lista dos seus cliques relevantes.

    Um clique relevante é um clique maximal com pelo menos n nós
    (n sendo um inteiro maior que ou igual a 3).
    """

    # TODO

    # Por enquanto retorna essa lista de grafos qualquer, so pra poder testar as outras funcoes:
    return [nx.petersen_graph(), nx.tutte_graph(), nx.tetrahedral_graph()]