import json
from datetime import datetime

import requests

from parse import parse
from utils import utils
from data import techdata


def get_daily_makertData(code):
    '''获取指定股票的当日行情数据，在收盘后才可以调用

    :param code: 股票代码
    :return: dict类型，or None
    '''
    if not (isinstance(code, str) or isinstance(code, int)):
        utils.myprint(3, 'get_daily_makertData, 参数类型不合法，code: ' + str(code))
        return None
    if not str(code).isdigit() or len(str(code)) > 6:
        utils.myprint(3, 'get_daily_makertData, 参数要求不合法，code: ' + str(code))
        return None

    if utils.is_stock_opening():
        utils.myprint(2, 'get_daily_makertData, 开盘期间不建议此时同步行情数据')

    if str(code).startswith(('600', '601', '603')):
        # 沪市股票
        secid = '1.%06d' % (int(code))
    else:
        secid = '0.%06d' % (int(code))

    timestamp = datetime.now().timestamp()
    response = requests.get(
        'http://push2.eastmoney.com/api/qt/stock/get',
        params={'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
                'fltt': '2',
                'invt': '2',
                'fields': 'f120,f121,f122,f174,f175,f59,f163,f43,f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f262,f263,f264,f267,f268,f255,f256,f257,f258,f127,f199,f128,f198,f259,f260,f261,f171,f277,f278,f279,f288,f152,f250,f251,f252,f253,f254,f269,f270,f271,f272,f273,f274,f275,f276,f265,f266,f289,f290,f286,f285,f292,f293,f294,f295',
                'secid': '%s' % secid,
                '_': timestamp})

    utils.myprint(1, 'get_daily_makertData, http request, url: ' + response.url)
    if response.status_code != 200:
        utils.myprint(3, 'get_daily_makertData, http request error, status_code: ' + str(
            response.status_code) + ', url: ' + response.url)
        return None

    utils.myprint(1,
                  'get_daily_makertData, http request, content: ' + response.content.decode('utf-8', errors='ignore'))
    # json 反序列化成 Python dict
    content = json.loads(response.content)

    if 'data' in content:
        data = content['data']
        if data is None:
            utils.myprint(3, 'get_daily_makertData, data is None, code: %s, \nurl: %s' % (code, response.url))
    else:
        data = None
        utils.myprint(3, 'get_daily_makertData, no data in content, code: ' + code)

    utils.myprint(1, 'get_daily_makertData, return: ' + str(data))
    return data


def get_stockInfomation(name):
    '''获取个股资讯，根据指定股票名字来搜索

    :param name:
    :return:
    '''

    response = requests.get(
        'http://searchapi.eastmoney.com//bussiness/Web/GetCMSSearchList',
        params={
            'type': 8193,
            'pageindex': 1,  # 查询第几页
            'pagesize': 10,  # 一页多少条资讯
            'keyword': name,
            'name': 'zixun',
            '_': datetime.now().timestamp()
        },
        headers={
            'Referer': requests.get('http://so.eastmoney.com/News/s', params={'keyword': name}).url}
    )

    if response.status_code != 200:
        utils.myprint(3, 'get_stockInfomation, http request error, status_code: ' + str(
            response.status_code) + ', url: ' + response.url)
        return None

    # { 请求对应的 响应内容
    #     "IsSuccess": true, # 判断是否请求成功
    #     "Code": 0,
    #     "Message": "成功",
    #     "TotalPage": 66, # 一共有多少页
    #     "TotalCount": 651, # 一共有多少条资讯
    #     "Keyword": "0.002655",
    #     "Data": Array[10], # 个股资讯
    #     "RelatedWord": "",
    #     "StillSearch": [
    #         "共达电声",
    #         "共达电声"
    #     ],
    #     "StockModel": {
    #         "Name": "共达电声",
    #         "Code": "002655"
    #     }
    content = response.content.decode('utf-8', errors='ignore')
    utils.myprint(1, 'get_stockInfomation, http request, content: ' + content)

    content = json.loads(content)
    if not content['IsSuccess']:
        utils.myprint(3, 'get_stockInfomation, http request, IsSuccess: False, so not Data')
        return None

    utils.myprint(2, 'get_stockInfomation, http request, name: ' + name + ', TotalPage: ' + str(
        content['TotalPage']) + ', TotalCount: ' + str(content['TotalCount']))

    infos = parse.data2stockInfo(content['Data'])
    timestamp = utils.zixun_filterTime()
    return [info for info in infos if info.art_timestamp > timestamp]


