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


def name_exists(name, r_names):
    for i in range(len(r_names)):
        if name == r_names[i][0]:
            return True
    return False


def read_name(name, r_names):
    if not name_exists(name, r_names):
        r_names.append([name, 0])
        return True
    return False


def main():
    t0 = time.time()
    filename = sys.argv[1]
    origin = sys.argv[2]
    destination = sys.argv[3]
    print("File:", filename, "Origin:", origin, "Destination:", destination)
    edges = file_read(filename)
    names = []
    for i in range(len(edges)):
        read_name(edges[i][0], names)
        read_name(edges[i][1], names)

    path, length = dijkstra(names, edges, origin, destination)
    t1 = time.time()
    for i in range(len(path)):
        print(path[i])
    total = t1 - t0
    print(total)


if __name__ == "__main__":
    main()
