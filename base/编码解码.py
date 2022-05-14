import urllib

line = "123456"
urllib.quote(line.decode("gbk").encode("utf-16"))
# 编码解码过程
# 现根据程序编码 在倒序解码显示
# decode 编码 encode解码 urllib.qoute url编码
# 代码顺序是 gbk编码->utf-16解码->url编码
# 倒序后 url解码->utf-16编码->gbk解码