def get_stockReport(name):
    '''获取个股资讯，根据指定股票名字来搜索

    :param name:
    :return:
    '''

    response = requests.get(
        'http://searchapi.eastmoney.com/bussiness/Web/GetSearchList',
        params={
            'type': 501,
            'pageindex': 1,  # 查询第几页
            'pagesize': 10,  # 一页多少条资讯
            'keyword': name,
            'name': 'normal',
            '_': datetime.now().timestamp()
        },
        headers={
            'Referer': requests.get('http://so.eastmoney.com/Ann/s', params={'keyword': name}).url}
    )

    if response.status_code != 200:
        utils.myprint(3, 'get_stockReport, http request error, status_code: ' + str(
            response.status_code) + ', url: ' + response.url)
        return None

    content = response.content.decode('utf-8', errors='ignore')
    utils.myprint(1, 'get_stockReport, http request, content: ' + content)

    content = json.loads(content)
    if not content['IsSuccess']:
        utils.myprint(3, 'get_stockReport, http request, IsSuccess: False, so not Data')
        return None

    utils.myprint(2, 'get_stockReport, http request, name: ' + name + ', TotalPage: ' + str(
        content['TotalPage']) + ', TotalCount: ' + str(content['TotalCount']))

    infos = parse.data2stockReport(content['Data'])
    timestamp = utils.yanbao_filterTime()
    return [info for info in infos if info.report_timestamp > timestamp]


def get_kline(code):
    '''根据股票代码来获取 K线图数据，默认是日K

    :param code: 股票代码
    :return:
    '''

    # 检查股票代码 code是否合法
    response = requests.get(
        url='http://push2his.eastmoney.com/api/qt/stock/kline/get?cb=?',
        params={
            # f1: 股票代码，f3：股票名字，f5：k线数据长度
            'fields1': 'f1,f2,f3,f4,f5,f6',
            # f51：时间，f52：开盘价，f53：收盘价，f54：最高价，f55：最低价
            # f56：涨跌幅，f57：涨跌额，f58：成交量，f59：成交额，f60：振幅，f61：换手率
            'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
            'ut': '7eea3edcaed734bea9cbfc24409ed989',
            'klt': '101',
            'fqt': '0',
            'secid': '0.002912',
            'beg': 0,
            'end': 20500000,
            '_': datetime.now().timestamp()
        })
    print(response.content.decode('utf-8', errors='ignore'))


def get_stockComment(code):
    '''结合千股千评来爬取个股的相关数据，主要是技术指标数据

    :return:
    '''

    # 检查股票代码 code是否合法
    response = requests.get(
        url='http://data.eastmoney.com/stockcomment/API/%s.json' % (str(code)),
        headers={
            'Referer': 'http://data.eastmoney.com/stockcomment/stock/%s.html' % (str(code))
        }
    )
    print(response.content.decode('utf-8', errors='ignore'))

    if (response.status_code != 200):
        print('status_code not 200 %s' %(str(response.status_code)))

    try:
        # 提取技术指标数据，如MACD，BOLL，KDJ等
        data = json.loads(response.content.decode('utf-8', errors='ignore'))['ApiResults']['zj']['Trend'][2][0]
    except:
        print('error, format data: {%s} to json' %(response.content.decode('utf-8', errors='ignore')))
    finally:
        print(str(data))
        return json.loads(str(json.dumps(data)), object_hook=techdata.json_2_techdata)

