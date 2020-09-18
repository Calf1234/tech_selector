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


def yanbao_filterTime():
    '''返回指定的过滤时间, 抓取最近七天的研报

    :return:
    '''

    time = datetime.now()
    time = time - timedelta(days=7, hours=time.hour, minutes=time.minute, seconds=time.second + 1)
    return time.timestamp()


def zixun_filterTime():
    ''' 返回指定的过滤时间, 开盘前抓取资讯，要前一天往后的;
    若是周一开盘前，则要带有周末的资讯; 开盘后只看当天的资讯

    '''

    time = datetime.now()
    if time.weekday() in [5, 6]:
        # 若是周末，则抓周末
        time = time - timedelta(days=(time.weekday() - 5), hours=time.hour, minutes=time.minute, seconds=time.second)
    elif time.weekday() == 0 and time.hour < 10:
        # 若是周一 且 10点前，则抓周末 + 周一
        time = time - timedelta(days=2, hours=time.hour, minutes=time.minute, seconds=time.second)
    elif time.hour < 10:
        # 10点前，则抓前一天 + 现在
        time = time - timedelta(days=1, hours=time.hour, minutes=time.minute, seconds=time.second)
    else:
        # 10点后抓，只抓当天的资讯
        time = time - timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

    return time.timestamp()


def get_current_day():
    '''获取当天的时间戳，比如今日是15号，则获取15号0点0分的时间戳

    :return: 返回时间戳
    '''

    time = datetime.now()
    time = time - timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)
    return time.timestamp()
