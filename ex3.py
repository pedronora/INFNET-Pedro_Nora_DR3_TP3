import networkx as nx
import matplotlib.pyplot as plt


class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_aeroporto(self, aeroporto):
        # Adiciona um aeroporto ao grafo.
        if aeroporto not in self.vertices:
            self.vertices[aeroporto] = {}

    def adicionar_linha(self, aero1, aero2, distancia):
        # Cria uma linha/viagem (aresta) entre dois aeroportos (vértices) com um peso (distância).
        self.vertices[aero1][aero2] = distancia
        self.vertices[aero2][aero1] = distancia  # Grafo não direcionado

    def dijkstra(self, origem, destino):
        # Encontra a menor rota entre dois aeroportos usando Dijkstra.
        nao_visitados = list(self.vertices.keys())  # Lista de aeroportos não visitadas
        distancias = {
            aeroporto: float("inf") for aeroporto in self.vertices
        }  # Inicializa todas as distâncias como infinito
        distancias[origem] = 0  # A distância da origem para ela mesma é 0
        predecessores = {}  # Para armazenar o caminho percorrido

        while nao_visitados:
            # Encontrar o nó com a menor distância conhecida
            aero_atual = min(nao_visitados, key=lambda aero: distancias[aero])

            if distancias[aero_atual] == float("inf"):
                break  # Se a menor distância ainda for infinita, não há caminho viável

            for vizinho, distancia in self.vertices[aero_atual].items():
                nova_distancia = distancias[aero_atual] + distancia
                if (
                    nova_distancia < distancias[vizinho]
                ):  # Se encontrarmos um caminho melhor
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = aero_atual  # Armazena de onde viemos

            nao_visitados.remove(aero_atual)  # Marca o aeroporto como visitado

        # Reconstrução do caminho
        caminho = []
        aero_atual = destino
        while aero_atual in predecessores:
            caminho.append(aero_atual)
            aero_atual = predecessores[aero_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]


if __name__ == "__main__":
    mapa_aeroportos = GrafoPoderado()
    aeroportos = ["GRU", "FLN", "CGH", "BSB", "GIG", "SSA", "CWB", "POA", "REC", "CAC"]

    for aero in aeroportos:
        mapa_aeroportos.adicionar_aeroporto(aero)

    linhas = [
        ("GRU", "FLN", 5),
        ("GRU", "CGH", 1),
        ("GRU", "BSB", 3),
        ("GRU", "GIG", 2),
        ("GRU", "SSA", 6),
        ("GRU", "CWB", 4),
        ("GRU", "POA", 7),
        ("GRU", "REC", 8),
        ("GRU", "CAC", 9),
        ("CGH", "GIG", 2),
        ("BSB", "SSA", 5),
        ("CWB", "POA", 3),
        ("REC", "SSA", 4),
        ("FLN", "CWB", 2),
    ]

    for aero1, aero2, distancia in linhas:
        mapa_aeroportos.adicionar_linha(aero1, aero2, distancia)

    origem = "CAC"
    destino = "FLN"
    rota, distancia = mapa_aeroportos.dijkstra(origem, destino)

    print(f"Melhor rota de {origem} para {destino}: {' => '.join(rota)}")
    print(f"Distância total: {distancia*100} km")

    G = nx.Graph()
    G.add_nodes_from(aeroportos)
    G.add_weighted_edges_from(linhas)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1000,
        node_color="skyblue",
        font_weight="bold",
        font_size=12,
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=14)

    plt.title("Representação Gráfica dos Aeroportos e Linhas", fontsize=16)
    plt.savefig("ex3.png", bbox_inches="tight")
