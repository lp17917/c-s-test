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


def dijkstra(names, edges, origin, endpoint):
    finished = 0
    path = []
    length = 0
    prioqueue = PriorityQueue()
    start = ["null", origin, 0]
    for i in range(len(names)):
        if names[i][0] == origin:
            names[i][1] = 1
            print(len(names))
            prioqueue.add_mod(start)
    prioqueue.display_list()

    while not finished:
        nearest = prioqueue.pop()
        path.append([nearest[0], nearest[1]])
        if nearest[1] == endpoint:
            length = nearest[2]
            finished = True
        else:
            for i in range(len(names)):
                if names[i][0] == nearest[1]:
                    names[i][1] = 2
            adj_nodes = get_adj(nearest, edges)
            check_if_fin(names, adj_nodes)
            addedweight = nearest[2]
            for i in range(len(adj_nodes)):
                adj_nodes[i][2] = adj_nodes[i][2] + addedweight
                prioqueue.add_mod(adj_nodes[i])
            print(nearest)
            prioqueue.display_list()
    path = generate_path(path, endpoint)
    return path, length


def get_adj(nearest, edges):
    adj_nodes = []
    for i in range(len(edges)):
        # add check for marked nodes
        if edges[i][0] == nearest[1]:
            adj_nodes.append(edges[i])
    return adj_nodes


def check_if_fin(names, adj):
    for j in range(len(names)):
        for i in range(len(adj)):

            if names[j][1] == 2 and adj[i][1] == names[j][0]:
                adj.pop(i)
                break
    return


def visited_nodes(names, adj_nodes):
    for j in range(len(names)):
        for k in range(len(adj_nodes)):
            if adj_nodes[k][1] == names[j][0]:
                names[j][1] = 1


def generate_path(path, destination):
    currentnode = destination
    f_path = []
    for i in reversed(path):
        if i[1] == currentnode:
            f_path.append(currentnode)
            currentnode = i[0]
    f_path.reverse()
    return f_path

