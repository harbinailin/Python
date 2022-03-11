import xlrd

# 代码格式化 Ctrl Alt L
# 读取Excel文件 支持两种格式xls xlsx
file_name = r'C:\Users\86159\PycharmProjects\pytest\xlrd_test\info.xlsx'
sheet_name = 'Sheet1'
book = xlrd.open_workbook(file_name)
sh1 = book.sheet_by_name(sheet_name)
rows = sh1.nrows
cols = sh1.ncols
print('行数：{},列数：{}'.format(rows, cols))
row1 = sh1.row_values(0)
print('输出表格中的第一列：', row1)
col1 = sh1.col_values(0)
print('输出表格中的第一行', col1)
a1 = sh1.cell(0, 2)
print('输出表格中的a2单元格内容', a1.value)
# 输出每行内容
for i in range(sh1.nrows):
    print(sh1.row_values(i))
