from time import time

import numpy as np
import matplotlib.pyplot as plt

def bell_ford(graph, source):
    # graph: adjacency matrix V*V where element are distance between nodes

    distance = {}  # distance of each node from source
    # #predecessor of each node to reach source according to the shortest path
    #predecessor = {}
    Cycles = False  # True if the graph has negative weight cycle

    # initialize source to allthe node distance= infinity
    for node in range(len(graph)):
        distance[node] = float('Inf')
        #predecessor[node] = None

    distance[source] = 0

    # Running the loop
    for i in range(len(graph)-1):
        for u in range(len(graph)):  # for each node in graph
            for v in range(len(graph[u])):  # for each edge from u

                # relaxation
                if distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]
                    #predecessor[v] = u

    # check for the negative weight cycle
    for u in range(len(graph)):
        for v in range(len(graph[u])):
            if distance[v] > distance[u] + graph[u][v]:
                Cycles = True

    return distance, Cycles  #predecessor

def test_bell_ford(V):
    # V : array with each entry as number of nodes in the graph

    duration = []
    for node in V:
        matrix = np.random.randint(1,100,(node,node))
        t0 = time()
        distance,Cycles = bell_ford(matrix,0)
        case_duration = time()-t0
        print(node,": ",case_duration,"\n")
        duration.append(case_duration)

    np.save("Vandtime",(V,duration))
    plt.plot(V,duration)
    plt.xlabel("Number of Nodes")
    plt.ylabel("Running Time")
    plt.title("Bellman Ford Analysis on Dense Graph")
    plt.savefig("performance.png")

if __name__ == '__main__':
    V = [1, 10, 100, 200, 500, 1000, 2000]
    test_bell_ford(V)
