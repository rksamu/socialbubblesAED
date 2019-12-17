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

# Grafo aleatorio:
soc = grafo_social_aleatorio(30, 60)

# Grafo manual:
#soc = gerar_grafo_manual()

proc = processar_grafo_social(soc)

# Mostrar grafo social inteiro:
visualizar([soc], titulo=f'Grafo Social\n({soc.number_of_nodes()} pessoas, {len(proc)} componentes)')

# Mostrar texto:
print(gerar_texto(proc))

# Mostrar figuras dos cliques de cada componente:
for i, componente in enumerate(proc):
    visualizar(
        componente["clique_list"],
        titulo = f'Cliques do Componente {i+1}\n' + r'($i_x$ = Índice de Extremismo)',
    )