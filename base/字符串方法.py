str = "@Hey, You are a lucky dog"
# capitalize()将字符串的第一个字符转化成大写，其他字符转化成小写
a = str.capitalize()
print(a)
print(str.count('a'))
# 检测子串存在有两种方法index和find find找不到返回-1 index找不到报异常
print(str.find('are'))
print(str.find('cat'))
print(str.index('are'))
# print(str.index('cat'))

# isalnum 判断字符串是否是由字母和数字组成的
print(str.isalnum())
a = "21dsbafh2"
print(a.isalnum())

# join将其他类型的数据和字符串进行拼接
s1 = '#'
l1 = ['hhh', 'uuu', 'yyy', 'iii']
print(s1.join(l1))

# isalpha 判断字符串是否是由汉字和字母构成
s2="hhh小笨蛋"
s3="666@@@皮燕子"
print(s2.isalpha())
print(s3.isalpha())

# isdigit 判断字符串是否只由数字构成
s1="123456"
print(s1.isdigit())
s1="113,"
print(s1.isdigit())

# replace
s1="yeyeyeyeyeye"
print(s1.replace('y','e'))
print(s1.replace('y','e',3))

# swapcase 大小写转换
s1="asdffQQQEETY"
print(s1.swapcase())
