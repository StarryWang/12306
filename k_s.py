import matplotlib.pyplot as plt


# 可视化函数
# 将每个列车所经历的的时间可视化，方便用户选择更合理的方案
def ke_shi_hua(ks):
    x = list(ks.keys())     # 取出ks(列车的 code 和 其历时)的 键 并用list将其列表化
    y = []                  # 建立一个空列表，用来存放 y 值
    y_j = list(ks.values())     # 取出 ks 的 值 并将去列表化
    for i in range(len(y_j)):   # for循环用来对 y 进行赋值
        s = int(y_j[i].split(':')[0])   # 使用方法 split 将小时和分钟分开 并将其 int 化，虽然 eval 函数也可以int化，但当
        f = int(y_j[i].split(':')[1])   # 小时或分钟 为 0x 时，就有bug了，好坑。
        y.append(s*60 + f)              # 转化为分钟并将其放入列表 y 中

    plt.figure(figsize=(18, 9))         # 使用figure函数创建一个 18*9 英寸的图形
    plt.plot(x, y, color='b', marker='p')       # 传入参数给 函数plot 它将绘制有意义的图形

    # 设置图表的 标题 并给 x y 坐标轴加上标签 并设置其 字体 的大小
    plt.title("Train Running Time", fontsize=25)
    plt.xlabel("Train Code", fontsize=20)
    plt.ylabel("Running Time ", fontsize=20)
    plt.show()      # 打开 matplotlib 查看器
