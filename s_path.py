import sys
import time

from dijkstra import dijkstra


def file_read(file):
    f = open(file, "r")
    edges = []
    for x in f:
        a = list(map(str, x.split()))
        edges.append([a[0], a[1], int(a[2])])
    f.close()
    return edges


def node_exists(node, nodes):
    for n in nodes:
        if n == node:
            return True
    return False


def read_name(node, nodes):
    if not node_exists(node, nodes):
        nodes.append(node)
        return True
    return False


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

    edges = file_read(filename)
    for edge in edges:
        read_name(edge[0], nodes)
        read_name(edge[1], nodes)

    if debug:
        print(nodes)

    if node_exists(origin, nodes) and node_exists(destination, nodes):
        path, length = dijkstra(edges, origin, destination, debug)
        for stop in path:
            print(stop)

    if debug:
        print(length)
        t1 = time.time()

        total = t1 - t0
        print(total)


if __name__ == "__main__":
    main()
