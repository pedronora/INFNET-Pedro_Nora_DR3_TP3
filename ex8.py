import networkx as nx
import matplotlib.pyplot as plt

# Representa um valor infinito para indicar que não há conexão direta entre os bairros
INF = float("inf")


def floyd_warshall(grafo):
    # Número de bairros no grafo
    num_bairros = len(grafo)

    # Criando uma cópia da matriz do grafo para armazenar os menores tempos de deslocamento
    dist = [[grafo[i][j] for j in range(num_bairros)] for i in range(num_bairros)]

    # Aplicação do algoritmo de Floyd-Warshall
    for k in range(num_bairros):  # Considera cada bairro como intermediário
        for i in range(num_bairros):  # Itera sobre todos os bairros de origem
            for j in range(num_bairros):  # Itera sobre todos os bairros de destino
                # Atualiza o tempo mínimo de deslocamento de i para j passando por k
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist  # Retorna a matriz com os menores tempos de deslocamento entre os pares de bairros


if __name__ == "__main__":
    # Definição do grafo representando os bairros e os tempos de deslocamento entre eles
    # A matriz indica os tempos de deslocamento entre os bairros (0 para si mesmo, INF se não houver ligação direta)
    bairros = [
        "Centro",
        "Vila Nova",
        "Jardim Botânico",
        "Bairro Alto",
        "São Pedro",
    ]

    grafo_bairros = [
        [0, 10, INF, 30, 100],  # Centro
        [10, 0, 50, INF, INF],  # Vila Nova
        [INF, 50, 0, 20, 10],  # Jardim Botânico
        [30, INF, 20, 0, 60],  # Bairro Alto
        [100, INF, 10, 60, 0],  # São Pedro
    ]

    # Executando o algoritmo de Floyd-Warshall
    menores_tempos = floyd_warshall(grafo_bairros)

    # Exibindo a matriz resultante
    print("Matriz dos menores tempos de deslocamento entre todos os bairros:")

    # Determinar a altura máxima dos bairros
    max_height = max(len(bairro) for bairro in bairros)

    for linha, bairro in zip(menores_tempos, bairros):
        print(f"{linha} => {bairro}")

    G = nx.Graph()
    G.add_nodes_from(bairros)

    conexoes = [
        ("Centro", "Vila Nova", 10),
        ("Centro", "Bairro Alto", 30),
        ("Vila Nova", "Jardim Botânico", 50),
        ("Jardim Botânico", "Bairro Alto", 20),
        ("Jardim Botânico", "São Pedro", 10),
        ("Bairro Alto", "São Pedro", 60),
    ]

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

    plt.title("Representação Gráfica dos Bairros e Tempos de Deslocamento", fontsize=16)
    plt.savefig("ex8.png", bbox_inches="tight")
