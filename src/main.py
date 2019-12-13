import networkx as nx
import matplotlib.pyplot as plt
import random as random

print("test")

nomes_de_pessoas = ['Ansley', 'Kyra', 'Irene', 'Abbas', 'Addalynn', 'Ariadne', 'Benicio', 'Gavyn', 'Millie', 'Kiyan', 'Emmett', 'Emelia', 'Marcus', 'Kylie', 'Lukas', 'Kenia', 'Zane', 'Elle', 'Abel', 'Marion', 'Kynslee', 'Aspyn', 'Charlize', 'Billy', 'Selina', 'Reyna', 'Louisa', 'Braelyn', 'Lauren', 'Evander', 'Kennedi', 'Amir', 'Gianni', 'Bryton', 'Isaac', 'Walter', 'Sahana', 'Elly', 'Armani', 'Shiloh', 'Emma', 'Ariel', 'Truett', 'Meredith', 'Mayte', 'Regina', 'Emi', 'Celina', 'April', 'Ruger', 'Russell', 'Avah', 'Landry', 'Avril', 'Hailie', 'Journie', 'Reyna', 'Isha', 'Veer', 'Anika', 'Kerrigan', 'Clay', 'Leonard', 'Ammon', 'Aida', 'Henley', 'Tate', 'Adyson', 'Ansley', 'Mahdi', 'Alexander', 'Ameer', 'Montgomery', 'Laith', 'Lochlan', 'Hanna', 'Harper', 'Latrell', 'Kenzi', 'Dan', 'Guillermo', 'Brad', 'Julieta', 'Rilynn', 'Alicia', 'Rocco', 'Osiris', 'Arden', 'Mitchell', 'Eva', 'Mireya', 'Brylee', 'Westin', 'Emmanuel', 'Dalton', 'Gavriel', 'Marlena']

def gen_social_graph(size = 12, amount_connections = 20):
    """Gera um grafo social."""

    # Criar grafo
    G = nx.Graph()

    # Add vertices
    G.add_nodes_from(random.choices(nomes_de_pessoas, k=size))

    # Add arestas
    for i in range(amount_connections):
        pair = random.choices(list(G.nodes), k=2)
        G.add_edge(pair[0], pair[1])
    
    return G

# Abrir visualizacao interativa com o matplotlib
nx.draw(gen_social_graph(12, 10), with_labels = True, font_weight='bold')
plt.show()