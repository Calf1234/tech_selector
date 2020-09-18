from datetime import datetime


class stock_report(object):
    # { 个股研报的格式
    #     'Title': '疫情导致业绩短期承压，5G放量依旧可期',
    #     'PUBLISHDATE': '2020-08-27 00:00:00',
    #     'Url': 'http://data.eastmoney.com/report/zw_stock.jshtml?encodeUrl=BmiolVIlr6KZkgoJQ09hBe8NSWD5/MhonF1FM3bjndI=',
    #     'StockName': '<em>中新赛克</em>',
    #     'INFOBODYCONTENT': ''}

    def __init__(self, Title, PUBLISHDATE, Url, StockName, INFOBODYCONTENT):
        self._report_title = Title
        self._report_publishdate = PUBLISHDATE
        self._report_url = Url
        self._report_stockname = StockName
        self._report_infobodycontent = INFOBODYCONTENT
        self._report_timestamp = datetime.strptime(PUBLISHDATE, '%Y-%m-%d %H:%M:%S').timestamp()

    @property
    def report_timestamp(self):
        return self._report_timestamp

    @property
    def report_publishdate(self):
        return self._report_publishdate

    @property
    def report_url(self):
        return self._report_url

    @property
    def report_stockname(self):
        return self._report_stockname

    @property
    def report_title(self):
        return self._report_title

    @property
    def report_infobodycontent(self):
        return self._report_infobodycontent

    def __str__(self):
        report = 'Title: %s, PUBLISHDATE: %s, Url: %s, StockName: %s, INFOBODYCONTENT: %s' % (
            self._report_title, self._report_publishdate, self._report_url, self._report_stockname,
            self._report_infobodycontent)

        return report
