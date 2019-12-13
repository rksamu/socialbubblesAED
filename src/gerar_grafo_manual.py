import networkx as nx
import random as random

#nomes_de_pessoas = ['Ansley', 'Kyra', 'Irene', 'Abbas', 'Addalynn', 'Ariadne', 'Benicio', 'Gavyn', 'Millie', 'Kiyan', 'Emmett', 'Emelia', 'Marcus', 'Kylie', 'Lukas', 'Kenia', 'Zane', 'Elle', 'Abel', 'Marion', 'Kynslee', 'Aspyn', 'Charlize', 'Billy', 'Selina', 'Reyna', 'Louisa', 'Braelyn', 'Lauren', 'Evander', 'Kennedi', 'Amir', 'Gianni', 'Bryton', 'Isaac', 'Walter', 'Sahana', 'Elly', 'Armani', 'Shiloh', 'Emma', 'Ariel', 'Truett', 'Meredith', 'Mayte', 'Regina', 'Emi', 'Celina', 'April', 'Ruger', 'Russell', 'Avah', 'Landry', 'Avril', 'Hailie', 'Journie', 'Reyna', 'Isha', 'Veer', 'Anika', 'Kerrigan', 'Clay', 'Leonard', 'Ammon', 'Aida', 'Henley', 'Tate', 'Adyson', 'Ansley', 'Mahdi', 'Alexander', 'Ameer', 'Montgomery', 'Laith', 'Lochlan', 'Hanna', 'Harper', 'Latrell', 'Kenzi', 'Dan', 'Guillermo', 'Brad', 'Julieta', 'Rilynn', 'Alicia', 'Rocco', 'Osiris', 'Arden', 'Mitchell', 'Eva', 'Mireya', 'Brylee', 'Westin', 'Emmanuel', 'Dalton', 'Gavriel', 'Marlena']


def gerar_grafo_social(tamanho = int(input("Quantas pessoas serão cadastradas na análise? "))):
    """
    Gera um grafo social aleatoriamente.
    O grafo tem quantidade de nós e arestas determinadas pelos argumentos.
    """
    qtd_conexoes = int(tamanho * 1.1)
    
    # Criar grafo
    G = nx.Graph()

    # Add vertices
    nomes = []
    for i in range(tamanho):
        nomes.append(input("Nome da {}ª pessoa: ".format(i + 1)))
    G.add_nodes_from(nomes)

    # Add opinioes
    for node in G.nodes:
        print("Perguntas para {}:".format(node))
        opiniao1 = int(input("O que você acha das mudanças climáticas?"
                                         "\n1- Não existem"
                                         "\n2- Estão acontecendo"
                                         "\n3- Estão acontecendo e são muito problemáticas"
                                        "\nSua resposta: ")) - 2
        opiniao2 = int(input("O que você acha do desmatamento na Amazônia?"
                                         "\n1- Não tem problema"
                                         "\n2- É ruim"
                                         "\n3- Vai destruir nosso futuro"
                                         "\nSua resposta: ")) - 2
        opiniao3 = int(input("O que você acha da caça esportiva?"
                                         "\n1- É uma prática normal"
                                         "\n2- É um tanto preocupante"
                                         "\n3- É crueldade gratuita e destrói a natureza"
                                         "\nSua resposta: ")) - 2
        opiniaofinal = (opiniao1 + opiniao2 +opiniao3) / 3
        G.nodes[node]['opinion'] = opiniaofinal

    # Add arestas
    for i in range(qtd_conexoes):
        # Escolher um par aleatorio de vertices:
        par = random.choices(list(G.nodes), k=2)
        G.add_edge(par[0], par[1])
    
    return G
