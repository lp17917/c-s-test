import time


def main():
    t0 = time.time()
    f = open("exmouth-links.dat", "r")
    start = []
    finish = []
    weight = []
    for x in f:
        a = list(map(str, x.split()))
        start.append(a[0])
        finish.append(a[1])
        weight.append(int(a[2]))
    f.close()
    for count in range(len(start)):
        print("Start: ", start[count], " Finish: ", finish[count], " Weight: ", weight[count])
    t1 = time.time()
    total = t1 - t0
    print(total)


if __name__ == "__main__":
    main()
