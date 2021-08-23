class PriorityQueue:

    queue = []

    def __init__(self):
        return

    def pop(self):
        # Add func
        if self.isempty():
            return None
        else:
            prio = self.queue[0][2]
            mindex = 0
            for i in range(len(self.queue)):
                if prio > self.queue[i][2]:
                    mindex = i
            return self.queue.pop(mindex)

    def push(self, ele):
        # Add func
        self.queue.append(ele)
        return

    def update_priority(self, index, ele):
        if ele[2] < self.queue[index][2]:
            self.queue[index] = ele

    def display_list(self):
        for i in range(len(self.queue)):
            print("(", self.queue[i][1], ",", self.queue[i][2], ")", end="   ")
        print("")

    def find(self, ele):
        for i in range(len(self.queue)):
            if self.queue[i][1] == ele[1]:
                return i
        return -1

    def isempty(self):
        if not self.queue:
            return True
        return False

    def add_mod(self, ele):
        pos = self.find(ele)
        if pos == -1:
            self.push(ele)
        else:
            self.update_priority(pos, ele)


def dijkstra(edges, origin, endpoint, debug):
    finished = 0
    path = []
    length = 0
    marked_nodes = []
    prioqueue = PriorityQueue()
    start = ["null", origin, 0]
    prioqueue.add_mod(start)
    if debug:
        prioqueue.display_list()

    while not finished:
        if prioqueue.isempty():
            finished = True
            print("Path could not be found")
            return [], 0
        else:
            nearest = prioqueue.pop()
            path.append([nearest[0], nearest[1]])
            if nearest[1] == endpoint:
                length = nearest[2]
                finished = True
            else:
                marked_nodes.append(nearest[1])
                adj_nodes = get_adj(marked_nodes, nearest, edges)
                addedweight = nearest[2]
                for adj_node in adj_nodes:
                    adj_node[2] = adj_node[2] + addedweight
                    prioqueue.add_mod(adj_node)

                if debug:
                    print(nearest)
                    prioqueue.display_list()

    path = generate_path(path, endpoint)
    return path, length


def get_adj(marked_nodes, nearest, edges):
    adj_nodes = []
    for edge in edges:
        # add check for marked nodes
        if edge[0] == nearest[1]:
            adj_nodes.append(edge)
    check_if_fin(marked_nodes, adj_nodes)
    return adj_nodes


def check_if_fin(marked_nodes, adj):
    for node in marked_nodes:
        for i in range(len(adj)):
            if node == adj[i][1]:
                adj.pop(i)
                break
    return


def generate_path(path, destination):
    currentnode = destination
    f_path = []
    for i in reversed(path):
        if i[1] == currentnode:
            f_path.append(currentnode)
            currentnode = i[0]
    f_path.reverse()
    return f_path

