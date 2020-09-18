# -*- coding: utf-8 -*-

from database import db
from network import net


def print_stockInfo(stocks, mark='关注的股票列表'):
    print('\n======================%s========================' % (mark))
    infos = []
    for stock in stocks:
        # 个股资讯
        infos = net.get_stockInfomation(stock)

    if infos is None:
        return
    for info in infos:
        print('\ninfo.title:' + info.art_Title + ', ' + info.art_CreateTime + ', \n' + info.art_Content)


if __name__ == '__main__':
    global prePrice
    print(">>>>> main" + "\n")

    opt = db.operate()

    #####################################################
    # 1. 展示相关个股的资讯
    #####################################################
    # stocks = opt.query_stock_by_group(group1=1)
    # names = [stock[1] for stock in stocks]
    # print_stockInfo(names, mark='自选列表1')
    #
    # stocks = opt.query_stock_by_group(group1=4)
    # names = [stock[1] for stock in stocks]
    # print_stockInfo(names, mark='自选列表4')

    #####################################################
    # 2. 同步相关个股的行情数据
    #     que1： 如果一天内同步多次，就会插入多条相同的数据，还需要
    #           补上检查，检查该股票当天是否已经同步过。
    #####################################################
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

    opt.delete_today_marketdata()

    #####################################################
    # Tkinter GUI
    #####################################################
    pass
