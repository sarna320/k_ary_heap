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
        font_size=10,
        node_size=1500,
        node_color=node_color_map,
        arrows=True,
        arrowstyle="-|>",
    )
    node_color_map = []
    ax = plt.gca()

    figure = plt.gcf()  # get current figure
    figure.set_size_inches(16, 16) # set figure's size manually to your full screen (32x18)
    #plt.savefig('filename.png', bbox_inches='tight') # bbox_inches removes extra white spaces
    ax.margins(0.20)
    plt.axis("off")
    ax.set_title(f"Heap for k={k}")
    plt.savefig(f"plots/{k}_{name}.png",bbox_inches='tight')
    plt.show()
