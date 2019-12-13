import networkx as nx
import matplotlib.pyplot as plt
from grafo_social_aleatorio import grafo_social_aleatorio
from achar_cliques_relevantes import achar_cliques_relevantes
from visualizar import visualizar
from gerar_texto import gerar_texto
from gerar_grafo_manual import gerar_grafo_manual

def processar_grafo_social(grafo):
    """
    Dado um grafo social, retorna uma estrutura no seguinte formato:

    [
        {
            "componente": Componente,
            "clique_list": [CliqueRel, ...]
        },
        ...
    ]

    (Isso é uma lista de dicionarios)

    Componente = Um componente conexo do grafo fornecido pelo argumento

    CliqueRel = Clique maximal com pelo menos N nós (N é um inteiro
                maior que ou igual a 3, ainda a ser decidido)
    """

    # Gerar uma lista de grafos onde cada um é um componente conexo
    comps = [grafo.subgraph(c).copy() for c in nx.connected_components(grafo)]

    resultado = []
    for comp in comps:
        resultado.append(
            {
                "componente": comp,
                "clique_list": achar_cliques_relevantes(comp, 3),
            }
        )

    return resultado


# Teste:
v = visualizar # atalho para a funcao visualizar

soc = grafo_social_aleatorio(10, 60)
v([soc])

proc = processar_grafo_social(soc)

#for clique in proc[0]["clique_list"]:
#    v([clique])
v(proc[0]["clique_list"])