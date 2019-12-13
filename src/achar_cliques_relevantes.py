import networkx as nx

def achar_cliques_relevantes(grafo, n):
    """
    Dado um grafo conexo, retorna uma lista dos seus cliques relevantes.

    Um clique relevante é um clique maximal com pelo menos n nós
    (n sendo um inteiro maior que ou igual a 3).
    """
    # TODO
    list_cliques = []

    for cliq in list(nx.find_cliques(grafo)):
        sub = grafo.subgraph(cliq)

        if nx.number_of_nodes(sub) >= n:
            list_cliques.append(sub)
    
    return list_cliques