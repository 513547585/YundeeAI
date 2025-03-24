# coding=utf8
import random
import xlrd
import os
import sys
import datetime


# 身份证前六位
def file_ID():
    # dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    os.path.realpath(sys.argv[0])
    # print(os.path.realpath(sys.argv[0]))
    # dir_parth = dirname + '\city.xls'
    # data_excel = xlrd.open_workbook(r'\Selenium_Chandao\Unit_tools\city.xls','utf-8')
    data_excel = xlrd.open_workbook(r'city.xls', 'utf-8')
    # names = data_excel.sheet_names()  # 获取所有sheet名称
    table1 = data_excel.sheets()[0]  # 通过索引顺序获取sheet
    # 获取文件的sheet 行数 列数
    sheet_name = table1.name  # sheet
    rows_number = table1.nrows  # 行数
    cols_number = table1.ncols  # 列数
    row_value = table1.row_values(0)  # 第一行 值
    col_value = table1.col_values(5)  # 列值
    # cell_value = table1.cell_value(0, 5)  # 第一行 第五列
    alist = []
    # 编列身份证前6位数
    for i in range(1, len(col_value)):
        alist.append(col_value[i])
    print(alist)  # 装进集合的所有证件号前六位
    return str(random.choice(alist))


def ID_Cards():
    # 获取当前年
    now_year = datetime.datetime.now()
    Nowyear = now_year.year
    # 年
    age_year = str(random.randint(1960, Nowyear))
    # 月
    mounths = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    age_month = random.choice(mounths)
    # 天
    day = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
           "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
    age_day = random.choice(day)
    Last_number=str(random.randrange(111, 999))
    # 身份证号
    ID_numbei_temp = file_ID() + age_year + age_month + age_day+Last_number
    sums = 0
    xishu = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    yushu = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    count = 0
    for i in range(17):
        count += int(ID_numbei_temp[i]) * xishu[i]
        last = count % 11
    IdNumbers = str(ID_numbei_temp) + str(yushu[last])
    print("生成身份证号：  "+IdNumbers)
    return IdNumbers


if __name__ == '__main__':
    print(file_ID())
