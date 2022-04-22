while True:
    try:
        n = int(input())
        print("* " * n)
        for i in range(n - 2):
            print("* " + " " * 2 * (n - 2) + "* ")
        print("* " * n)
    except:
        break
