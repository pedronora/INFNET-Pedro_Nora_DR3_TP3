import networkx as nx
import matplotlib.pyplot as plt


class GrafoAlgoritmoPrim:
    def __init__(self, bairros):
        self.V = len(bairros)  # Número de bairros
        self.bairros = bairros  # Lista de bairros
        self.grafo = [[0] * self.V for _ in range(self.V)]  # Matriz de adjacência

    def adicionar_conexao(self, bairro1, bairro2, custo):
        # Adiciona uma conexão entre dois bairros com um custo.
        u = self.bairros.index(bairro1)
        v = self.bairros.index(bairro2)
        self.grafo[u][v] = custo
        self.grafo[v][u] = custo  # Grafo não direcionado

    def prim(self):
        # Executa o algoritmo de Prim para encontrar a Árvore Geradora Mínima.
        infinito = float("inf")
        selecionado = [False] * self.V  # Marcar os bairros incluídos na AGM
        chave = [infinito] * self.V  # Custo mínimo para incluir um bairro
        pai = [-1] * self.V  # Armazena a estrutura da AGM

        # Começamos pelo primeiro bairro
        chave[0] = 0

        for _ in range(self.V):
            # Escolhe o bairro de menor custo que ainda não foi incluído na AGM
            minimo = infinito
            u = -1
            for v in range(self.V):
                if not selecionado[v] and chave[v] < minimo:
                    minimo = chave[v]
                    u = v

            selecionado[u] = True  # Marca o bairro como incluído na AGM

            # Atualiza os valores das chaves e define os pais dos bairros adjacentes
            for v in range(self.V):
                if 0 < self.grafo[u][v] < chave[v] and not selecionado[v]:
                    chave[v] = self.grafo[u][v]
                    pai[v] = u

        # Exibindo a Árvore Geradora Mínima
        print("\nConexões da Árvore Geradora Mínima:")
        custo_total = 0
        for i in range(1, self.V):
            bairro1 = self.bairros[pai[i]]
            bairro2 = self.bairros[i]
            custo = self.grafo[i][pai[i]]
            print(f"{bairro1} - {bairro2} (Custo: {custo})")
            custo_total += custo
        print(f"Custo total da AGM: {custo_total}")


if __name__ == "__main__":

    bairros = [
        "Centro",
        "Vila Nova",
        "Jardim Botânico",
        "Bairro Alto",
        "São Pedro",
        "Lagoa",
    ]

    g = GrafoAlgoritmoPrim(bairros)

    conexoes = [
        ("Centro", "Vila Nova", 4),
        ("Centro", "Jardim Botânico", 2),
        ("Vila Nova", "Jardim Botânico", 5),
        ("Vila Nova", "Bairro Alto", 10),
        ("Jardim Botânico", "Bairro Alto", 8),
        ("Jardim Botânico", "São Pedro", 3),
        ("Bairro Alto", "São Pedro", 7),
        ("Bairro Alto", "Lagoa", 6),
        ("São Pedro", "Lagoa", 1),
    ]

    for bairro1, bairro2, custo in conexoes:
        g.adicionar_conexao(bairro1, bairro2, custo)

    g.prim()

    G = nx.Graph()
    G.add_nodes_from(bairros)
    G.add_weighted_edges_from(conexoes)
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

    plt.title("Representação Gráfica dos Bairros e Conexões", fontsize=16)
    plt.savefig("ex7.png", bbox_inches="tight")
