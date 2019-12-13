import networkx as nx

def gerar_texto(estrutura):
    """
    Recebe a estrutura gerada por processar_grafo_social e retorna um texto
    para ser mostrado ao usuário, informando os cliques relevantes e todas as
    informações relacionadas que o usuário deve saber.
    """

    def texto_comp(comp, num):
        """ Gera o texto de um componente """

        def texto_clique(clique, num):
            """ Gera o texto de um clique """

            return """
              --Clique: {pessoas}
                Indice de extremismo: {indice}
            """.format(
                pessoas = ', '.join(clique.nodes),
                indice = 'TO-DO',
            )
        
        return """
            Componente:
                {cliques}
        """.format(
            cliques = "".join([texto_clique(clq, -1) for clq in comp["clique_list"]])
        )

    return "\n\n".join([texto_comp(cp, -1) for cp in estrutura])

    # Exemplo de retorno:
    """
    O grafo social fornecido tem 3 componentes conexos.

    Componente 1 (18 pessoas, 22 conexoes, 2 cliques relevantes):
        * Clique 1 (3 pessoas):
          Maria, Ana, Pedro
          Indice de extremismo: 0.79

        * Clique 2 (3 pessoas):
          Ana, Marcio, Lucas
          Indice de extremismo: -0.69

    Componente 2 (12 pessoas, 15 conexoes, 3 cliques relevantes):
        * Clique 1 (5 pessoas):
          Luiza, Abraao, Judite, Vladmir, Joao
          Indice de extremismo: 0.98

        * Clique 2 (3 pessoas):
          Fabio, Marcone, Leo
          Indice de extremismo: -0.7

        * Clique 3 (3 pessoas):
          John, Smith, Bob
          Indice de extremismo: -0.5
    """
