# def f(a, b):
#     if b == 0:
#         return a
#     else:
#         return f(b, a % b)
#
#
# a = int(input("Enter a natural number: "))
# b = int(input("Enter another natural numbers: "))
# print(f(a, b))


# list = [1, 2, 3, 4, 5, 6]
# print(list[10:])

# strs = 'abcd12efg'
# print(strs.upper().title())

# a = 0 or 1 and True
# print(a)

a=[1, 2, 3, 4, 5]
sums = sum(map(lambda x: x + 3, a[1::3]))
print(sums)