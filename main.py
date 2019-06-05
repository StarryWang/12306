# encoding:utf-8

# 导入各个模块
from get_parse import *
from print_l import *
from judge_t import *
from k_s import *
from gui import *


def main():
    quit_flag = ""      # 退出 结束 程序标志
    person_type = ['ADULT', '0X00']     # 用来选择成人票 or 学生票 来构建一个新url
    print("Please choose you are ADULT or STUDENT")
    j = input("If you are adult please input '0' else please input '1' : ")

    while quit_flag != 'quit':      # 输入 quit 做为程序退出的标志
        flag = [0, 0, 0]    # 标志 flag 做为日期 始发站 终点站全部正确的标志
        kk = []
        k_tmp = -1
        list_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9006'

        stations_list = get_station_list(list_url)
        sta_cod = station_dict(stations_list)

        windnow = Tk()

        windnow.title("The information input")
        windnow.geometry("470x150")
        windnow.geometry("+550+300")
        lable1 = Label(windnow, text="The data:", font=('微软雅黑', 15))
        lable1.grid()
        lable2 = Label(windnow, text="From station:", font=("微软雅黑", 15))
        lable2.grid()
        lable3 = Label(windnow, text="To station:", font=("微软雅黑", 15))
        lable3.grid()

        entry1 = Entry(windnow, font=("微软雅黑", 15))
        entry1.grid(row=0, column=1)
        entry1.insert(15, "20180822")
        dat = entry1.get()

        entry2 = Entry(windnow, font=("微软雅黑", 15))
        entry2.grid(row=1, column=1)
        entry2.insert(15, "焦作")
        fro = entry2.get()

        entry3 = Entry(windnow, font=("微软雅黑", 15))
        entry3.grid(row=2, column=1)
        entry3.insert(15, "郑州")
        to = entry3.get()

        button1 = Button(windnow, text="Ok", command=sure_print(dat=dat, fro=fro, to=to), width=16)
        button1.grid(row=3, column=0, sticky=W)

        button2 = Button(windnow, text="Quit", command=windnow.quit, width=16)
        button2.grid(row=3, column=1, sticky=E)

        windnow.mainloop()
        infor_lis = sure_print(dat=dat, fro=fro, to=to)
        print(infor_lis)

        cod_sta = {c: s for s, c in sta_cod.items()}
        infor_list = infor_judge(flag, sta_cod, infor_lis)
        url_infor_train = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=' + infor_list[0] + \
                          '&leftTicketDTO.from_station=' + infor_list[1] + '&leftTicketDTO.to_station=' \
                          + infor_list[2] + '&purpose_codes=' + person_type[int(j)]
        response = get_infor_train(url_infor_train)
        parse_after_dict = parse_infor(response)
        # print_list(kk, k_tmp, parse_after_dict, cod_sta)
        ks = print_list(kk, k_tmp, parse_after_dict, cod_sta)
        ke_shi_hua(ks)

        quit_flag = input("If you quit, please input 'quit'(If not just input anything):  ")


main()
