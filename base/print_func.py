# 一个模块中有__name__
# 1. 直接运行 __name__为 __main__
# 2. 调用该模块,__name__为被调用模块的 模块名
print('HelloWorld!')
print('__name__value: ', __name__)


def main():
    print('This message is from main function')


if __name__ == '__main__':
    main()
