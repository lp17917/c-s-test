import sys
import time


class PriorityQueue:
    queue = []

    def pop(self):
        # Add func
        min = self.queue[0][2]
        mindex = 0
        for i in range(len(self.queue)):
            if min > self.queue[i][2]
                mindex = i
        return self.queue.pop(mindex)

    def push(self, ele):
        # Add func
        self.queue.append(ele)
        return


def file_read(file):
    f = open(file, "r")
    s = []
    e = []
    w = []
    for x in f:
        a = list(map(str, x.split()))
        s.append(a[0])
        e.append(a[1])
        w.append(int(a[2]))
    f.close()
    return s, e, w


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
    start, finish, weight = file_read(filename)
    #for count in range(len(start)):
        #print("Start: ", start[count], " Finish: ", finish[count], " Weight: ", weight[count])
    t1 = time.time()
    total = t1 - t0
    print(total)
    names = []
    for i in range(len(start)):
        read_name(start[i], names)
    for i in range(len(finish)):
        read_name(finish[i], names)

    print(names)
    path = ["null", origin]
    for i in range(len(names)):
        if names[i][0] == origin:
            names[i][1] = 1
            add_e("null", origin, 0)


if __name__ == "__main__":
    main()
