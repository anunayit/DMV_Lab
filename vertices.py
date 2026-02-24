import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter the number of vertices: "))

if n > 3:
    G = nx.complete_graph(n)   # Create the complete graph
    
    nx.draw(
        G,
        node_color='green',
        node_size=1500,
        with_labels=True
    )
    
    plt.show()
else:
    print("Minimum number of vertices should be more than 3")