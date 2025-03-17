import networkx as nx
import matplotlib.pyplot as plt


class GrafoAlgoritmoPrim:
    def __init__(self, bairros):
        self.bairros = bairros  # Lista de nomes dos bairros
        self.V = len(bairros)  # Número de bairros
        self.grafo = [[0] * self.V for _ in range(self.V)]  # Matriz de custos

    def adicionar_conexao(self, bairro1, bairro2, custo):
        # Adiciona uma conexão entre dois bairros com seu custo
        u = self.bairros.index(bairro1)
        v = self.bairros.index(bairro2)
        self.grafo[u][v] = custo
        self.grafo[v][u] = custo  # Grafo não direcionado

    def prim(self):
        # Executa o algoritmo de Prim para encontrar a Árvore Geradora Mínima.
        infinito = float("inf")
        selecionado = [False] * self.V
        custo_minimo = [infinito] * self.V
        origem = [-1] * self.V  # Armazena a estrutura da AGM

        # Começa pelo primeiro bairro
        custo_minimo[0] = 0

        for _ in range(self.V):
            # Escolhe o bairro de menor custo que ainda não foi incluído na AGM
            min_custo = infinito
            bairro_atual = -1
            for v in range(self.V):
                if not selecionado[v] and custo_minimo[v] < min_custo:
                    min_custo = custo_minimo[v]
                    bairro_atual = v

            selecionado[bairro_atual] = True

            # Atualiza os custos mínimos para os bairros vizinhos
            for v in range(self.V):
                if (
                    0 < self.grafo[bairro_atual][v] < custo_minimo[v]
                    and not selecionado[v]
                ):
                    custo_minimo[v] = self.grafo[bairro_atual][v]
                    origem[v] = bairro_atual

        # Exibindo o plano de instalação das tubulações
        print("Plano de Abastecimento de Água (Custo Mínimo):")
        custo_total = 0
        for i in range(1, self.V):
            bairro_origem = self.bairros[origem[i]]
            bairro_destino = self.bairros[i]
            custo = self.grafo[i][origem[i]]
            print(f"\t{bairro_origem} → {bairro_destino} (Custo: R${custo} milhões)")
            custo_total += custo
        print(f"\nCusto total do projeto: R$ {custo_total} milhões")


if __name__ == "__main__":
    bairros = [
        "Bairro A",
        "Bairro B",
        "Bairro C",
        "Bairro D",
        "Bairro E",
        "Bairro F",
        "Bairro G",
    ]

    rede_agua = GrafoAlgoritmoPrim(bairros)

    conexoes = [
        ("Bairro A", "Bairro B", 4),
        ("Bairro A", "Bairro C", 6),
        ("Bairro B", "Bairro C", 2),
        ("Bairro B", "Bairro D", 8),
        ("Bairro C", "Bairro D", 5),
        ("Bairro D", "Bairro E", 7),
        ("Bairro E", "Bairro F", 3),
        ("Bairro F", "Bairro G", 6),
        ("Bairro E", "Bairro G", 9),
        ("Bairro G", "Bairro A", 10),
    ]

    for bairro1, bairro2, custo in conexoes:
        rede_agua.adicionar_conexao(bairro1, bairro2, custo)

    rede_agua.prim()

    G = nx.Graph()
    G.add_nodes_from(bairros)
    G.add_weighted_edges_from(conexoes)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=10500,
        node_color="DeepSkyBlue",
        font_weight="bold",
        font_size=12,
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=14)

    plt.title(
        "Representação Gráfica dos Bairros e Custos de Instalação das Tubulações",
        fontsize=16,
    )
    plt.savefig("ex10.png", bbox_inches="tight")
