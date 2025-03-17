import networkx as nx
import matplotlib.pyplot as plt


class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_cidade(self, cidade):
        # Adiciona uma cidade ao grafo.
        if cidade not in self.vertices:
            self.vertices[cidade] = {}

    def adicionar_trajeto(self, trajeto1, trajeto2, custo):
        # Cria um trajeto (aresta) entre duas cidades (vértices) com um peso (custo da viagem).
        self.vertices[trajeto1][trajeto2] = custo
        self.vertices[trajeto2][trajeto1] = custo  # Grafo não direcionado

    def dijkstra(self, origem, destino):
        # Encontra a menor rota entre duas cidades usando Dijkstra.
        nao_visitados = list(self.vertices.keys())  # Lista de cidades não visitadas
        custos = {
            cidade: float("inf") for cidade in self.vertices
        }  # Inicializa todas os custos como infinito
        custos[origem] = 0  # O custo da origem para ela mesma é 0
        predecessores = {}  # Para armazenar o trajeto percorrido

        while nao_visitados:
            # Encontrar o nó com o menor custo
            cidade_atual = min(nao_visitados, key=lambda custo: custos[custo])

            if custos[cidade_atual] == float("inf"):
                break  # Se o menor custo ainda for infinito, não há trajeto viável

            for vizinho, custo in self.vertices[cidade_atual].items():
                novo_trajeto = custos[cidade_atual] + custo
                if novo_trajeto < custos[vizinho]:  # Se encontrarmos um caminho melhor
                    custos[vizinho] = novo_trajeto
                    predecessores[vizinho] = cidade_atual  # Armazena de onde viemos

            nao_visitados.remove(cidade_atual)  # Marca a cidade como visitada

        # Reconstrução do trajeto
        trajeto = []
        cidade_atual = destino
        while cidade_atual in predecessores:
            trajeto.append(cidade_atual)
            cidade_atual = predecessores[cidade_atual]
        trajeto.append(origem)
        trajeto.reverse()

        return trajeto, custos[destino]


if __name__ == "__main__":
    mapa_cidades = GrafoPoderado()
    cidades = [
        "Florianópolis",
        "Blumenau",
        "Joinville",
        "Balneário Camboriú",
        "Chapecó",
    ]

    for cidade in cidades:
        mapa_cidades.adicionar_cidade(cidade)

    trajetos = [
        ("Florianópolis", "Blumenau", 130),
        ("Florianópolis", "Balneário Camboriú", 80),
        ("Blumenau", "Joinville", 90),
        ("Chapecó", "Florianópolis", 550),
        ("Balneário Camboriú", "Joinville", 60),
    ]

    for cidade1, cidade2, custos in trajetos:
        mapa_cidades.adicionar_trajeto(cidade1, cidade2, custos)

    origem = "Joinville"
    destino = "Florianópolis"
    rota, custos = mapa_cidades.dijkstra(origem, destino)

    print(f"Melhor rota de {origem} para {destino}: {' => '.join(rota)}")
    print(f"Custo da viagem: {custos}")

    G = nx.Graph()
    G.add_nodes_from(cidades)
    G.add_weighted_edges_from(trajetos)
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

    plt.title("Representação Gráfica das Cidades", fontsize=16)
    plt.savefig("ex4.png", bbox_inches="tight")
