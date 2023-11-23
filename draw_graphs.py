import networkx as nx
import matplotlib.pyplot as plt


def draw_graph_4(visual, k,name):
    G = nx.Graph()
    # print(visual)    
    node_color_map=[]
    node_color_map.append("orange")
    for i in range(0, len(visual)):
        if k * i  < len(visual):
            try:
                G.add_edge(visual[i], visual[k * i + 1])
                node_color_map.append("lightgreen")
            except:
                break
            try:

                G.add_edge(visual[i], visual[k * i + 2])
                node_color_map.append("lightgreen")
            except:
                break
            try:

                G.add_edge(visual[i], visual[k * i + 3])
                node_color_map.append("lightgreen")
            except:
                break
            try:

                G.add_edge(visual[i], visual[k * i + 4])
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
    ax = plt.gca()
    plt.axis("off")
    ax.set_title("Heap for k=4")
    plt.savefig(f"plots/4_{name}.png")
    plt.show()


def draw_graph_3(visual, k,name):
    G = nx.Graph()
    node_color_map=[]
    node_color_map.append("orange")

    # print(visual)
    for i in range(0, len(visual)):
        if k * i  < len(visual):
            try:
                G.add_edge(visual[i], visual[k * i + 1])
                node_color_map.append("lightgreen")
            except:
                break
            try:

                G.add_edge(visual[i], visual[k * i + 2])
                node_color_map.append("lightgreen")
            except:
                break
            try:

                G.add_edge(visual[i], visual[k * i + 3])
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
    ax = plt.gca()
    ax.set_title("Heap for k=3")
    plt.axis("off")
    plt.savefig(f"plots/3_{name}.png")
    plt.show()


def draw_graph_2(visual, k,name):
    G = nx.Graph()
    #print(visual)
    node_color_map=[]
    node_color_map.append("orange")
    #print(len(visual))
    for i in range(0, len(visual)):
        if k * i<len(visual):
            try:
                G.add_edge(visual[i], visual[k * i + 1])
                node_color_map.append("lightgreen")
            except:
                break
            try:
                G.add_edge(visual[i], visual[k * i + 2])
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
    node_color_map=[]
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    ax.set_title("Heap for k=2")
    plt.savefig(f"plots/2_{name}.png")
    plt.show()

