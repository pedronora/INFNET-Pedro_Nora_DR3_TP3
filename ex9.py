import networkx as nx
import matplotlib.pyplot as plt


class GrafoAlgoritmoPrim:
    def __init__(self, cidades):
        self.cidades = cidades  # Lista de nomes das cidades
        self.V = len(cidades)  # Número de cidades
        self.grafo = [[0] * self.V for _ in range(self.V)]  # Matriz de custos

    def adicionar_conexao(self, cidade1, cidade2, custo):
        # Adiciona uma conexão entre duas cidades com seu custo
        u = self.cidades.index(cidade1)
        v = self.cidades.index(cidade2)
        self.grafo[u][v] = custo
        self.grafo[v][u] = custo  # Grafo não direcionado

    def prim(self):
        # Executa o algoritmo de Prim para encontrar a Árvore Geradora Mínima.
        infinito = float("inf")
        selecionado = [False] * self.V
        custo_minimo = [infinito] * self.V
        origem = [-1] * self.V  # Armazena a estrutura da AGM

        # Começa pela primeira cidade
        custo_minimo[0] = 0

        for _ in range(self.V):
            # Escolhe a cidade menor custo que ainda não foi incluído na AGM
            min_custo = infinito
            cidade_atual = -1
            for v in range(self.V):
                if not selecionado[v] and custo_minimo[v] < min_custo:
                    min_custo = custo_minimo[v]
                    cidade_atual = v

            selecionado[cidade_atual] = True

            # Atualiza os custos mínimos para as cidades vizinhas
            for v in range(self.V):
                if (
                    0 < self.grafo[cidade_atual][v] < custo_minimo[v]
                    and not selecionado[v]
                ):
                    custo_minimo[v] = self.grafo[cidade_atual][v]
                    origem[v] = cidade_atual

        # Exibindo a Árvore Geradora Mínima
        print("Plano de Expansão da Rede Elétrica (Custo Mínimo):")
        custo_total = 0
        for i in range(1, self.V):
            cidade_origem = self.cidades[origem[i]]
            cidade_destino = self.cidades[i]
            custo = self.grafo[i][origem[i]]
            print(f"\t{cidade_origem} → {cidade_destino} (Custo: R${custo} mi)")
            custo_total += custo
        print(f"\nCusto total do projeto: R$ {custo_total} milhões")


if __name__ == "__main__":
    cidades = ["Cidade A", "Cidade B", "Cidade C", "Cidade D", "Cidade E", "Cidade F"]

    rede_eletrica = GrafoAlgoritmoPrim(cidades)

    conexoes = [
        ("Cidade A", "Cidade B", 5),
        ("Cidade A", "Cidade C", 3),
        ("Cidade B", "Cidade C", 4),
        ("Cidade B", "Cidade D", 12),
        ("Cidade C", "Cidade D", 7),
        ("Cidade D", "Cidade E", 6),
        ("Cidade D", "Cidade F", 8),
        ("Cidade E", "Cidade F", 4),
    ]

    for cidade1, cidade2, custo in conexoes:
        rede_eletrica.adicionar_conexao(cidade1, cidade2, custo)

    rede_eletrica.prim()

    G = nx.Graph()
    G.add_nodes_from(cidades)
    G.add_weighted_edges_from(conexoes)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=10000,
        node_color="SpringGreen",
        font_weight="bold",
        font_size=12,
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=14)

    plt.title(
        "Representação Gráfica das Cidades e Custos de Instalação da Rede Elétrica",
        fontsize=16,
    )
    plt.savefig("ex9.png", bbox_inches="tight")
