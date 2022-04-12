def quickSort(iList):
    if len(iList) <= 1:
        return iList
    left = []
    right = []
    for i in iList[1:]:
        if i <= iList[0]:
            left.append(i)
        else:
            right.append(i)
    return quickSort(left) + [iList[0]] + quickSort(right)


if __name__ == '__main__':
    iList = [4, 5, 9, 6, 7, 1, 3]
    print(quickSort(iList))
