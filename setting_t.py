# 模块存放一些其他其他函数
import re


# 将车站和它们的代号构成一个字典
def station_dict(stations_list):
    # 强大的正则表达式 [\u4e00-\ufa5] 表示匹配中文字符
    # 将 车站 和其 编码 提取出来 格式：车站|编码
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', stations_list)
    sta_cod = dict(stations)    # 将其字典化，每个车站对应着它自己的代码
    # cod_sta = {c: s for s, c in sta_cod.items()}
    return sta_cod         # 返回 格式为：车站|编码 的字典


# 日期输入函数 将使用者 需要查询的日期输入
# def data_infor_input():
    # station_data = input("Please input the data that like (20180814):")
    # return station_data


# 出发站的信息输入
# def from_infor_input():
    # from_sta = input("From station:")
    # return from_sta


# 终点站的信息输入
# def to_infor_input():
    # to_sta = input("To station:")
    # return to_sta

