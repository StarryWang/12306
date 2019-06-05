# 判断时间的输入
from setting_t import *
from gui import *


# 判断时间的输入格式是否正确
def judge_time_format(flag, station_data, station_dat):
    # 判断输入的日期是否为八位数
    if len(station_data) == 8:

        # 将输入的时期 切开 再 合并 构建一个新的 字符串 作为一个 参数 用来构建一个 新的 url
        station_dat = station_data[0:4] + '-' + station_data[4:6] + '-' + station_data[6:8]

        # 将 station_data[0:4]切片 对应的字符串用函数 eval() 将其当成有效表达式来求值并返回其计算结果
        year = eval(station_data[0:4])

        # 判断月份的第一位数字是否为0 若为0 就取station_data[5] 为0就取切片station_data[4:5]
        if eval(station_data[4]) != 0:
            month = eval(station_data[4:6])
        else:
            month = eval(station_data[5])

        # 判断天的第一位数字是否为0 若为0 就取station_data[7] 为0就取切片station_data[6:8]
        if eval(station_data[6]) != 0:
            day = eval(station_data[6:8])
        else:
            day = eval(station_data[7])

        # 判断月份的正确性
        if month < 1 or month > 12 or day < 0 or day > 31:
            print('The start data is wrong!')
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            flag[0] = 1
        elif month in [4, 6, 9, 11]:
            if day < 31:
                flag[0] = 1
            else:
                print('The start data is wrong!')
        else:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if day < 30:
                    flag[0] = 1
                else:
                    print('The start data is wrong!')
            else:
                if day < 29:
                    flag[0] = 1
                else:
                    print('The start data is wrong!')
    else:
        print('The start data is wrong!')
    return station_dat


def infor_judge(flag, sta_cod, infor_lis):
    while sum(flag) != 3:
        while True:        # 死循环 判断日期时间是否正确，不正确一直输入，直到正确为止，正确通过 break 退出循环
            station_data = infor_lis[0]   # 输入时间
            station_dat = ""                    # 定义一个空字符串，存放 2018-8-15 格式的时间
            judge_time_format(flag, station_data, station_dat)      # 调用函数
            if flag[0] == 1:                                        # 时间格式正确，flag[0] 置 1
                station_dat = judge_time_format(flag, station_data, station_dat)
                break                           # 时间格式正确退出循环
            else:
                print("please input again")

        while True:        # 死循环 判断车站是否正确，不正确一直输入，直到正确为止，正确通过 break 退出循环
            from_sta_j = infor_lis[1]     # 输入 简化的车站信息
            from_sta = from_sta_j        # 拼接 一个完整的车站信息
            if from_sta not in sta_cod.keys():  # 判断 输入的 车站信息是否存在  用方法 keys()
                print("The station can not find.")
            elif from_sta in sta_cod.keys():    # 判断 输入的 车站信息是否存在  用方法 keys()
                flag[1] = 1                     # 车站信息信息正确 flag[1] 置1
                from_sta = sta_cod[from_sta]

            if flag[1] == 1:
                break                           # 车站 格式正确退出循环
            else:
                print("please input the start station again")
        while True:          # 死循环 判断车站是否正确，不正确一直输入，直到正确为止，正确通过 break 退出循环
            to_sta_j = infor_lis[2]       # 输入 简化的车站信息
            to_sta = to_sta_j           # 拼接 一个完整的车站信息
            if to_sta not in sta_cod.keys():  # 判断 输入的 车站信息是否存在  用方法 keys()
                print("The station can not find.")
            elif to_sta in sta_cod.keys():        # 判断 输入的 车站信息是否存在  用方法 keys()
                flag[2] = 1                         # 车站信息信息正确 flag[2] 置1
                to_sta = sta_cod[to_sta]
            if flag[2] == 1:
                break
            else:
                print("please input the end station again")

        inform_list = [station_dat, from_sta, to_sta]
        if sum(flag) == 3:
            return inform_list
