from datetime import datetime


class stock_information(object):

    # { 个股资讯的格式
    #     "Art_UniqueUrl": "http://stock.eastmoney.com/a/202009091626257445.html",
    #     "Art_Title": "<em>共达电声</em>9月9日盘中跌幅达5%",
    #     "Art_Url": "http://stock.eastmoney.com/news/1944,202009091626257445.html",
    #     "Art_CreateTime": "2020-09-09 10:39:33",
    #     "Art_Content": "以下是<em>共达电声</em>在北京时间9月9日10:37分盘口异动快照：9月9日，<em>共达电声</em>盘中跌幅达5%，截至10点37分，报9.64元，成交1.85亿元，换手率5.23%。分笔10:37:549.64188↓10:37:519.65188↑10:37:489.653350↓10:37:459..."
    # }

    def __init__(self, Art_UniqueUrl, Art_Title, Art_Url, Art_CreateTime, Art_Content):
        self._art_UniqueUrl = Art_UniqueUrl
        self._art_Title = Art_Title.strip()
        self._art_Url = Art_Url
        self._art_CreateTime = Art_CreateTime
        self._art_Content = ''.join(Art_Content.split())
        self._art_timestamp = datetime.strptime(Art_CreateTime, '%Y-%m-%d %H:%M:%S').timestamp()

    @property
    def art_UniqueUrl(self):
        return self.__art_UniqueUrl

    @art_UniqueUrl.setter
    def art_UniqueUrl(self, Art_UniqueUrl):
        self._art_UniqueUrl = Art_UniqueUrl

    @property
    def art_Title(self):
        return self._art_Title

    @art_Title.setter
    def art_Title(self, Art_Title):
        self._art_Title = str(Art_Title).strip()

    @property
    def art_Url(self):
        return self._art_Url

    @art_Url.setter
    def art_Url(self, Art_Url):
        self._art_Url = Art_Url

    @property
    def art_CreateTime(self):
        return self._art_CreateTime

    @art_CreateTime.setter
    def art_CreateTime(self, Art_CreateTime):
        self._art_CreateTime = Art_CreateTime

    @property
    def art_Content(self):
        return self._art_Content

    @art_Content.setter
    def art_Content(self, Art_Content):
        self._art_Content = Art_Content

    @property
    def art_timestamp(self):
        return self._art_timestamp
