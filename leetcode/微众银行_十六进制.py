# 将十进制转换成十六进制 并查看16进制数中有几个字母 输出字母数量 没有输出0
while True:
    try:
        num = int(input())
        hexi = hex(num)
        print(hexi)
        hexi = list(hexi)
        hexi.pop(0)
        hexi.pop(0)
        count = 0
        for i in hexi:
            if i.isalpha():
                count = count + 1
        print(count)
    except:
        break
# yushu = num % 16
# chushu = num // 16
# count = 0
# if yushu > 9:
#     count = count + 1
# while yushu > 9:
#     count = count + 1
#     yushu = yushu // 16
# print(f"{count}")
# # 54%
