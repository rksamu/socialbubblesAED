import networkx as nx

def gerar_texto(estrutura):
    """
    Recebe a estrutura gerada por processar_grafo_social e retorna um texto
    para ser mostrado ao usuário, informando os cliques relevantes e todas as
    informações relacionadas que o usuário deve saber.
    """

    def texto_comp(estrutura, index):
        comp = estrutura[index]["componente"]
        clique_list = estrutura[index]["clique_list"]
        
        return (
            f"  * Componente {index+1} ({comp.number_of_nodes()} pessoas, {comp.number_of_edges()} conexões):\n"
            +
            "".join([f"    - Clique: {clq.nodes}\n" for clq in clique_list])
        )

    qtd_de_pessoas = sum([comp["componente"].number_of_nodes() for comp in estrutura])

    return (
        f"\n\nO grafo social tem {qtd_de_pessoas} pessoas e {len(estrutura)} componentes conexos.\n\n"
        +
        "".join([texto_comp(estrutura, i) for i in range(len(estrutura))])
    )

