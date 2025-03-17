import networkx as nx
import matplotlib.pyplot as plt


class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_bairro(self, bairro):
        # Adiciona um bairro ao grafo.
        if bairro not in self.vertices:
            self.vertices[bairro] = {}

    def adicionar_rua(self, bairro1, bairro2, distancia):
        # Cria uma rua (aresta) entre dois bairros (vértices) com um peso (distância).
        self.vertices[bairro1][bairro2] = distancia
        self.vertices[bairro2][bairro1] = distancia  # Grafo não direcionado

    def dijkstra(self, origem, destino):
        # Encontra a menor rota entre dois bairros usando Dijkstra.
        nao_visitados = list(self.vertices.keys())  # Lista de bairros não visitadas
        distancias = {
            bairro: float("inf") for bairro in self.vertices
        }  # Inicializa todas as distâncias como infinito
        distancias[origem] = 0  # A distância da origem para ela mesma é 0
        predecessores = {}  # Para armazenar o caminho percorrido

        while nao_visitados:
            # Encontrar o nó com a menor distância conhecida
            bairro_atual = min(nao_visitados, key=lambda bairro: distancias[bairro])

            if distancias[bairro_atual] == float("inf"):
                break  # Se a menor distância ainda for infinita, não há caminho viável

            for vizinho, distancia in self.vertices[bairro_atual].items():
                nova_distancia = distancias[bairro_atual] + distancia
                if (
                    nova_distancia < distancias[vizinho]
                ):  # Se encontrarmos um caminho melhor
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = bairro_atual  # Armazena de onde viemos

            nao_visitados.remove(bairro_atual)  # Marca o bairro como visitado

        # Reconstrução do caminho
        caminho = []
        bairro_atual = destino
        while bairro_atual in predecessores:
            caminho.append(bairro_atual)
            bairro_atual = predecessores[bairro_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]


if __name__ == "__main__":
    mapa_bairros = GrafoPoderado()
    bairros = [
        "BAIRRO A",
        "BAIRRO B",
        "BAIRRO C",
        "BAIRRO D",
        "BAIRRO E",
        "BAIRRO F",
        "BAIRRO G",
    ]

    for bairro in bairros:
        mapa_bairros.adicionar_bairro(bairro)

    ruas = [
        ("BAIRRO A", "BAIRRO B", 2),
        ("BAIRRO A", "BAIRRO C", 3),
        ("BAIRRO B", "BAIRRO D", 4),
        ("BAIRRO C", "BAIRRO D", 1),
        ("BAIRRO C", "BAIRRO E", 5),
        ("BAIRRO D", "BAIRRO F", 3),
        ("BAIRRO E", "BAIRRO F", 2),
        ("BAIRRO F", "BAIRRO G", 4),
        ("BAIRRO G", "BAIRRO A", 6),
    ]

    for bairro1, bairro2, distancia in ruas:
        mapa_bairros.adicionar_rua(bairro1, bairro2, distancia)

    origem = "BAIRRO A"
    destino = "BAIRRO E"
    rota, distancia = mapa_bairros.dijkstra(origem, destino)

    print(f"Melhor rota de {origem} para {destino}: {' => '.join(rota)}")
    print(f"Distância total: {distancia} km")

    G = nx.Graph()
    G.add_nodes_from(bairros)
    G.add_weighted_edges_from(ruas)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3000,
        node_color="lightgreen",
        font_size=11,
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=14)

    plt.title("Representação Gráfica do Grafo dos Bairros e Ruas", fontsize=16)
    plt.savefig("ex2.png", bbox_inches="tight")
