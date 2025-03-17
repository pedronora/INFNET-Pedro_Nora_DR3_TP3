import networkx as nx
import matplotlib.pyplot as plt


class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_cidade(self, cidade):
        # Adiciona uma cidade ao grafo.
        if cidade not in self.vertices:
            self.vertices[cidade] = {}

    def adicionar_estrada(self, cidade1, cidade2, distancia):
        # Cria uma estrada (aresta) entre duas cidades (vértices) com um peso (distância).
        self.vertices[cidade1][cidade2] = distancia
        self.vertices[cidade2][cidade1] = distancia  # Grafo não direcionado

    def dijkstra(self, origem, destino):
        # Encontra a menor rota entre duas cidades usando Dijkstra.
        nao_visitados = list(self.vertices.keys())  # Lista de cidades não visitadas
        distancias = {
            cidade: float("inf") for cidade in self.vertices
        }  # Inicializa todas as distâncias como infinito
        distancias[origem] = 0  # A distância da origem para ela mesma é 0
        predecessores = {}  # Para armazenar o caminho percorrido

        while nao_visitados:
            # Encontrar o nó com a menor distância conhecida
            cidade_atual = min(nao_visitados, key=lambda cidade: distancias[cidade])

            if distancias[cidade_atual] == float("inf"):
                break  # Se a menor distância ainda for infinita, não há caminho viável

            for vizinho, distancia in self.vertices[cidade_atual].items():
                nova_distancia = distancias[cidade_atual] + distancia
                if (
                    nova_distancia < distancias[vizinho]
                ):  # Se encontrarmos um caminho melhor
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = cidade_atual  # Armazena de onde viemos

            nao_visitados.remove(cidade_atual)  # Marca a cidade como visitada

        # Reconstrução do caminho
        caminho = []
        cidade_atual = destino
        while cidade_atual in predecessores:
            caminho.append(cidade_atual)
            cidade_atual = predecessores[cidade_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]


if __name__ == "__main__":
    mapa_cidades = GrafoPoderado()
    cidades = ["A", "B", "C", "D", "E", "F", "G"]

    for cidade in cidades:
        mapa_cidades.adicionar_cidade(cidade)

    estradas = [
        ("A", "B", 4),
        ("A", "C", 3),
        ("B", "C", 5),
        ("B", "D", 2),
        ("C", "E", 7),
        ("D", "E", 6),
        ("D", "F", 5),
        ("E", "F", 2),
        ("F", "G", 3),
    ]

    for cidade1, cidade2, distancia in estradas:
        mapa_cidades.adicionar_estrada(cidade1, cidade2, distancia)

    origem = "A"
    destino = "F"
    rota, distancia = mapa_cidades.dijkstra(origem, destino)

    print(f"Melhor rota de {origem} para {destino}: {' => '.join(rota)}")
    print(f"Distância total: {distancia} km")

    G = nx.Graph()
    G.add_nodes_from(cidades)
    G.add_weighted_edges_from(estradas)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=800, font_size=10)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Representação Gráfica do Grafo")
    plt.savefig("ex1.png", bbox_inches="tight")
