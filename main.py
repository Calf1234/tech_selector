#-*- coding: utf-8 -*-
import json
import math
import time

import matplotlib
import matplotlib.pyplot as plt
import requests


# reqests 模块 get请求，
# 请求指定的url地址，然后返回响应内容给调用者
def http_reqeust(url, data):
    print(">>>>> http_reqeust" + "\n")
    r = requests.get(url, params=data)
    if (r.status_code != 200):
        print("reqeust error, code: " + r.status_code + "\n")
        return

    r.encoding = 'utf-8'
    print("request ok, url: " + r.url + ", \ncontent: " + r.text + "\n")
    return str(r.text)


# 数据解析，解析url返回的数据
# 指定格式，[（time，prices）,（time，prices), ...]
def parse_data(res):
    global prePrice
    print(">>>>> parse_data" + "\n")

    if (res == None):
        print("parse error, res: " + res)
        return []

    result = res[res.find("(") + 1: res.rfind(")")]
    # print("format: json, " + result + "\n")

    data = json.dumps(json.loads(result)['data'])
    # print("parse, data: " + data + "\n")

    if (str(json.loads(data)['code']) == '399905'):
        prePrice = json.loads(data)['prePrice']
    details = json.loads(data)['details']
    print("parse, data[prePrice]: " + str(prePrice) + ", data[details]: " + str(details) + "\n")

    if details[0] is None:
        print("parse error, data[details] is []" + "\n")
        return

    # 取一个时间点，到时可以标记在横轴上，精度：min
    tim = str(details[0]).split(",")[0]
    tim = tim[0:tim.rfind(":")]
    # 存储对应指数的点，目前是 中证500指数的点
    result = []
    for item in details:
        # 11:26:30,5681.03,26168,0,2
        # 时间，指数点数，
        # print("item: " + item)
        result.append((totimestamp(str(item).split(",")[0]), float(str(item).split(",")[1])))

    # print("\n" + "parse ok, result: " + str(result) + "\n")
    return result


# time: 09:30转换成时间戳，当天的
def totimestamp(tim):
    localtime = time.localtime()
    formattime = str(localtime.tm_year) + "-" + str(localtime.tm_mon) + "-" + str(localtime.tm_mday) + ' ' + tim
    timestamp = int(time.mktime(time.strptime(formattime, '%Y-%m-%d %H:%M:%S')))
    # print("tim: " + tim + ", formattime: " + formattime + ", timestamp: " + str(timestamp))
    return timestamp


# 获取指定股票代码的 分时数据
def get_data_by_secid(secid, cnt):
    url = "http://push2.eastmoney.com/api/qt/stock/details/get"

    params = {
        "secid": secid,  # secid：股票代码id
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",  # ut：
        "fields1": "f1,f2,f3,f4,f8",
        "fields2": "f51,f52,f53,f54,f55",
        "pos": -cnt,  # pos: 指定时间或者当前时间往前取多少个数据
        "invt": 2,
        "cb": "jQuery112407215890784356498_1582613030748",
        "_": int(time.time())
    }  # -: 时间戳 非必须

    res = http_reqeust(url, params)

    # 解析 中证500指数的请求结果
    data = parse_data(res)
    return data


if __name__ == '__main__':
    global prePrice
    print(">>>>> main" + "\n")

    # plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.rcParams['figure.figsize'] = (8.0, 4.0)  # 分辨率
    plt.rcParams['savefig.dpi'] = 140  # 图片像素
    plt.rcParams['figure.dpi'] = 140  # 图片像素

    # Q1. ok
    # url优化，将 param参数分隔开
    # param参数的含义 尽量备注上

    # Q2. ok
    # 每天第一次运行的时候 抓数据应该从9:30开始，
    # 而不是当前时间前一分钟
    tm = time.localtime().tm_hour * 60 + time.localtime().tm_min
    cnt = 0
    cntpermin = 1000  # 每分钟抓11条数据
    if (tm < (9 * 60 + 30)):  # 上午开盘前，9点半
        cnt = 0
    elif (tm < (11 * 60 + 30)):  # 上午休盘前，11点半
        cnt = (tm - (9 * 60 + 30)) * cntpermin
    elif (tm < (13 * 60)):  # 下午开盘前，13点
        cnt = (2 * 60) * cntpermin
    elif (tm < 15 * 60):
        cnt = (2 * 60 + tm - (13 * 60)) * cntpermin
    else:
        cnt = 4 * 60 * cntpermin

    # 数据可视化
    # 中证500：0.399905
    data = get_data_by_secid(0.399905, cnt)

    # Q3. ok
    # 先拉取中证500指数 昨天收盘的点数
    value = prePrice
    print("value: " + str(value))

    plt.axis([totimestamp("09:25:01"), totimestamp("15:00:01"), math.floor(value * 0.95), math.ceil(value * 1.06)])

    xticks = range(totimestamp("09:30:00"), totimestamp("15:00:01"), 60 * 30)
    labels = []
    for xtick in xticks:
        timeArray = time.localtime(xtick)
        otherStyleTime = time.strftime("%H:%M", timeArray)
        # otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        labels.append(otherStyleTime)

    plt.xticks(xticks, labels, rotation=10)  # x轴刻度清空
    # 设置下涨停幅限制：跌 5个点、涨 6个点以内
    plt.yticks(range(math.floor(value * 0.95), math.ceil(value * 1.06), 60))  # y轴刻度

    # 绘制昨天收盘的点
    plt.axhline(y=value, color='black', linestyle='-', linewidth=1.5)
    for y in range(math.floor(value * 0.95), math.ceil(value * 1.06), 30):
        # 绘制平行于x轴的水平参考线
        plt.axhline(y=y, color='red', linestyle='--', linewidth=0.5)

    # 从数据里面分离出x、y
    xdot = []
    ydot = []
    # IC2004：8.061104
    for (x, y) in data:
        xdot.append(x)
        ydot.append(round(y))
    plt.plot(xdot, ydot, color='r', label="中证500")

    xdot.clear()
    ydot.clear()
    data = get_data_by_secid(8.061104, cnt)
    for (x, y) in data:
        xdot.append(x)
        ydot.append(round(y))
    plt.plot(xdot, ydot, color='y', label="IC2004", linewidth=0.8, alpha=0.8)

    xdot.clear()
    ydot.clear()
    data = get_data_by_secid(8.061105, cnt)
    for (x, y) in data:
        xdot.append(x)
        ydot.append(round(y))
    plt.plot(xdot, ydot, color='b', label="IC2005", linewidth=0.8, alpha=0.8)

    plt.legend()

    plt.title(u'中证500 期指分时图')

    plt.show()

    # Q4. todo
    # 实时刷新，当天第一次同步完数据后，
    # 后面的数据需要实时同步

