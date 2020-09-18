from utils import utils
from data import information, marketdata
import re


def dict2marketData(data):
    '''提取关键的行情数据

    :param data:
    :return:
    '''
    if data is None:
        utils.myprint(3, 'dict2marketData, data is None')
        return

    return marketdata.marketData(
        data['f57'],  # 股票代码
        data['f58'],  # 股票名字
        data['f43'],  # 最新
        data['f46'],  # 今开
        data['f60'],  # 昨收
        data['f71'],  # 均价
        data['f44'],  # 最高
        data['f45'],  # 最低
        data['f51'],  # 涨停价
        data['f52'],  # 跌停价
        data['f47'],  # 成交量
        data['f48'],  # 成交额
        data['f135'],  # 主力流入
        data['f136'],  # 主力流出
        data['f117'],  # 流通市值
        data['f116'],  # 总市值
        data['f122']  # 今年以来涨跌幅
    )


def data2stockInfo(data):
    '''将 json形式的数据 转换成 list，list内元素是 stock_information类对象

    :param data:
    :return:
    '''
    infos = []
    for info in data:
        utils.myprint(2, 'data2stockInfo, info: ' + str(info))

        # { 个股资讯的格式，来自响应内容的 "Data": Array[10]
        #     "Art_UniqueUrl": "http://stock.eastmoney.com/a/202009091626257445.html",
        #     "Art_Title": "<em>共达电声</em>9月9日盘中跌幅达5%",
        #     "Art_Url": "http://stock.eastmoney.com/news/1944,202009091626257445.html",
        #     "Art_CreateTime": "2020-09-09 10:39:33",
        #     "Art_Content": "以下是<em>共达电声</em>在北京时间9月9日10:37分盘口异动快照：9月9日，<em>共达电声</em>盘中跌幅达5%，截至10点37分，报9.64元，成交1.85亿元，换手率5.23%。分笔10:37:549.64188↓10:37:519.65188↑10:37:489.653350↓10:37:459..."
        # },
        infos.append(information.stock_information(
            info['Art_UniqueUrl'],
            re.sub(r'[</em><em>]', '', info['Art_Title']),
            info['Art_Url'],
            info['Art_CreateTime'],
            re.sub(r'[</em><em>]', '', info['Art_Content'])
        ))
    return infos
