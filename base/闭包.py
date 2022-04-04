#
def f1(n):
    def f2(x):
        return (x + n)

    return f2


# p1 = f1(n=2)
# print(p1(x=6))
p1 = f1(2)
print(p1(6))
