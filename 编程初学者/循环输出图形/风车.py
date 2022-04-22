while True:
    try:
        n = int(input())
        print("*" + " " * (n - 2) + "*" * n)
        for i in range(n - 2):
            print("*" + " " * i + "*" + " " * (n - 3 - i) + "*" + (n - 3 - i) * " " + "*")
        print("*" * (2 * n - 1))
        for i in range(n - 2):
            print(" " * (n - 2 - i) + "*" + " " * i + "*" + " " * i + "*" + (n - 3 - i) * " " + "*")
        print(n * "*" + (n - 2) * ' ' + "*")
    except:
        break
