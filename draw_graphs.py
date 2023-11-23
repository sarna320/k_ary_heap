import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(visual, k, name="heap"):
    G = nx.Graph()
    # print(visual)
    node_color_map = []
    node_color_map.append("orange")
    # print(len(visual))
    for i in range(0, len(visual)):
        for kk in range(1, k + 1):
            if k * i < len(visual):
                try:
                    G.add_edge(visual[i], visual[k * i + kk])
                    node_color_map.append("lightgreen")
                except:
                    break

    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    nx.draw_networkx(
        G,
        pos=pos,
        ax=None,
        with_labels=True,
        font_size=6,
        node_size=500,
        node_color=node_color_map,
        arrows=True,
        arrowstyle="-|>",
    )
    node_color_map = []
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    ax.set_title(f"Heap for k={k}")
    plt.savefig(f"plots/{k}_{name}.png")
    plt.show()
