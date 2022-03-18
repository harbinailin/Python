def jumpFloor(number: int) -> int:
    if number < 3:
        return number
    else:
        a, b = 1, 2
        for i in range(number - 2):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    print(jumpFloor(10))
