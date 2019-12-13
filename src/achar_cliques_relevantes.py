import networkx as nx

def achar_cliques_relevantes(grafo, n):
    """
    Dado um grafo conexo, retorna uma lista dos seus cliques relevantes.

    Um clique relevante é um clique maximal com pelo menos n nós
    (n sendo um inteiro maior que ou igual a 3).
    """
    # TODO
    list_cliques = []
    list_find_cliques = list(nx.find_cliques(grafo))
    for cliq in list_find_cliques:
        S = grafo.subgraph(cliq)
        print(S)
        if nx.number_of_nodes(S) >= n:
            list_cliques.append(S)
    return list_cliques