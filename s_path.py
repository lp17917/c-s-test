import sys
import time

from dijkstra import dijkstra


# Reads the file specified and generates a list of edges
def file_read(file):
    f = open(file, "r")
    edges = []
    for x in f:
        a = list(map(str, x.split()))
        edges.append([a[0], a[1], int(a[2])])
    f.close()
    return edges


# Checks to see if a node exists
def node_exists(node, nodes):
    for n in nodes:
        if n == node:
            return True
    return False


# Adds a node to the list of nodes if not already in the list
def add_node(node, nodes):
    if not node_exists(node, nodes):
        nodes.append(node)
    return


def main():
    debug = False
    nodes = []
    path = []
    length = 0
    filename = sys.argv[1]
    origin = sys.argv[2]
    destination = sys.argv[3]

    try:

        if sys.argv[4]:
            debug = True
    except IndexError:
        pass

    if debug:
        t0 = time.time()

    # Reads the file for all edges and generates a list of nodes
    edges = file_read(filename)
    for edge in edges:
        add_node(edge[0], nodes)
        add_node(edge[1], nodes)

    if debug:
        print(nodes)

    # If both the origin and destination nodes exist run the algorithm
    if node_exists(origin, nodes) and node_exists(destination, nodes):
        path, length = dijkstra(edges, origin, destination, debug)
        # Writes out the path from the origin to the destination
        for stop in path:
            print(stop)

    if debug:
        print(length)
        t1 = time.time()

        total = t1 - t0
        print(total)


if __name__ == "__main__":
    main()
