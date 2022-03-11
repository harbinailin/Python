# openpyxl写入Excel文件步骤
# 1、导包
# 2、打开Excel文件
# 3、打开工作表
# 4、写入内容
# 5、保存文件,或另存为
# 不支持xls文件格式 解决措施：可以将xls文件转化为xlsx文件
# openpyxl也是Python Excel的拓展库, openpyxl可以读写修改xlsx文件。对xls文件进行写操作可以使用xlwt库
import openpyxl

file_name = r'C:\Users\86159\Desktop\api.xlsx'
sheet_name = 'Sheet1'
book = openpyxl.load_workbook(file_name)
# sh1 = book.get_sheet_by_name(sheet_name)
sh1 = book[sheet_name]
# f2\f3 pass
# 写入单元格
sh1['F2'] = 'PASS'
sh1['F3'] = 'FALSE'
# 坐标写入 openpyxl索引从1开始 wlrd索引从0开始
sh1.cell(1, 1).value = 'name'
# 写入一行 append追加在原本文件的后面
new_row = ['post-xml-new接口', 'post', 'https://baidu.com/post']
sh1.append(new_row)
# 保存文件
book.save(file_name)
# 另存为新文件
book.save('newapi.xlsx')
