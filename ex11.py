import networkx as nx
import matplotlib.pyplot as plt


class GrafoAlgoritmoPrim:
    def __init__(self, torres):
        self.torres = torres  # Lista de torres de comunicação
        self.V = len(torres)  # Número de torres
        self.grafo = [[0] * self.V for _ in range(self.V)]  # Matriz de custos

    def adicionar_conexao(self, torre1, torre2, custo):
        # Adiciona uma conexão entre duas torres com seu custo
        u = self.torres.index(torre1)
        v = self.torres.index(torre2)
        self.grafo[u][v] = custo
        self.grafo[v][u] = custo  # Grafo não direcionado

    def prim(self):
        # Executa o algoritmo de Prim para encontrar a Árvore Geradora Mínima.
        infinito = float("inf")
        selecionado = [False] * self.V
        custo_minimo = [infinito] * self.V
        origem = [-1] * self.V  # Armazena a estrutura da AGM

        # Começa pela primeira torre
        custo_minimo[0] = 0

        for _ in range(self.V):
            # Escolhe a torre de menor custo que ainda não foi incluída na AGM
            min_custo = infinito
            torre_atual = -1
            for v in range(self.V):
                if not selecionado[v] and custo_minimo[v] < min_custo:
                    min_custo = custo_minimo[v]
                    torre_atual = v

            selecionado[torre_atual] = True

            # Atualiza os custos mínimos para as torres vizinhas
            for v in range(self.V):
                if (
                    0 < self.grafo[torre_atual][v] < custo_minimo[v]
                    and not selecionado[v]
                ):
                    custo_minimo[v] = self.grafo[torre_atual][v]
                    origem[v] = torre_atual

        # Exibindo a Árvore Geradora Mínima
        print("Plano de Expansão da Infraestrutura de Telefonia (Custo Mínimo):")
        custo_total = 0
        for i in range(1, self.V):
            torre_origem = self.torres[origem[i]]
            torre_destino = self.torres[i]
            custo = self.grafo[i][origem[i]]
            print(f"\t{torre_origem} → {torre_destino} (Custo: R$ {custo} mihões)")
            custo_total += custo
        print(f"\nCusto total do projeto: R$ {custo_total} milhões")


if __name__ == "__main__":
    torres = [
        "Torre A",
        "Torre B",
        "Torre C",
        "Torre D",
        "Torre E",
        "Torre F",
        "Torre G",
    ]

    infraestrutura = GrafoAlgoritmoPrim(torres)

    conexoes = [
        ("Torre A", "Torre B", 7),
        ("Torre A", "Torre C", 5),
        ("Torre B", "Torre C", 3),
        ("Torre B", "Torre D", 10),
        ("Torre C", "Torre D", 4),
        ("Torre D", "Torre E", 6),
        ("Torre E", "Torre F", 8),
        ("Torre F", "Torre G", 5),
        ("Torre E", "Torre G", 9),
        ("Torre G", "Torre A", 12),
    ]

    for torre1, torre2, custo in conexoes:
        infraestrutura.adicionar_conexao(torre1, torre2, custo)

    infraestrutura.prim()

    G = nx.Graph()
    G.add_nodes_from(torres)
    G.add_weighted_edges_from(conexoes)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=5000,
        node_color="Lavender",
        font_weight="bold",
        font_size=12,
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=14)

    plt.title(
        "Plano de Expansão das Torres de Telefonia",
        fontsize=16,
    )
    plt.savefig("ex11.png", bbox_inches="tight")
