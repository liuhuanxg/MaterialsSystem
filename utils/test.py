#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback

import xlrd


def parse_excel_data(file_path):
    try:
        wb = xlrd.open_workbook(file_path)
        sh1 = wb.sheet_by_index(0)
        print(u"sheet %s 共 %d 行 %d 列" % (sh1.name, sh1.nrows, sh1.ncols))
        # 打印获取的行列值
        total_rows = sh1.nrows
        total_ncols = sh1.ncols
        if total_rows > 1 and total_ncols >= 4:
            for row_index in range(total_rows):
                row_data = sh1.row_values(row_index)
                materials_name = row_data[0]
                unit = row_data[1]
                specifications = row_data[2]
                number = row_data[3]
                # print(materials_name, unit, specifications, number)
                yield materials_name, unit, specifications, number
    except:
        print("parse_excel_data error:{}".format(traceback.format_exc()))
        return None


if __name__ == '__main__':
    for data in parse_excel_data("./防疫物品.xlsx"):
        print(data)
