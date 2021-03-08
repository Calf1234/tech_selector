# -*- coding: utf-8 -*-

from database import db
from network import net
from parse import parse
from data import techdata


def print_stockReport(stocks, mark='关注的股票列表#研报'):
    print('\n======================%s========================' % (mark))
    print(str(stocks))

    for stock in stocks:
        # 个股研报
        reports = net.get_stockReport(stock)
        if reports is None or len(reports) < 1:
            continue
        print('\n======================%s========================' % (stock))
        for re in reports:
            print(
                'report:' + re.report_title + ', ' + re.report_publishdate + ', \n' + re.report_url + '\n')


def print_stockInfo(stocks, mark='关注的股票列表#资讯'):
    print('\n======================%s========================' % (mark))
    print(str(stocks))

    for stock in stocks:
        # 个股资讯
        infos = net.get_stockInfomation(stock)
        if infos is None or len(infos) < 1:
            continue
        print('\n======================%s========================' % (stock))
        for info in infos:
            print('info:' + info.art_Title + ', ' + info.art_CreateTime + ', \n' + info.art_Content + ', \n' + info.art_UniqueUrl + '\n')


if __name__ == '__main__':
    global prePrice
    print(">>>>> main" + "\n")

    opt = db.operate()
    # net.get_kline('002912')
    obj = net.get_stockComment('002912')
    print(str(techdata.techdata_2_json(obj)))

    #####################################################
    # 1. 展示相关个股的资讯
    #####################################################
    # stocks = opt.query_stock_by_group(a_h=1)
    # names = [stock[1] for stock in stocks]
    # print_stockInfo(names, mark='all')

    #####################################################
    # 2. 展示相关个股的研报
    #####################################################
    # stocks = opt.query_stock_by_group()
    # names = [stock[1] for stock in stocks]
    # print_stockReport(names)

    #####################################################
    # 3. 同步相关个股的行情数据
    #####################################################
    # # 若有当天的行情数据，则先删除再同步
    # opt.delete_today_marketdata()
    # stocks = opt.query_allstock()
    # for stock in stocks:
    #     data = net.get_daily_makertData(stock[0])
    #
    #     if not data is None:
    #         data = parse.dict2marketData(data)
    #         opt.insert_marketData(data)
    #     else:
    #         # 行情数据获取失败，打印是哪个股票获取失败
    #         print(str(stock) + '\n\n')

    #####################################################
    # Tkinter GUI
    #####################################################
    pass
