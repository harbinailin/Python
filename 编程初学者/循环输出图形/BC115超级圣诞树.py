while True:
    try:
        h = int(input())
        l = ["*", "* *", "* * *"]
        for i in range(h - 1):
            n = len(l)
            for j in range(n):
                l.append(l[j] + " " * (2 * n - 1 - 2 * j) + l[j])
        w = 6 * 2 ** (h - 1) - 1
        for i in range(len(l)):
            print(l[i].center(w))
        for i in range(h):
            print("*".center(w))
    except:
        break
