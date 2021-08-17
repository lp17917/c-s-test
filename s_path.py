import time


def main():
    t0 = time.time()
    f = open("tester.dat", "r")
    a = []
    x = f.readline()
    a.append(x)
    print(a[0])
    f.close()
    numbers = list(map(str, a[0].split()))
    print(numbers)
    t1 = time.time()
    total = t1 - t0
    print(total)


if __name__ == "__main__":
    main()
