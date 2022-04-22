a = "  *   "
b = " * *  "
c = "* * * "
d = " " * 3
while True:
    try:
        n = int(input())
        for i in range(1, n + 1):
            print(d * (n - i) + a * i)
            print(d * (n - i) + b * i)
            print(d * (n - i) + c * i)
        w = 6 * n - 1
        for i in range(n):
            print("*".center(w))
    except:
        break
