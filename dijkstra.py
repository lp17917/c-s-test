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
                    prio = self.queue[i][2]
            return self.queue.pop(mindex)

    def push(self, ele):
        # Add func
        self.queue.append(ele)
        return

    def update_priority(self, index, ele):
        if ele[2] < self.queue[index][2]:
            self.queue[index] = ele

    def display_list(self):
        for ele in self.queue:
            print("(", ele[1], ",", ele[2], ")", end="   ")
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
    visiting_nodes = PriorityQueue()
    # Add the starting point as the first path
    start = ["null", origin, 0]
    visiting_nodes.add_mod(start)

    while not finished:
        if debug:
            visiting_nodes.display_list()

        # If there are no edges in the queue then there is no path
        if visiting_nodes.isempty():
            finished = True
            print("Path could not be found")
            return [], 0

        else:
            # Remove the lowest distance edge calculating the shortest path to that node
            nearest = visiting_nodes.pop()
            # Add the node to the path
            path.append([nearest[0], nearest[1]])
            # If the node is the destination finish computing path
            if nearest[1] == endpoint:
                length = nearest[2]
                finished = True
            else:
                # Add the node to the list of calculated nodes
                marked_nodes.append(nearest[1])
                # Gets the adjacent edges to the calculated nodes
                adj_nodes = get_adj(marked_nodes, nearest, edges)
                current_distance = nearest[2]
                for adj_node in adj_nodes:
                    # Add the distance to get to the node to the adjacent edges
                    adj_node[2] = adj_node[2] + current_distance
                    # Add the adjacent edges to the queue
                    visiting_nodes.add_mod(adj_node)

                if debug:
                    print(nearest)
                    visiting_nodes.display_list()

    path = generate_path(path, endpoint)
    return path, length


# Gets the edges adjacent to a node
def get_adj(marked_nodes, nearest, edges):
    adj_nodes = []
    for edge in edges:
        # add check for marked nodes
        if edge[0] == nearest[1]:
            adj_nodes.append(edge)
    check_if_fin(marked_nodes, adj_nodes)
    return adj_nodes


# Checks if the endpoint of an edge already has the shortest distance calculated
def check_if_fin(marked_nodes, adj):
    for node in marked_nodes:
        for i in range(len(adj)):
            if node == adj[i][1]:
                # Removes any edges going to calculated nodes
                adj.pop(i)
                break
    return


# Takes the output of the Dijkstras algorithm and puts it into a format for output
def generate_path(path, destination):
    currentnode = destination
    f_path = []
    # Goes through the list backwards following the path from the destination back to the origin
    for i in reversed(path):
        if i[1] == currentnode:
            f_path.append(currentnode)
            currentnode = i[0]
    f_path.reverse()
    return f_path

