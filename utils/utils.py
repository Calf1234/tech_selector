from datetime import datetime, timedelta


def is_stock_opening():
    '''股市是否开盘中

    :return: True：开盘中，False：已收盘
    '''

    date = datetime.now()
    # 周六、周日：休盘日
    # 没有排除节假日
    if date.weekday() in [5, 6]:
        return False;

    # 周一至周五，上午9点半至下午3点：开盘时间
    if (date.hour >= 9 and date.minute > 30) and date.hour <= 15:
        return True;

    return False


def myprint(level, *args):
    ''' level: 1 debug, 2 default, 3 warning, 4 error, 5

    :param level: 打印级别，低于 default_level 就不会打印日志
    :param args: 打印内容
    :return:
    '''

    default_level = 2
    if (level <= default_level):
        return None

    info = ''
    for arg in args:
        info += arg + ' '
    print(info)


def zixun_filterTime():
    ''' 返回指定的过滤时间, 开盘前抓取资讯，要前一天往后的; 开盘后只看当天的资讯

    '''

    time = datetime.now()
    if (time.hour < 10):
        # 10点前抓当天和前一天的资讯内容
        time = time - timedelta(days=1, hours=time.hour, minutes=time.minute)
    else:
        time = time - timedelta(hours=time.hour, minutes=time.minute)
    return time.timestamp()


def get_current_day():
    '''获取当天的时间戳，比如今日是15号，则获取15号0点0分的时间戳

    :return: 返回时间戳
    '''

    time = datetime.now()
    time = time - timedelta(hours=time.hour, minutes=time.minute)
    return time.timestamp()
