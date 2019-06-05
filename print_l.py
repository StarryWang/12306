# 打印列表


def print_list(kk, k_tmp, parse_after_list, cod_sta):
    k_s = {}                # 构建一个空字典 用来存放需要可视化的数据
    if parse_after_list['messages'] != []:  # 如果不为空，则说明日期不对
        print('SO sorry, You choose the tickets is not the Pre sale data ！\n')
    elif parse_after_list['data']['result'] == [] and parse_after_list['messages'] == []:
        print('So sorry ,NO Train you that choose！\n')
    else:
        mes = parse_after_list['data']['result']    # 列车的信息都存在 data 下的 result

        # 构建空列表来存放各个信息
        tra_cod = []  # 车次
        sta_beg = []  # 始发站
        sta_end = []  # 终到站
        sta_lea = []  # 起始站
        sta_arr = []  # 终点站
        t_lea = []    # 出发时间
        t_arr = []    # 到达时间
        t_dur = []    # 历时
        t_dat = []    # 出发日期
        tic = []      # 是否有票
        gr = []       # 高级软卧
        rw = []       # 软卧
        rz = []       # 软座
        wz = []       # 无座
        yw = []       # 硬卧
        yz = []       # 硬座
        edz = []      # 二等座
        ydz = []      # 一等座
        swz = []      # 商务座
        dw = []       # 动卧
        for i in range(0, len(mes)):  # 根据字符串特征提取相关信息
            for j in range(0, len(mes[i])):
                k_tmp = mes[i].find('|', k_tmp + 1)
                if k_tmp == -1:
                    break
                kk.append(k_tmp)
            tra_cod.append(mes[i][(kk[2] + 1):kk[3]])
            sta_beg.append(cod_sta[mes[i][(kk[3] + 1):kk[4]]])
            sta_end.append(cod_sta[mes[i][(kk[4] + 1):kk[5]]])
            sta_lea.append(cod_sta[mes[i][(kk[5] + 1):kk[6]]])
            sta_arr.append(cod_sta[mes[i][(kk[6] + 1):kk[7]]])
            t_lea.append(mes[i][(kk[7] + 1):kk[8]])
            t_arr.append(mes[i][(kk[8] + 1):kk[9]])
            t_dur.append(mes[i][(kk[9] + 1):kk[10]])
            tic.append(mes[i][(kk[10] + 1):kk[11]])
            t_dat.append(mes[i][(kk[12] + 1):kk[13]])
            gr.append(mes[i][(kk[20] + 1):kk[21]])
            rw.append(mes[i][(kk[22] + 1):kk[23]])
            rz.append(mes[i][(kk[23] + 1):kk[24]])
            wz.append(mes[i][(kk[25] + 1):kk[26]])
            yw.append(mes[i][(kk[27] + 1):kk[28]])
            yz.append(mes[i][(kk[28] + 1):kk[29]])
            edz.append(mes[i][(kk[29] + 1):kk[30]])
            ydz.append(mes[i][(kk[30] + 1):kk[31]])
            swz.append(mes[i][(kk[31] + 1):kk[32]])
            dw.append(mes[i][(kk[32] + 1):kk[33]])
            for h in range(0, len(gr)):  # 表示列车不存在相关票种
                if gr[h].strip() == '':
                    gr[h] = '--'
                if rw[h].strip() == '':
                    rw[h] = '--'
                if rz[h].strip() == '':
                    rz[h] = '--'
                if wz[h].strip() == '':
                    wz[h] = '--'
                if yw[h].strip() == '':
                    yw[h] = '--'
                if yz[h].strip() == '':
                    yz[h] = '--'
                if edz[h].strip() == '':
                    edz[h] = '--'
                if ydz[h].strip() == '':
                    ydz[h] = '--'
                if swz[h].strip() == '':
                    swz[h] = '--'
                if dw[h].strip() == '':
                    dw[h] = '--'
            k_tmp = -1
            del kk[0:(len(kk) + 1)]
        # 输出格式统一
        tplt = "{:^5}\t{:^5}\t{:^5}\t{:^5}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}"
        # 使用 Python 中强大的字符串格式化函数 format() 将格式统一输出
        print(tplt.format("车次", "车站", "时间", "历时", "商务座", "一等座", "二等座", "高级软卧", "软卧", "动卧", "硬卧",
                          "软座", "硬座", "无座",
                          chr(12288)))
        for i in range(0, len(mes)):
            print(tplt.format(tra_cod[i], sta_lea[i], t_lea[i], t_dur[i], swz[i], ydz[i], edz[i], gr[i], rw[i], dw[i],
                              yw[i], rz[i], yz[i], wz[i], chr(12288)))
            print(tplt.format("", sta_arr[i], t_arr[i], "", "", "", "", "", "", "", "", "", "", "", chr(12288)))
            print("")
            k_s[tra_cod[i]] = t_dur[i]
    return k_s
