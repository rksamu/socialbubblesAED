import networkx as nx
import random as random

nomes_de_pessoas = ['Ansley', 'Kyra', 'Irene', 'Abbas', 'Addalynn', 'Ariadne', 'Benicio', 'Gavyn', 'Millie', 'Kiyan', 'Emmett', 'Emelia', 'Marcus', 'Kylie', 'Lukas', 'Kenia', 'Zane', 'Elle', 'Abel', 'Marion', 'Kynslee', 'Aspyn', 'Charlize', 'Billy', 'Selina', 'Reyna', 'Louisa', 'Braelyn', 'Lauren', 'Evander', 'Kennedi', 'Amir', 'Gianni', 'Bryton', 'Isaac', 'Walter', 'Sahana', 'Elly', 'Armani', 'Shiloh', 'Emma', 'Ariel', 'Truett', 'Meredith', 'Mayte', 'Regina', 'Emi', 'Celina', 'April', 'Ruger', 'Russell', 'Avah', 'Landry', 'Avril', 'Hailie', 'Journie', 'Reyna', 'Isha', 'Veer', 'Anika', 'Kerrigan', 'Clay', 'Leonard', 'Ammon', 'Aida', 'Henley', 'Tate', 'Adyson', 'Ansley', 'Mahdi', 'Alexander', 'Ameer', 'Montgomery', 'Laith', 'Lochlan', 'Hanna', 'Harper', 'Latrell', 'Kenzi', 'Dan', 'Guillermo', 'Brad', 'Julieta', 'Rilynn', 'Alicia', 'Rocco', 'Osiris', 'Arden', 'Mitchell', 'Eva', 'Mireya', 'Brylee', 'Westin', 'Emmanuel', 'Dalton', 'Gavriel', 'Marlena']

def gerar_grafo_social(size = 12, amount_connections = 20):
    """
    Gera um grafo social aleatoriamente. O grafo tem tamanho size e quantidade
    de nós igual a amount_connections.
    """

    # Criar grafo
    G = nx.Graph()

    # Add vertices
    G.add_nodes_from(random.choices(nomes_de_pessoas, k=size))

    # Add opinioes
    for node in G.nodes:
        G.nodes[node]['opinion'] = random.uniform(-1.0, 1.0)

    # Add arestas
    for i in range(amount_connections):
        # Escolher um par aleatorio de vertices:
        pair = random.choices(list(G.nodes), k=2)
        G.add_edge(pair[0], pair[1])
    
    return G