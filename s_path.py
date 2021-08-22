import sys
import time


class PriorityQueue:

    queue = []

    def __init__(self):
        return

    def pop(self):
        # Add func
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

    def add_mod(self, ele):
        pos = self.find(ele)
        if pos == -1:
            self.push(ele)
        else:
            self.update_priority(pos, ele)


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


def add_e(start, end, weight):
    return


def main():
    t0 = time.time()
    filename = sys.argv[1]
    origin = sys.argv[2]
    destination = sys.argv[3]
    print("File:", filename, "Origin:", origin, "Destination:", destination)
    edges = file_read(filename)
    #for count in range(len(start)):
        #print("Start: ", start[count], " Finish: ", finish[count], " Weight: ", weight[count])
    t1 = time.time()
    total = t1 - t0
    #print(total)
    names = []
    for i in range(len(edges)):
        read_name(edges[i][0], names)
        read_name(edges[i][1], names)

    #print(names)
    path = ["null", origin]
    for i in range(len(names)):
        if names[i][0] == origin:
            names[i][1] = 1
            add_e("null", origin, 0)

"""
    prioqueue = PriorityQueue()
    loading_vals = [["A", "B", 10],
                    ["C", "D", 11],
                    ["E", "A", 8],
                    ["C", "B", 7],
                    ["A", "D", 1],
                    ]
    for i in range(5):

        prioqueue.add_mod(loading_vals[i])
        prioqueue.display_list()
"""

if __name__ == "__main__":
    main()
