# 读写模式：w:写入新文件，r:读取已有文件，wb:二进制写入，rb:二进制读取，a+:追加，
# 写入文件
with open("./new.txt", "w", encoding="utf-8") as f:
    f.write("\n沙雕女孩没有爱情\t笑死")

# 读取文件
with open("./new.txt", "r", encoding="utf-8") as f:
    print(f.read())  # 读取所有值，作为一个字符串返回
    # print(f.readline())  # 读取一行值，再次调用时从本次读取位置继续下一行读取
    # print(f.readlines())  # 读取所有值 列表格式，每行一个字符串
