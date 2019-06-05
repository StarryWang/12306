
# 对网页的下载和解析
# 模块存放是对得到的url进行提取和解析的函数
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


# 传入list_url得到列车及其对应的编码的文本
def get_station_list(list_url):
    try:                    # try-except 处理异常
        headers = {
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3)AppleWebkit/537.36(KHTML, like Gecko) '
                          'Chrome/65.03325.162 Safari/537.36'
        }
        response = requests.get(list_url, headers=headers)  # 传入参数headers，不然可能无法正常请求url
        if response.status_code == 200:     # 状态码为200，说明服务器正常处理请求
            return response.text
        return None
    except RequestException:
        return None


# 得到列车的信息
def get_infor_train(url_infor_train):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3)AppleWebkit/537.36(KHTML, like Gecko) '
                          'Chrome/65.03325.162 Safari/537.36'
        }
        response = requests.get(url_infor_train, headers=headers)       # 传入参数headers，不然可能无法正常请求url
        if response.status_code == 200:      # 状态码为200，说明服务器正常处理请求
            return response.text             # 返回得到的文本
        return None
    except RequestException:
        return None


# 解析得到列车的信息
def parse_infor(response):
    soup = BeautifulSoup(response, 'html.parser')   # 使用BeautifulSoup库对得到的信息进行解析，熬一锅汤
    str_tmp = str(soup)     # 将熬好的汤字符串化
    rep_soup = str_tmp.replace("true", "'true'")    # 用'true'代替true，方便字典化
    mes = eval(rep_soup)    # 字典化
    return mes

